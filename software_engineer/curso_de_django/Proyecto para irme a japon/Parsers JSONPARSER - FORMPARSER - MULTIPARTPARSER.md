### 🧠 ¿Qué es un Parser? (En criollo)

Cuando un frontend (ya sea Postman, una app de React, o el JavaScript de tu Kanban) le hace un `POST` o un `PUT` a tu API, le manda un paquete de datos puro a través de la red (un chorro de bytes).

El **Parser** es el portero del backend que recibe ese chorro de bytes, mira el tipo de contenido que trae y lo traduce a un **Diccionario de Python** (`request.data`). Si el portero no sabe cómo masticar ese tipo de datos, te rebota con un error **415 Unsupported Media Type** 

### 🏆 Los 3 Mosqueteros de DRF

Por defecto, la clase `APIView` de DRF (de la cual heredan todos los ViewSets) ya viene configurada con tres parsers integrados de fábrica 
#### 1. `JSONParser` 
- **¿Qué busca?** Contenido de tipo `application/json`.
    
- **Cuándo se usa:** Es el formato estándar de las APIs modernas. Cuando mandás texto estructurado (por ejemplo, cuando movés la tarjeta del Kanban y mandás `{"estado": "progreso"}`).
    

#### 2. `FormParser` 
- **¿Qué busca?** Contenido de tipo `application/x-www-form-urlencoded`.
    
- **Cuándo se usa:** Es el formato clásico en el que los formularios HTML de toda la vida envían los datos (un string largo estilo `nombre=Tarea1&status=pendiente`).
    

#### 3. `MultiPartParser`

- **¿Qué busca?** Contenido de tipo `multipart/form-data`.
    
- **Cuándo se usa:** **¡Este es el importante para archivos!** Si querés subir una foto de perfil, un PDF, o la imagen de una tarea, el JSON común no sirve porque no puede transportar archivos binarios eficientemente. El `MultiPartParser` abre la canilla para recibir tanto texto como archivos al mismo tiempo

### 🚨 El experimento clave del video

El pibe del video demuestra la importancia de esto haciendo algo muy loco: vacía la lista de parsers en su vista (`parser_classes = []`) y el servidor se rompe al toque tirando el error 415 

Después, hace la prueba de importar solo el `JSONParser`. Cuando intenta subir una imagen desde Postman usando `form-data`, **vuelve a fallar**, porque el `JSONParser` solo sabe leer texto plano estructurado, no entiende nada de archivos binarios . Recién cuando le agrega el `MultiPartParser`, la imagen se sube correctamente a la carpeta `media/` 