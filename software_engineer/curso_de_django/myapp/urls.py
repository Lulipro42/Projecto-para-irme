from django.contrib import admin
from django.urls import path
from . import views  
from .views import ActualizarEstadoKanbanAPIView
from . import api    # Asegurate de que tu archivo api.py exista en la misma carpeta

urlpatterns = [
    # ==========================================
    # 🏠 VISTAS GENERALES Y DE PRUEBA
    # ==========================================
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),

# ==========================================
    # 📁 GESTIÓN DE PROYECTOS (CRUD)
    # ==========================================
    path('projects/', views.projects, name="projects"),
    path('create_project/', views.create_project, name="create_project"),
    path('project/<int:id>/', views.project_detail, name="project_detail"),
    path('project_update/<int:id>/', views.update_project, name="update_project"),
    path('project_eliminar/<int:id>/', views.project_eliminar, name='project_eliminar'),
    
    # 🌟 DEJA SOLO ESTA LÍNEA (conecta tu nueva vista que maneja el ID del proyecto)
    path('project/<int:id>/create_task/', views.create_task, name='create_task'),

    # ==========================================
    # 📝 GESTIÓN DE TAREAS Y NOTAS (CRUD / ESTADOS)
    # ==========================================
    # 🔥 BORRAMOS la línea repetida de 'recibir_id' que causaba el conflicto
    
    path('task/', views.task, name="task"),
    path('task/<int:task_id>/complete/', views.complete_task, name="complete_task"),
    path('task/<int:task_id>/delete/', views.delete_task, name="delete_task"),
    path('task/editar/<int:task_id>/', views.task_editar, name="task_editar"),
    path('task/<int:task_id>/note/add/', views.add_task_note, name="add_task_note"),
    # ==========================================
    # 🏷️ ETIQUETAS Y KANBAN ASÍNCRONO
    # ==========================================
    path('project/<int:project_id>/tag/create/', views.create_tag, name="create_tag"),
    path('api/kanban/<int:task_id>/', ActualizarEstadoKanbanAPIView.as_view(), name="actualizar_estado_kanban"),
    # ==========================================
    # 🔐 SISTEMA DE AUTENTICACIÓN
    # ==========================================
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),

    # ==========================================
    # 🤖 ADMINISTRACIÓN Y API REST (Clases Explícitas)
    # ==========================================
    path('admin/', admin.site.urls),
    
    # Removimos la línea de include(router.urls) que rompía el sistema
    path('api/tasks/', api.TaskListAPIView.as_view(), name='api_task_list'),
    path('api/tasks/<int:pk>/', api.TaskDetailAPIView.as_view(), name='api_task_detail'),
]