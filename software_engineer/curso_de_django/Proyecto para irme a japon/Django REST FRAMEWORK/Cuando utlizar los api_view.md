### ⚖️ El balance en el código profesional

Para que te lleves la regla de oro que se usa en los equipos de ingeniería:

- **Usás Clases (`APIView`):** Cuando manejás la lógica principal de un recurso de tu base de datos (tus Tablas, Proyectos, Usuarios) donde necesitás que convivan el listado, el detalle, la edición y el borrado de forma ordenada y escalable.
    
- **Usás Funciones (`@api_view`):** Cuando el endpoint es un "servidor de una sola acción", un proceso matemático aislado, una pasarela de pagos o una integración con otra API externa.
    

Por eso está perfecto que mantengas ese `import` arriba. En tu portfolio o en un laburo real, ver ambos enfoques aplicados en los lugares correctos demuestra que sabés elegir la herramienta adecuada para cada problema técnico.


# Registro con API_VIEWS y Serializer

### 1. Deserialización y validación automática

Anteriormente viste que el serializador transforma datos de la base de datos a JSON. Aquí se explica el proceso inverso: recibe datos crudos en JSON desde `request.data`, los "deserializa" y comprueba que cumplan con las reglas del modelo (por ejemplo, que no superen el largo máximo de caracteres o que los campos obligatorios estén presentes).

Para cargar los datos recibidos en el serializador, se los pasas usando el parámetro `data`:

Python

```
serializer = UserSerializer(data=request.data)
```

### 2. El método `.is_valid()`

Casi idéntico a cómo funcionan los formularios tradicionales de Django, debes ejecutar obligatoriamente el método `.is_valid()` antes de intentar guardar algo. Este método gatilla de forma interna todas las comprobaciones necesarias y devuelve un valor booleano (`True` o `False`).

### 3. Guardado con `.save()`

Si `.is_valid()` determina que los datos son correctos, invocas al método `.save()`. Esto se encarga de crear el nuevo registro directamente en la base de datos utilizando el modelo asociado. Una ventaja añadida es que, tras guardarse con éxito, el serializador almacena una copia en formato JSON del objeto recién creado dentro de `.data`, permitiéndote retornarlo fácilmente como respuesta de confirmación para el usuario.

### 4. Manejo de errores con `.errors`

Si la validación falla (por ejemplo, si intentas registrar un usuario con un correo o un username que ya existe y son campos únicos), el serializador no rompe el programa, sino que recolecta los fallos en la propiedad `.errors`.

Django REST Framework se encarga de estructurar automáticamente estos errores en un formato de diccionario JSON ordenado por campo, facilitando que el frontend sepa exactamente qué dato estuvo mal cargado para mostrárselo al usuario.