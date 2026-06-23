from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from .serializers import TaskSerializer
from .models import Project, Task, TaskNote, Tag
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
from django.utils import timezone
from django.db.models import Case, Value, When, Q, Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .services import TaskService

# ==========================================
# 🏠 VISTAS GENERALES Y DE INICIO
# ==========================================

# 1. La vista para 'about/' que te pedía antes
def about(request):
    return HttpResponse("Acerca de")

# 2. La vista para 'hello/' que te pide ahora (con el username)
def hello(request, username):
    return HttpResponse(f"<h1>Hola {username}</h1>")

class UpdateTaskAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self,request,task_id):
        # Le delegamos TODO el trabajo al servicio en una sola línea 🚀
        resultado = TaskService.update_user_task(
            task_id=task_id,
            user=request.user,
            data=request.data
        )
        
        if resultado["success"]:
            return Response({
                "success": True,
                "message": "tarea actualizada",
                "data": resultado["data"]
            }, status=status.HTTP_200_OK )
            
            
        return Response({
            "success": False,
            "message": "Error de validación.",
            "errors": resultado["errors"]
        }, status=status.HTTP_400_BAD_REQUEST)




def index(request):
    total_proyectos = Project.objects.filter(state=True).count() 

    # Agrupamos conteos eficientemente en una sola consulta usando Q
    conteos = Task.objects.filter(state=True).aggregate(
        tot_pendientes=Count('id', filter=Q(status='pendiente')),
        tot_progreso=Count('id', filter=Q(status='progreso')),
        tot_completadas=Count('id', filter=Q(status='completada'))
    )
    
    # TICKET
    todas_las_tareas = Task.objects.filter(state=True).select_related('project','user','assigned_to')
    
    lista_pendientes = []
    lista_progreso = []
    lista_completadas  = []
    
    for tarea in todas_las_tareas:
        if tarea.status == 'pendiente':
            lista_pendientes.append(tarea)
        elif tarea.status == 'progreso':
            lista_progreso.append(tarea)
        elif tarea.status == 'completada':
            lista_completadas.append(tarea)
    
    hoy = timezone.now().date()
    tareas_vencidas = Task.objects.filter(state=True, due_data__lt=hoy).count()
    
    return render(request, 'project/index.html', {
        'total_proyectos': total_proyectos,
        'tareas_completadas': conteos['tot_completadas'],
        'tareas_en_progreso': conteos['tot_progreso'],
        'tareas_pendientes': conteos['tot_pendientes'],
        'tareas_vencidas': tareas_vencidas,
        'lista_pendientes': lista_pendientes, 
        'lista_completadas': lista_completadas,
        'lista_progreso': lista_progreso
    })



# ==========================================
# 📁 GESTIÓN DE PROYECTOS (CRUD)
# ==========================================

@login_required
def projects(request):
    termino_buscar = request.GET.get('search', '')
    if termino_buscar:
        proyectos = Project.objects.filter(user=request.user, state=True, name__icontains=termino_buscar)
    else:
        proyectos = Project.objects.filter(user=request.user, state=True)

    return render(request, 'project/projects.html', {'projects': proyectos})

@login_required
def project_detail(request, id):
    # Tu búsqueda blindada impecable
    project = get_object_or_404(Project, id=id, user=request.user, state=True) 
    todas_las_tareas_del_proyecto = project.task_set.filter(state=True)
    
    tareas_totales = todas_las_tareas_del_proyecto.count()
    tareas_completadas = todas_las_tareas_del_proyecto.filter(done=True).count()
    
    if tareas_totales > 0:
        porcentaje_progreso = int((tareas_completadas / tareas_totales) * 100)
    else:
        porcentaje_progreso = 0

    hoy = timezone.now().date()
    filtro = request.GET.get('filtrar_por', 'todas')
    tasks = todas_las_tareas_del_proyecto 
    
    if filtro == 'pendientes':
        tasks = tasks.filter(done=False)
    elif filtro == 'vencidas':
        tasks = tasks.filter(due_data__lt=hoy, done=False)
    elif filtro == 'completadas':
        tasks = tasks.filter(done=True)
        
    tasks = tasks.order_by(
        Case(
            When(priority='Alta', then=Value(1)),
            When(priority='Media', then=Value(2)),
            When(priority='Baja', then=Value(3)),
            default=Value(4)
        ),
        'due_data'
    )
    todos_los_usuarios = User.objects.all()
    todas_las_etiquetas = Tag.objects.all()
    
    return render(request, 'project/project_detail.html', {
        'project': project, 
        'tasks': tasks,
        'hoy': hoy,
        'filtro_activa': filtro,
        'all_tags': todas_las_etiquetas,
        'all_users': todos_los_usuarios,
        'porcentaje': porcentaje_progreso, 
    })

