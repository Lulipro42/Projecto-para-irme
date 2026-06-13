### ¿Por qué esto YA cuenta como desarrollo de APIs?

Aunque lo estés manejando desde una página web, lo que pasa por detrás de escena es desarrollo backend puro y duro:

- **Ya configuraste un Endpoint:** La URL `/api/api-tasks/` es un canal de comunicación limpio.
    
- **Ya usás Serializers:** Creaste el traductor que transforma los objetos complejos de Python (`Task.objects.all()`) a texto plano estructurado (**JSON**).
    
- **Ya implementaste un ViewSet:** Usaste `viewsets.ModelViewSet`, que es una de las herramientas más potentes de DRF. Con esa sola clase, le diste soporte a tu sistema para procesar **cuatro operaciones clave de internet (CRUD)** utilizando métodos HTTP estándar:
    

|**Acción en la API**|**Método HTTP**|**¿Qué hace por detrás?**|
|---|---|---|
|**Ver la lista de tareas**|`GET`|Lee las tareas y te las muestra en JSON|
|**Darle al botón POST**|`POST`|Envía los datos del formulario para registrar una tarea nueva|
|**Editar una tarea**|`PUT` / `PATCH`|Actualiza los datos de un ID específico|
|**Borrar una tarea**|`DELETE`|Elimina el registro por completo|

### Lo que te falta para considerarte un "Experto en APIs"

Ya diste el paso más difícil, que es conectar los cables y hacer que funcione. Lo único que te falta de acá en adelante para dominar el tema por completo es:

1. **Dejar de usar la interfaz visual:** Aprender a enviarle y pedirle datos a esa misma URL usando herramientas profesionales como **Postman**, **Insomnia**, o directamente usando comandos desde una terminal.
    
2. **Personalizar la lógica:** Aprender a meterle filtros personalizados a la API (por ejemplo, que el JSON solo muestre las tareas que tengan `state=True`, ocultando los borrados lógicos que configuramos en tu `BaseModel`).