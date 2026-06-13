import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework import viewsets
from .serializers import TaskSerializer
from django.core.exceptions import ValidationError
from .models import Project, Task, TaskNote, Tag
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
from django.utils import timezone
from django.db.models import Count, Case, Value, When, Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


# Create your views here.
def index(request):
    total_proyectos = Project.objects.filter(state=True).count() # 👁️ Solo proyectos activos

    # 1. Traemos solo las tareas activas optimizadas de la base de datos
    tareas_activas = Task.objects.filter(state=True).select_related('project', 'user', 'assigned_to')
    
    # 2. Inicializamos listas vacías puras de Python para usar .append()
    # normalmente cuando queremos buscar algo con filter afecta a todo el QuerySet
    conteos = Task.objects.filter(state=True).aggregate(
        tot_pendientes=Count('id',filter=Q(status='pendiente')),
        tot_progreso=Count('id',filter=Q(status='progreso')),# Y despues Q significa query/consulta y para futuro e permite guardar en 'capsula' para poder meter adentro a funciuones como count
        tot_completadas=Count('id',filter=Q(status='completada'))
        
    )
    
    lista_pendientes = Task.objects.filter(status='pendiente').select_related('project','user','assigned_to') # Bueno aca haace lo que hacia anteriormente de state true para que el baseModel ande despues el status es para buscar a la variable o cmo se diga con ese nmombre y el selecet related es para que no ocurrar el problema del N + 1
    lista_progreso = Task.objects.filter(status='progreso').select_related('project','user','assigned_to')
    lista_completadas = Task.objects.filter(status='completada').select_related('project','user','assigned_to')
    
    

    
    hoy = timezone.now().date()
    # Contamos solo las vencidas que estén activas (state=True)
    tareas_vencidas = tareas_activas.filter(due_data__lt=hoy, done=False).count()
    
    # Contamos los totales basados en nuestras listas clasificadas
    tareas_pendientes = len(lista_pendientes)
    tareas_en_progreso = len(lista_progreso)
    tareas_completadas = len(lista_completadas)
    
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


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)
    
    
def about(request):
    username = 'fazt'
    return render(request, "task/about.html", {
        'username': username
    })



@login_required
def projects(request):
    termino_buscar = request.GET.get('search', '')
    
    if termino_buscar:
        # 🕵️‍♂️ Busca por nombre, pero filtrando SÓLO los proyectos del usuario actual
        proyectos = Project.objects.filter(user=request.user, state=True, name__icontains=termino_buscar)
    else:
        # 👤 Si no está buscando nada, trae todos los proyectos del usuario actual
        proyectos = Project.objects.filter(user=request.user,state=True)

    # 🛠️ Ruta corregida: 'project/projects.html'
    return render(request, 'project/projects.html', {
        'projects': proyectos
    })


def task(request):
    #task = Task.objects.get(name=name)
    tareas_pendietes = Task.objects.filter(done=False)
    tareas_completadas = Task.objects.filter(done=True)
    
    return render(request, 'task/task.html', {
        'pendientes': tareas_pendietes,
        'completadas': tareas_completadas
    })





def create_task(request):
    if request.method == 'POST':
        # 1. Debug para ver en la terminal EXACTAMENTE qué te está enviando el HTML
        print("DATOS RECIBIDOS EN POST:", request.POST)
        
        # 2. Capturamos los datos del HTML a mano usando los "name" de tus inputs
        title = request.POST.get('title').strip()
        description = request.POST.get('description', '')
        project_id = request.POST.get('project_id')
        user_id = request.POST.get('user_id')
        priority = request.POST.get('priority', 'Baja')
        
        # 3. Intentamos guardar directamente usando el Modelo para saltarnos las trabas del Form
        try:
            nueva_tarea = Task(
                title=title,
                description=description,
                project_id=project_id,  # Django acepta asignar directamente el ID con _id
                user_id=user_id,        # Lo mismo para el usuario
                priority=priority,
                status='pendiente',
                done=False
                # Si 'deadline' no está en el HTML, no lo ponemos o poné: deadline=None
            )
            nueva_tarea.save()  # Guarda directo en SQLite
            print("¡TAREA GUARDADA CON ÉXITO EN LA BASE DE DATOS!")
            return redirect('index')
            
        except Exception as e:
            print("ERROR AL GUARDAR DIRECTO EN EL MODELO:", e)
            
            # Si falla, le pasamos los datos al form para ver los errores
            form = CreateNewTask(request.POST)
            print("ERRORES DEL FORMULARIO:", form.errors)

    else:
        form = CreateNewTask()
        
    usuarios = User.objects.all()
    proyectos = Project.objects.all()
    
    return render(request, 'task/create_task.html', {
        'form': form,
        'projects': proyectos,
        'users': usuarios
    }) 