@login_required
def create_project(request):
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {'form': CreateNewProject()})
    else:
        form = CreateNewProject(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.user = request.user
            proyecto.save()
            return redirect('projects')

@login_required
def update_project(request, id):
    # Ojo acá: Tenías user=request, debe ser user=request.user
    proyecto = get_object_or_404(Project, id=id, user=request.user, state=True)
    
    if request.method == 'POST':
        proyecto.name = request.POST['name']
        proyecto.save()
        return redirect('projects')
    
    return render(request, 'project/update_project.html', {'project': proyecto})

@login_required
def project_eliminar(request, id):
    proyecto = get_object_or_404(Project, id=id, user=request.user)
    proyecto.state = False  # Borrado lógico profesional
    proyecto.save()
    return redirect('projects')


# ==========================================
# 📝 GESTIÓN DE TAREAS (CRUD Y ESTADOS)
# ==========================================
def task(request):
    # Trae todas las tareas de la base de datos MySQL
    todas_las_tareas = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': todas_las_tareas})



@login_required
def recibir_id(request, id):
    proyecto = get_object_or_404(Project, id=id, user=request.user, state=True)
    
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        description = (request.POST.get('description') or '').strip()
        priority = request.POST.get('priority', 'Baja')
        
        fecha_texto = request.POST.get('due_data') 
        fecha_limite = None
        
        if fecha_texto:
            fecha_limite = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
            hoy = timezone.now().date()
            if fecha_limite < hoy:
                print("❌ ERROR: La fecha límite no puede ser una fecha pasada.")
                return redirect('project_detail', id=id)

        if title:
            nueva_tarea = Task.objects.create(
                title=title,
                description=description,
                project=proyecto,          
                user=request.user,         
                priority=priority,
                status='pendiente',
                done=False,
                due_data=fecha_limite      
            )
            
            etiquetas_seleccionadas = request.POST.getlist('tags')
            if etiquetas_seleccionadas:
                nueva_tarea.tags.set(etiquetas_seleccionadas)
                
        return redirect('project_detail', id=id)
    return redirect('project_detail', id=id)

@login_required
def task_editar(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__user=request.user)
    
    if request.method == 'GET':
        return render(request, 'task/task_form.html', {'task': task})
        
    task.title = request.POST.get('title', '').strip()
    task.description = request.POST.get('description', '').strip()
    task.priority = request.POST.get('priority', 'Baja')
    task.save()
    
    return redirect('project_detail', id=task.project.id)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__user=request.user)
    project_id = task.project.id
    task.state = False #Aca hice como otros coidogfs que tengo 
    task.save()
    return redirect('project_detail', id=project_id)

@login_required
def complete_task(request, task_id): 
    task = get_object_or_404(Task, id=task_id, project__user=request.user) 

    # 🧠 Si el estado actual es 'completada', el usuario quiere "desmarcarla"
    if task.status == 'completada':
        task.status = 'pendiente'
# 🧠 Si está en cualquier otro estado ('pendiente' o 'progreso'), la marcamos como terminada
    else:
        task.status = 'completada'
    task.save()
    return redirect('project_detail', id=task.project.id)

