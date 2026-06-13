from rest_framework import serializers
from .models import Task, User # [1] Importamos tu plano de la base de datos

# [2] Creamos el traductor automático para el modelo Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # [3] Le decimos qué modelo tiene que traducir
        # [4] Elegimos qué columnas de la base de datos queremos que viajen por internet
        fields = ['id', 'title', 'description', 'status', 'done', 'project', 'user', 'state']
            

    def validate_title(self,value):
        
        # 1. Aplicamos el blindaje para limpiar espacios fantasmas
        titulo_limpio = (value or '').strip()
        
        # 2. Regla de negocio: No puede estar vacío
        if not titulo_limpio:
            raise serializers.ValidationError("Tu mensaje da error")
        # 3. Regla de negocio avanzada: Evitar títulos basura (mínimo 3 caracteres)
        if len(titulo_limpio) < 3:
            raise serializers.ValidationError("Dale un nombre a tu titulo de la tarea")
        # 4. CRUCIAL: Siempre tenés que devolver el valor limpio para que se guarde en la BD
        return titulo_limpio
        
        
        
    def validate_status(self,value): # Aca bueno hice como antes cree la varialble def o no me acuerdo como se decia 
        status_limpio = (value or '').strip() # Aca hice como antes limpio los espacios vacios 
        

        estado_status = ['pendiente','progreso','completada']# Aca hice lo que pude captar
        
        if status_limpio not in estado_status:
            raise serializers.ValidationError("El estado enviado no es válido.")
    
        return status_limpio 
    
    def to_representation(self,instance):
        # 1. Dejamos que DRF arme el JSON básico con los IDs (el comportamiento por defecto)
        data = super().to_representation(instance)
        
        # 2. Reemplazamos el ID del usuario por su nombre real (o lo que necesites)
        # Usamos un "if" por las dudas de que la tarea no tenga usuario asignado (evita que explote en Null)
        if instance.user:
            data['user'] = instance.user.username # En vez del ID, el frontend recibe el string del username
        else:
            data['user'] = "sin asignar"
            
        # 3. Hacemos lo mismo con el proyecto si el frontend necesita su nombre
        if instance.project:
            data['project'] = instance.project.name # Cambialo por el campo real que tenga tu modelo Project (name, title, etc.)
        else:
            data['project'] = "Sin proyecto"

        # 4. Devolvemos el JSON transformado
        return data
            
# CREAMOS UN SERIALIZER PARA LOS USUARIOS
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
            
        fields = ['id','username','email']
        