def complete_task(request, task_id): # Usamos task_id para que combine con el urls.py
    # Corregí el nombre de la función de Django acá:
    task = get_object_or_404(Task, id=task_id) 
    
    # Tu lógica brillante que invierte el estado:
    task.done = not task.done
    
    # 2. 🔥 TU MISIÓN: Escribí acá el bloque IF / ELSE para actualizar task.status
    # Si task.done es True -> task.status debe ser 'completada'
    # Si task.done es False -> task.status debe ser 'pendiente'
    if task.done:
        task.status = 'completada'
    else:
        task.status = 'pendiente'

    task.save()
    # Para volver al detalle del proyecto, necesitamos el ID del proyecto de ESTA tarea.
    # Django te permite viajar a través del modelo: task.project.id
    return redirect('project_detail', id=task.project.id)



@login_required
def create_project(request):
    if request.method == 'GET':
        # SACALE EL 'templates/'. Empezá directo desde 'project/'
        return render(request, 'project/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        form = CreateNewProject(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.user = request.user
            
            proyecto.save()
            
            return redirect('projects')




def task_editar(request, task_id):
        task = get_object_or_404(Task,id=task_id)
        
        if request.method == 'GET':
            return render(request, 'task/task_form.html',{
                'task':task
            })
        
        title =  request.POST.get('title').strip()
        description =  request.POST.get('description', '')
        
        task.title = title
        task.description = description

        task.save()
        
        return redirect('project_detail',id=task.project.id)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__user=request.user)
    
    # 2. Nos guardamos el ID del proyecto antes de borrar la tarea para poder volver
    project_id = task.project.id
    
    # 3. La borramos de la base de datos con el método mágico .delete()
    task.delete()
    
    # 4. Redireccionamos de vuelta al detalle del proyecto usando su ID
    return redirect('project_detail', id=project_id) # Cambiá 'project_detail' si tu ruta tiene otro name




def add_task_note(request,task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)

        nota_texto = request.POST.get('note_text')

        if nota_texto:
            TaskNote.objects.create(task=task, text=nota_texto)
        
        return redirect('project_detail', id=task.project.id)
    
    return redirect('projects')


@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, id=id, user=request.user, state=True) # Aca puse el user=request.user para buscar bien al usuario y decime si tendira que haber pusto title__icontains etc porque me parece que no decime si esta bien o no 
    
    # Traemos TODAS las tareas asociadas a este proyecto
    todas_las_tareas_del_proyecto = project.task_set.filter(state=True)
    
    # 📊 MATEMÁTICA DEL PROYECTO
    tareas_totales = todas_las_tareas_del_proyecto.count()
    tareas_completadas = todas_las_tareas_del_proyecto.filter(done=True).count()
    
    # --- 💣 AQUÍ ESTÁ EL CAMBIO QUE METÍ (EL BUG) ---
    # Un compañero de equipo intentó optimizar el cálculo del progreso quitando el "if" redundante:
    if tareas_totales > 0:
        porcentaje_progreso = int((tareas_completadas / tareas_totales) * 100)
    else:
        porcentaje_progreso = 0
    # -----------------------------------------------

    # Esto es lo que se muestra en pantalla según los botones de arriba (Filtros)
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
    
    
#   TAREA PARA HACER
def project_eliminar(request,id):
    proyecto = get_object_or_404(Project,id=id,user=request.user)
    
    proyecto.state = False #Lo desactivamos
    proyecto.save() # Guardamos el cambio den la base de datos
    
    return redirect('projects')


    
    