@login_required
def add_task_note(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, project__user=request.user)
        nota_texto = request.POST.get('note_text', '').strip()

        if nota_texto:
            TaskNote.objects.create(task=task, text=nota_texto)
        return redirect('project_detail', id=task.project.id)
    return redirect('projects')


# ==========================================
# 🏷️ ETIQUETAS Y KANBAN ASÍNCRONO (API)
# ==========================================
@login_required
def create_task(request, id):
    # 1. Buscamos el proyecto usando el ID de la URL y asegurándonos de que sea del usuario logueado
    project = get_object_or_404(Project, id=id, user=request.user)
    
    # 2. MOMENTO POST: El usuario llenó el formulario y apretó "Guardar"
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        description = (request.POST.get('description') or '').strip()
        
        # Validación: Si el título no está vacío, creamos la tarea en MySQL
        if title:
            Task.objects.create(
                title=title, 
                description=description, 
                project=project  # <-- Vinculamos la tarea al proyecto que buscamos arriba
            )
            # Una vez guardada, lo redirigimos directo al detalle del proyecto
            return redirect('project_detail', id=id)
    
    # 3. MOMENTO GET: El usuario recién entra a la página (se saltea el IF de arriba)
    # Le mostramos el formulario HTML vacío y le pasamos el proyecto en el contexto
    return render(request, 'myapp/create_task.html', {'project': project})

@login_required
def create_tag(request, project_id):
    # Protegido por seguridad contra usuarios maliciosos
    
    get_object_or_404(Project, id=project_id, user=request.user, state=True)
    
    if request.method == 'POST':
        nombre = (request.POST.get('name') or '').strip()
        color_hex = request.POST.get('color', '#007bff')
        
        if nombre:
            Tag.objects.create(name=nombre, color=color_hex)
            
    return redirect('project_detail', id=project_id)

class ActualizarEstadoKanbanAPIView(APIView):
    # Le decimos explícitamente a DRF que esta API SOLO entiende JSON.
    # Si alguien intenta mandar un formulario viejo o una imagen, el portero lo rebota.
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,task_id):
        # 💥 MAGIA DE DRF: request.data ya es un diccionario de Python limpio.
        # Gracias al JSONParser, no hace falta usar json.loads(request.body)
        nuevo_estado = request.data.get('estado')
        
        # Traemos la tarea de forma segura
        tarea = get_object_or_404(Task,id=task_id,project__user=request.user)
        
        # -------------------------------------------------------------
        # 🧠 TU DESAFÍO DE LÓGICA (El Ticket 107 que unificamos acá)
        # -------------------------------------------------------------
        estado_validos = ['pendiente','progreso','completada']
        
        if nuevo_estado not in estado_validos:
            return Response({'error':'Estado invalido'}, status=status.HTTP_400_BAD_REQUEST)

        # Regla A: No saltar de pendiente a completada sin trabajar
        if tarea.status == 'pendiente' and nuevo_estado == 'completada':
            return Response({'error':'No podes saltearte el progreso'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Regla B: Si ya estaba completada, está bloqueada
        elif tarea.status == 'completada':
            return Response({'error': 'Esta tarea ya esta bloqueada'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Si pasa los filtros, asignamos y guardamos
        else:
            tarea.status = nuevo_estado
            tarea.save()
            return Response({'success': True}, status=status.HTTP_200_OK)



# ==========================================
# 🔐 SISTEMA DE AUTENTICACIÓN
# ==========================================

def login_view(request):
    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        nombre = request.POST.get('username')  
        contrasenia = request.POST.get('password')

        usuario_validado = authenticate(request, username=nombre, password=contrasenia)

        if usuario_validado is not None:
            auth_login(request, usuario_validado)
            return redirect('projects')
        else:
            return render(request, 'registration/login.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'registration/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login_view')


# ==========================================
# 🤖 DJANGO REST FRAMEWORK (API ENDPOINTS)
# ==========================================

class TaskViewSet(viewsets.ModelViewSet):
    
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(state=True,project__user=self.request.user)
    
    def perform_destroy(self,instance):
        instance.state = False
        instance.save()
        
        
        
        
## ------ TICKETS ----------- ##