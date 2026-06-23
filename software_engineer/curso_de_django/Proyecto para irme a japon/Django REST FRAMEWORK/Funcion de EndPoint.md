### 🌐 Bienvenidos a Django REST Framework (DRF)

Como ya viste la teoría de los videos, sabés que en lugar de renderizar plantillas HTML (`render(request, 'template.html')`), nuestro objetivo ahora es exponer **endpoints** (URLs) que devuelvan datos puros en formato **JSON**. Esto va a permitir que en el futuro cualquier frontend (como React, Angular o una app móvil) se conecte a tu sistema.

Para entender la diferencia de flujo entre lo que venías haciendo y lo que vas a hacer ahora con DRF, mirá este mapa mental de arquitectura:

- **Antes:** El cliente pedía una URL ➡️ Django procesaba la vista ➡️ Mezclaba datos con HTML ➡️ Devolvía una página web armada.
    
- **Ahora (DRF):** El cliente pide una URL (Endpoint) ➡️ DRF procesa la vista ➡️ El Serializador transforma los modelos a **JSON** ➡️ Devolvía texto plano estructurado.
    

### 🎟️ TICKET API-01: Tu Primer Endpoint Completo (TaskViewSet)

Vamos a revisar la clase que ya tenías declarada al final de tu `views.py` para entender el poder de lo que escribiste:

Python

```
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() # Trae todas las tareas activas
    serializer_class = TaskSerializer
    
    def perform_destroy(self, instance):
        instance.state = False
        instance.save()        
```

#### 🔍 El ojo clínico del Senior: ¿Qué hace este bloque de código?

Al heredar de **`viewsets.ModelViewSet`**, Django REST Framework hace magia negra por detrás. En lugar de escribir 5 funciones separadas (`listar_tareas`, `crear_tarea`, `ver_tarea`, `editar_tarea`, `borrar_tarea`), esta sola clase te regala **el CRUD completo** adaptándose a los métodos HTTP automáticamente:

- **`GET /api/tasks/`** ➡️ Llama automáticamente a listar todas las tareas.
    
- **`POST /api/tasks/`** ➡️ Lee el JSON que te mandan, lo valida con tu `TaskSerializer` y crea la tarea en SQLite.
    
- **`GET /api/tasks/<id>/`** ➡️ Devuelve el JSON de una sola tarea específica.
    
- **`PUT / PATCH /api/tasks/<id>/`** ➡️ Edita la tarea de forma parcial o completa.
    
- **`DELETE /api/tasks/<id>/`** ➡️ Ejecuta tu función `perform_destroy`. ¡Y mirá qué bien que la hiciste acá! En lugar de borrarla físicamente con un `.delete()`, interceptaste el borrado para hacerle un **Soft Delete** (`instance.state = False`), manteniendo tu regla de negocio de conservar los datos desactivados. ¡10 puntos ahí!
    

### 🛠️ Tu Misión de hoy: Poner a prueba la API

Para ver si esto funciona de verdad y no quedarnos solo en la teoría, tenemos que asegurarnos de que las URLs de la API estén conectadas.

1. **Revisá tu archivo `urls.py` de la aplicación.** Tenés que tener configurado el `DefaultRouter` de Django REST Framework para que mapee tu `TaskViewSet`. Debería verse algo parecido a esto:
    

Python

```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet # O como lo tengas importado

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # ... tus rutas viejas de los proyectos y login ...
    path('api/', include(router.urls)), # Esto une el router de la API
]
```

2. **Levantá el servidor** (`python manage.py runserver`) e ingresá desde tu navegador a esta URL: 👉 `http://127.0.0.1:8000/api/tasks/`
    

### 📊 ¿Qué tenés que ver?

Si las URLs están bien puestas, DRF te va a mostrar una interfaz gráfica hermosa dentro del navegador (el _Browsable API_) donde vas a ver la lista de todas tus tareas en formato JSON y un formulario abajo para crear una nueva tarea enviando datos limpios.