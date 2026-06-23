from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Task, User  # Asumiendo que tu modelo se llama Task
from .serializers import TaskSerializer,UserSerializer 


class TaskListAPIView(APIView):
    # 🔍 GET: Trae todas las tareas de la base de datos
    def get(self,request):

        # Usamos select_related como aprendiste para que no sea pesado 🚀
        
        tareas = Task.objects.all().select_related('project','user','assigned_to')  
        # Pasamos many=True porque 'tareas' es una lista de objetos: "Che, te voy a pasar una lista con muchos objetos, tratalos uno por uno y armame una lista de JSONs".


        serializador = TaskSerializer(tareas, many=True)
        
        return Response(serializador.data, status=status.HTTP_200_OK)
    

    # 📥 POST: Recibe datos en JSON desde el frontend y crea una tarea nueva
    def post(self,request):
        # request.data agarra el JSON que mande el cliente automáticamente 🔒
        serializador = Taskerializer(data=request.data)
        # Validamos si los datos cumplen con las reglas del modelo (ej: títulos no vacíos)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        # Si los datos estaban mal (ej: faltó un campo obligatorio), responde los errores
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)\
            
            
# =====================================================================
# 2. VISTA PARA MANEJAR UNA TAREA ESPECÍFICA (Sí pide el ID en la URL)
# =====================================================================
class TaskDetailAPIView(APIView):
    # 👁️ GET: Trae el detalle de una sola tarea usando su ID
    def get(self, request, pk):
        tarea = get_object_or_404(Task,id=pk)
        serializador = TaskSerializer(tarea)# Sin many=True porque es una sola Osea que cuando son mas de una lista el many true los convierte en unos objetos
        return Response(serializador.data, status=status.HTTP_200_OK)
    
        # 📝 PUT: Modifica o actualiza los datos de una tarea existente
    def put(self, request, pk):
        tarea = get_object_or_404(Task,id=pk)
        # Le pasamos la tarea actual y los datos nuevos que vienen en el JSON
        serializador = TaskSerializer(tarea, data=request.data)
        
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_200_OK) 
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
        # ❌ DELETE: Borra la tarea de la base de datos de forma SEGURA
    def delete(self, request, pk):
        # 1. Traemos la tarea que quieren borrar usando el ID (pk) de la URL
        tarea = get_object_or_404(Task, id=pk)
        
        # 2. 🛡️ ¡EL IF DE SEGURIDAD! (Tu lógica en acción)
        # Comparamos: ¿El dueño de la tarea (tarea.user) es DISTINTO (!=) al usuario logueado (request.user)?
        if tarea.user != request.user:
            # Si no es el dueño, le frenamos el carro con un estado 403 Forbidden (Prohibido)
            return Response(
                {"error": "¡Ey! No podés borrar una tarea que no es tuya."}, 
                status=status.HTTP_403_FORBIDDEN
            )
            
        # 3. Si el "if" no se cumple, significa que SÍ es el dueño. Procedemos al borrado:
        tarea.delete()
        return Response({'message':'Tarea eliminada correctamente'}, status=status.HTTP_200_OK)