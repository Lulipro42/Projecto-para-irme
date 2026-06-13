from rest_framework import serializers
from .models import Task  # [1] Importamos tu plano de la base de datos

# [2] Creamos el traductor automático para el modelo Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # [3] Le decimos qué modelo tiene que traducir
        # [4] Elegimos qué columnas de la base de datos queremos que viajen por internet
        fields = ['id', 'title', 'description', 'status', 'done', 'project', 'user']