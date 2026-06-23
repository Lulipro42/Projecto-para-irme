### 1. El gran cambio: `request.data` y `request.query_params` 

En Django normal usabas `request.POST` o `request.FILES`. En **Django REST Framework eso cambia por completo**:

- **`request.data`:** Olvidate de `request.POST`. Ahora, absolutamente **toda** la información que envíe el cliente (un JSON, un formulario, un texto o incluso archivos e imágenes) se unifica y se recibe dentro de `request.data` . DRF procesa el contenido automáticamente por detrás.
    
- **`request.query_params`:** El clásico `request.GET` (para capturar parámetros de la URL como búsquedas o filtros `?search=python`) deja de usarse. Ahora se accede mediante `request.query_params`

### 2. La negociación de contenido y `response` 

A diferencia de Django común donde devolvías un HTML renderizado, en DRF siempre vas a devolver datos puros.

- **`Response(data, status)`:** Es la clase nativa de DRF para responderle al cliente . Por lo general, solo le pasás dos cosas: los datos ya serializados (`data`) y el código de estado HTTP (`status`) .
    
- **Proceso de Negociación:** Cuando entra una petición, DRF negocia automáticamente con el frontend. Sabe que es una API REST, por lo que casi siempre define el tipo de contenido como `application/json` y procesa todo para escupir un JSON limpio .

### 3. El nuevo flujo de trabajo (Los 4 pasos de DRF) 

En Django normal hacías: _Modelo ➡️ Formulario ➡️ Vista ➡️ Template (HTML)_. En **Django REST Framework los formularios y los templates desaparecen** . El nuevo flujo es:

1. **Modelo:** Tu base de datos de Django de toda la vida .
    
2. **Serializador (Serializer):** Reemplaza a los formularios. Su única función es agarrar los datos del modelo (código Python/ORM) y convertirlos a un formato estándar como **JSON** (y viceversa al recibir datos) .
    
3. **Vista (View):** Procesa la lógica de negocio conectando el serializador con el modelo .
    
4. **Ruta (URL / Router):** Define los endpoints de acceso .
    

### 4. La filosofía de las URLs en API REST 

En Django tradicional solías crear una URL para cada acción (ej: `/tareas/crear/`, `/tareas/listar/`, `/tareas/eliminar/1/`).

En DRF las rutas se vuelven **globales y genéricas** `[00:38:32]`. La acción que ejecuta el servidor no depende del nombre de la URL, sino del **Método HTTP** con el que se le pega:

- Una petición **`GET`** a `/usuarios/` ➡️ Lista todos los usuarios .
    
- Una petición **`POST`** a `/usuarios/` ➡️ Crea un usuario nuevo 
    
- Una petición **`GET`** a `/usuarios/1/` ➡️ Trae el detalle del usuario con ID 1 
    

### 5. Códigos de Estado HTTP (Status Codes) 

El profesor hace mucho hincapié en que una API REST debe comunicarse de forma transparente usando los códigos estándar del protocolo HTTP:

- **`200 OK`:** Todo salió bien 
    
- **`201 Created`:** Ideal para cuando se crea con éxito un registro en la base de datos tras un `POST`
    
- **`400 Bad Request`:** Error del cliente (envió datos inválidos).
    
- **`404 Not Found`:** El recurso solicitado no existe `
    
- **`500 Internal Server Error`:** Errores de código o del servidor `


# RESPONSE

Response(data,status=None,template_name=None,headers=None,content_type=None)

.data: son los datos ya SERIALIZADOS que se envian como respuesta
.status: codigo HTTP de estado para la respuesta , por defecto retorna codigo HTTP_@))_OK
.template_name: plantilla a utilizar si es que se utiliza HTMLRenderer como medio de renderizado.
.contet_type: tipo de contenido de la respuesta, este tipoi es definido automaticamente cuando se trata de la peticion pero hay casso donde se debe espesificar manualmente
