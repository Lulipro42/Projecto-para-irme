from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer

class TaskService:
    @staticmethod
    def update_user_task(task_id, user, data):
        # La seguridad y la optimizacion se manejan aca 
        tarea = get_object_or_404(Task,id=task_id,user=user)
        
        # Aplicamos el .copy() que te faltaba sumar 💎
        datos_mutables = data.copy()
        
        if datos_mutables.get('description') == 'null':
            datos_mutables['description'] = ""
            
        serializer = TaskSerializer(tarea, data=datos_mutables)
        
        if serializer.is_valid():
            serializer.save()
            return {"succes": True, "data": serializer.data}
        
        return {"success": False, "errors": serializer.errors}
    
### -------- TICKETS ------ ###