def recibir_id(request, id):
    proyecto = get_object_or_404(Project, id=id,user=request.user) #Aca puse eso debido a que me dijiste que verifique al usuario antes de poder buscar una tarea 
    
    if request.method == 'POST':
        # 1. Capturamos los datos con el blindaje que ya sabés usar
        title = (request.POST.get('title') or '').strip()
        description = (request.POST.get('description') or '').strip()
        priority = request.POST.get('priority', 'Baja')
        
        # 2. Procesamos la fecha límite
        fecha_texto = request.POST.get('due_data') # Captura el string del HTML
        fecha_limite = None
        
        if fecha_texto:
            # 💡 Convertimos el texto "2026-06-09" en una fecha real de Python
            fecha_limite = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
            hoy = timezone.now().date()
            
            # 🔥 TU LÓGICA: Si la fecha ingresada es menor a hoy, frenamos el guardado
            if fecha_limite < hoy:
                print("❌ ERROR: La fecha límite no puede ser una fecha pasada.")
                # Freno de mano: redirige al detalle sin crear la tarea
                return redirect('project_detail', id=id)

        # 3. Si el título es válido y pasó la fecha, creamos la tarea
        if title:
            nueva_tarea = Task.objects.create(
                title=title,
                description=description,
                project=proyecto,          # El objeto proyecto completo
                user=request.user,         # El usuario logueado
                priority=priority,
                status='pendiente',
                done=False,
                due_data=fecha_limite      # Guarda la fecha validada o None si vino vacía
            )
            
            # Guardamos las etiquetas si seleccionó alguna
            etiquetas_seleccionadas = request.POST.getlist('tags')
            if etiquetas_seleccionadas:
                nueva_tarea.tags.set(etiquetas_seleccionadas)
                
            print(f"¡Tarea '{title}' creada con éxito desde el detalle!")
        else:
            print("❌ ERROR: El título no puede estar vacío.")

        return redirect('project_detail', id=id)
    
    return redirect('project_detail', id=id)

# UPDATE
def update_project(request, id):
    proyecto = get_object_or_404(Project,id=id,user=request)
    
    
    if request.method == 'POST':
        proyecto.name = request.POST['name']
        proyecto.save()
        
        return redirect('projects')
    
    return render(request, 'project/update_project.html', {
        'project': proyecto
    })
    
    
# ZONA DE ETIQUETAS EN LA PAGINA 
def create_tag(request, project_id):
    if request.method == 'POST':
        # Aplicamos la regla del fallback (or '') para que nunca más falle con .strip()
        nombre = (request.POST.get('name')or '').strip()
        color_hex = request.POST.get('color','#007bff')
        
        if nombre:
            Tag.objects.create(
                name=nombre,
                color=color_hex
            )
            
    return redirect('project_detail', id=project_id)



def login_view(request):
    # 1. Si el usuario ya inició sesión, no tiene sentido que vea el login. Lo mandamos a los proyectos.
    if request.user.is_authenticated:
        return redirect('projects')

    # 2. Si el usuario apretó el botón de "Iniciar Sesión" (Formulario POST)
    if request.method == 'POST':
        nombre = request.POST.get('username')  # Django usa 'username' por defecto en su modelo
        contrasenia = request.POST.get('password')

        # 3. Mandamos las credenciales al "guardaespalda" de Django para ver si coinciden
        usuario_validado = authenticate(request, username=nombre, password=contrasenia)

        # 4. Si el usuario existe y la contraseña es correcta...
        if usuario_validado is not None:
            # 5. Creamos la sesión oficial en el navegador
            auth_login(request, usuario_validado)
            # 6. Lo redirigimos a la pantalla principal de proyectos
            return redirect('projects')
        else:
            # 7. Si falló, volvemos a renderizar el login pero le pasamos un mensaje de error
            return render(request, 'registration/login.html', {'error': 'Usuario o contraseña incorrectos'})

    # 8. Si entró normal por la URL (Método GET), simplemente le mostramos el formulario vacío
    return render(request, 'registration/login.html')



def logout_view(request):
    auth_logout(request)


    return redirect('login_view')





## ------ ESTADO DEL KABAN ----- ##

@csrf_exempt
def actualizar_estado_kanban(request, task_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_estado = data.get('estado') # Recibe 'pendiente' o 'completada' desde JS
            
            # Buscamos la tarea por su ID
            tarea = Task.objects.get(id=task_id)
            
            if tarea.status == nuevo_estado:
                return JsonResponse({'success': True})
            
            # 🔄 Guardamos el string exacto en el nuevo campo del modelo
            if nuevo_estado in ['pendiente', 'progreso', 'completada']:
                tarea.status = nuevo_estado
                
            
            
            # 🔄 TRADUCCIÓN: Convertimos el string del Kanban al booleano 'done' de tu modelo
            if nuevo_estado == 'completada':
                tarea.done = True
            elif nuevo_estado == 'pendiente' or nuevo_estado == 'progreso':
                tarea.done = False
                
            tarea.save() # Ahora sí impacta una columna real en SQLite y se guarda de verdad
            
            return JsonResponse({'success': True})

        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'La tarea no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
        
    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)



# Esta clase maneja todo el CRUD (Crear, Leer, Actualizar, Borrar) automáticamente
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().select_related('user','project','assigned_to') # Como "objects" ya filtra state=True, parecería que está bien... 
    serializer_class = TaskSerializer
    
    def perform_destroy(self, instance):
        instance.state = False
        instance.save()        
    
# TICKECTS
