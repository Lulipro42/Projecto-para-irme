Una **API REST** (Interfaz de Programación de Aplicaciones que sigue el estilo de arquitectura REST) es un conjunto de reglas que permite que dos sistemas de software se comuniquen entre sí a través de internet de forma sencilla, rápida y estandarizada

Actúa como un "traductor" o "mensajero" para que una aplicación solicite y reciba información de otra, sin importar el lenguaje de programación en el que estén construidas

y esto es el codigo 

## 🛠️ Paso 1: El Traductor (`myapp/serializers.py`)

Este archivo lo creamos recién. Su única función en la vida es agarrar la información cruda que sale de tu base de datos SQLite (que son objetos de Python que la web no entiende) y traducirlos a ese texto con llaves llamado **JSON**.

Abrí tu archivo `serializers.py` y miralo mientras te lo explico línea por línea:

Python

```
from rest_framework import serializers
from .models import Task  # [1] Importamos tu plano de la base de datos

# [2] Creamos el traductor automático para el modelo Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # [3] Le decimos qué modelo tiene que traducir
        # [4] Elegimos qué columnas de la base de datos queremos que viajen por internet
        fields = ['id', 'title', 'description', 'status', 'done', 'project', 'user']
```

- **`serializers.ModelSerializer` [2]:** Es una herramienta espectacular de Django REST Framework. En vez de tener que programar a mano la traducción de cada campo, esta clase mira tu modelo `Task`, ve qué tipos de datos tiene (texto, números, booleanos) y aprende a traducirlos sola.
    
- **`fields` [4]:** Acá vos tenés el control total como Ingeniero de Software. Si tu tabla tuviera un campo secreto (como una contraseña o un dato interno), simplemente lo sacás de esta lista y nunca va a viajar hacia la API. En este caso, elegimos que se muestre todo (el id, el título, si está hecha, el proyecto y el usuario).
    

## 🚦 Paso 2: El Cerebro de la Operación (`myapp/views.py`)

En el Django tradicional, la vista se encargaba de buscar los datos y mezclarlos con un archivo HTML. Acá, en el mundo de las APIs, la vista es el **mozo** de la analogía de MiduDev. Recibe la petición del cliente, le pide al traductor (el serializer) que empaquete los datos y los despacha.

Mirá cómo quedó tu `views.py`:

Python

```
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# [1] El "Super-Mozo" que hace todo el trabajo pesado
class TaskViewSet(viewsets.ModelViewSet):
    # [2] Qué datos vamos a buscar (¡Todas las tareas!)
    queryset = Task.objects.all() 
    
    # [3] Qué traductor vamos a usar para empaquetar estos datos
    serializer_class = TaskSerializer 
```

- **`viewsets.ModelViewSet` [1]:** Esto es magia pura de DRF. Al heredar de acá, Django automáticamente te crea la lógica para **las 5 operaciones del CRUD**:
    
    1. Si entran pidiendo la lista completa, hace un `.all()` (`GET`).
        
    2. Si entran mandando datos nuevos, crea una tarea (`POST`).
        
    3. Si piden una sola tarea por su ID, la busca (`GET` individual).
        
    4. Si mandan datos para editar, la actualiza (`PUT` / `PATCH`).
        
    5. Si piden borrarla, la elimina de la base de datos (`DELETE`). _¡Y todo eso lo ganás escribiendo solo 3 líneas de código!_
        

## 🗺️ Paso 3: Las Puertas de Entrada (`mysite/urls.py`)

Ya tenemos el traductor y el cerebro que maneja los datos. Ahora nos falta poner los carteles en la calle para que el navegador sepa a dónde tiene que ir a golpear la puerta. De eso se encargan las URLs.

Abrí tu `urls.py` principal (el que está en la carpeta del proyecto `mysite`):

Python

```
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp import views

# [1] Creamos un enrutador automático
router = routers.DefaultRouter()

# [2] Registramos nuestro cerebro de tareas bajo la palabra 'tasks'
router.register(r'tasks', views.TaskViewSet, 'tasks') 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # [3] Conectamos el enrutador bajo el prefijo 'api/'
    path('api/', include(router.urls)),
]
```

- **`routers.DefaultRouter()` [1]:** Como el `ModelViewSet` de las vistas hace 5 cosas distintas, crear las URLs a mano para cada una sería un dolor de cabeza. El `router` se encarga de crear todas las combinaciones de URLs por vos tras bambalinas.
    
- **`path('api/', ...)` [3]:** Esto significa que todas las rutas automáticas del router van a empezar con `/api/`. Por eso, para ver tus tareas, la dirección final se convirtió en `[http://127.0.0.1:8000/api/tasks/](http://127.0.0.1:8000/api/tasks/)`.
    

## 🕵️ El flujo completo: Qué pasa cuando apretás Enter en el navegador

Para que cierres el circuito de manera perfecta, este es el viaje que hace la información en milisegundos cuando entrás a la "página de código":

Plaintext

```
Tu Navegador (Petición GET) 
       │
       ▼
   urls.py ──► Dice: "Ah, vas para /api/tasks/, te toca ir a las vistas".
       │
       ▼
   views.py ──► Dice: "Soy un ViewSet, voy a buscar las Tasks usando el ORM".
       │
       ▼
Base de Datos ──► Devuelve las filas de la tabla de tareas a la vista.
       │
       ▼
serializers.py ──► La vista le pasa las tareas al Serializer, que las convierte en JSON.
       │
       ▼
Tu Navegador (Respuesta) ──► Recibe el JSON limpio y te lo muestra en pantalla.
```