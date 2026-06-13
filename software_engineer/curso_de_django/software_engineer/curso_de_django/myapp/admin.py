from django.contrib import admin
from .models import Project, Task, TaskNote, Tag, SubTask



# Register your models here.
# 1. Configuración mágica para que las SubTasks aparezcan dentro de las Tasks
class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1  # Te deja siempre un casillero en blanco listo para escribir una sub-tarea nueva

# 2. Personalizamos el panel de Task para que use esa configuración en línea
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTaskInline]

# 3. Registramos los modelos en el orden correcto
admin.site.register(Project)
admin.site.register(Task, TaskAdmin)  # 👈 Registramos Task pasándole la personalización de las sub-tareas
admin.site.register(TaskNote)
admin.site.register(Tag)