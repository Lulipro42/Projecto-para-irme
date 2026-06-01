from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, 'tasks')


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('task/', views.task, name="task"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
    path('project/<int:id>/', views.project_detail, name="project_detail"),
    path('project_eliminar/<int:id>/', views.project_eliminar, name='project_eliminar'),
    path('update_task/<int:id>/', views.upadate_task, name='update_task'),
    path('task_completar/<int:id>/', views.task_completar, name="task_completar"),
    path('task_eliminar/<int:id>/', views.task_eliminar, name="task_eliminar"), 
    path('project/<int:id>/create_task/', views.recibir_id, name='recibir_id'),
    path('project_update/<int:id>/', views.update_project, name="update_project"),
    path('task/<int:task_id>/complete/', views.complete_task, name="complete_task"),
    path('task/<int:task_id>/delete/', views.delete_task, name="delete_task"),
    path("task/editar/<int:task_id>/", views.task_editar, name="task_editar"),
    path('task/<int:task_id>/note/add/', views.add_task_note, name="add_task_note"),
    path('project/<int:project_id>/tag/create/', views.create_tag, name="create_tag"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('task/actualizar-estado/<int:task_id>/', views.actualizar_estado_kanban, name="actualizar_estado_kaban"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]