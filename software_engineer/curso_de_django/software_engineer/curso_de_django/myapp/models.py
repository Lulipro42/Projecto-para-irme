from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #(Le ponemos null=True y blank=True para que los proyectos que ya tenías creados de antes no te rompan la base de datos al migrar).
    
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#6c757d')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, default='Baja')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks') # EL BLANK SIRVE PAR QUE UNA TAREA SE CREE SIN NINGUNA ETIQUTA PUESTA LA PRINCIPIO
    due_data = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #  ¡Ahora sí sabe que apunta a User!
    # 📅 Nueva fecha de vencimiento para las tareas AL PONER NULL Y BLANK DICE:si una tarea no tiene fecha asignada no pasa nada la dejamos vacia
    deadline = models.DateField(null=True, blank=True)



    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    
    
    PRIORIDAD_CHOICES = [
        ('Baja', '🟢 Baja'),
        ('Media', '🟡 Media'),
        ('Alta', '🔴 Alta'),
    ]
    
    priority = models.CharField(
        max_length=10,
        choices=PRIORIDAD_CHOICES,
        default='Baja'
    )
    
    ESTADO_CHOICES = [
        ('pendiente','⏳ Pendiente'),
        ('progreso', '🔄 En Progreso'),
        ('completada', '✅ Completada'),
    ]
    
    status = models.CharField(
        max_length=15,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )
    
    def __str__(self):
        return self.title + '-' + self.project.name
    


class TaskNote(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notes')    
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Nota para {self.task.title}: {self.text[:20]}..."


class SubTask(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='subtasks'
    )
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} ({'✅' if self.is_completed else '🔲'})"