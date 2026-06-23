### 1. ¿Qué es y para qué sirve un Serializer?

En Django tradicional usabas los `Forms` (formularios) para pintar código HTML en el navegador. En una API eso ya no pasa. El video explica que la tarea **única y fundamental** de un serializador es tomar la estructura de un modelo (los datos que están en tu base de datos) y **convertirla a un formato JSON**  JSON es el lenguaje universal que entienden las aplicaciones móviles, páginas en React, Angular, etc.

### 2. Creación de un `ModelSerializer`

En el video se crea el primer serializador utilizando `ModelSerializer`  Heredar de esta clase es genial porque te ahorra escribir mucho código si ya tienes un modelo de Django preexistente.

La estructura básica que se muestra es:

Python

```
from rest_framework import serializers
from .models import Usuario # Tu modelo de Django

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' # Trae todos los campos del modelo
```

- **La convención:** Se recomienda bautizarlo usando el nombre del modelo seguido de la palabra `Serializer` (ej: `UserSerializer`) 
    
- **`class Meta`:** Aquí le dices a DRF en qué modelo basarse (`model = Usuario`) y qué campos transformar. Al poner `fields = '__all__'`, le indicas que meta absolutamente todas las columnas de la tabla en el JSON 
    
- **Diferencia clave:** A diferencia de los formularios de Django, aquí **no** existen atributos como `labels` o `widgets` , porque el serializador no dibuja interfaces visuales, solo procesa datos crudos.
    

### 3. El truco del parámetro `many=True`

Este es uno de los errores más comunes cuando se está aprendiendo. Cuando invocas al serializador en tu vista, debes pasarle los datos de la base de datos 
- Si tu consulta (`QuerySet`) trae **una lista de varios usuarios** (por ejemplo, usando `Usuario.objects.all()`), DRF se va a romper si no le avisas.
    
- Para solucionar esto, el video destaca que debes agregar obligatoriamente el parámetro **`many=True`** De esta forma, el serializador entiende que no va a procesar una sola fila, sino un listado completo, encargándose de iterar y convertir cada registro a JSON 
    

Python

```
# Ejemplo en la vista:
usuarios = Usuario.objects.all()
serializer = UserSerializer(usuarios, many=True) # <--- Aquí se usa many=True
```

### 4. ¿Cómo extraer los datos listos? El atributo `.data`

Una vez que le pasas los datos al serializador, no puedes simplemente retornar el objeto `serializer` directamente en la respuesta de tu API

El video explica que la información ya convertida y formateada en JSON no es la variable en sí, sino que se almacena dentro de un atributo especial llamado **`.data`** . Por lo tanto, cuando construyes tu respuesta (`Response`), debes pasarle `serializer.data` 

Python

```
return Response(serializer.data)
```

### 5. El resultado final en el navegador

Al final del video se muestra cómo DRF te regala una interfaz web (la _Browsable API_) para hacer pruebas . Sin embargo, el instructor aclara que cuando un cliente real (como una app mobile) consuma esa ruta, no verá los botones ni el diseño visual; lo que recibirá de forma pura y directa es un formato **`application/json`**  es decir, texto organizado en estructuras de clave-valor (`"nombre": "Juan"`) 

### 6. El Serializer NO siempre necesita un Modelo 🧠

Vos venías usando `serializers.ModelSerializer` (que se conecta a tu tabla de tareas o proyectos). Pero el video te enseña que existe el `serializers.Serializer` puro. 

- **Por qué te sirve saberlo:** En una empresa, a veces necesitás un serializador para recibir datos que **no se guardan en la base de datos**. Por ejemplo, un formulario de "Contacto" (donde el usuario manda nombre, email y mensaje para que le llegue un mail al dueño de la empresa), o un formulario de "Cambio de contraseña". Saber que podés usar serializadores sueltos para validar datos puros te abre la cabeza.
    

### 7. El "Ciclo de Vida" de `.is_valid()` (¡Esto es oro puro!) 🔄

¿Te acordás de que en tu código pusiste `if serializador.is_valid():`? Este video te explica detalladamente qué pasa tras bambalinas en Python cuando se ejecuta esa línea: 
Tiene un **orden de ejecución estricto** que Django REST Framework respeta a rajatabla: ``

1. **Validación de Tipo:** Primero se fija si pusiste texto en un `CharField` o un correo real en un `EmailField`. ``
    
2. **Validación por Campo (`validate_nombre_campo`):** Busca si creaste una función específica para ese atributo (¡Justo como la función `validate_title` que aprendiste a armar en el Ticket #01! ⭐). ``
    
3. **Validación General (`validate`):** Si todo lo anterior pasó, ejecuta un método general llamado `validate` donde podés comparar campos entre sí (por ejemplo, chequear si `password` y `confirm_password` son iguales). ``
    

### 8. La regla estricta del `return value` ⚠️

En el minuto ``, al profesor le explota el servidor y le tira un error en la pantalla. ¿Por qué? Porque se olvidó de poner el `return` en sus funciones de validación.

- **Por qué te sirve:** Grabatelo a fuego porque es el error número uno cuando uno arranca: **Toda función de validación que crees en un serializador tiene que terminar sí o sí devolviendo el valor o los datos limpios (`return value` o `return data`)**.  Si no lo ponés, Django asume que el dato se convirtió en `None` y te rompe el guardado.
    

### 💡 Mi consejo para este video:

**No copies su código** de `UserSerializer` de prueba porque te va a desacomodar el proyecto real que ya tenés armado e impecable.

**Miralo como si fuera una clase de universidad:** Concentrate en entender el flujo de cómo viajan los datos del JSON al serializador, cómo se ejecutan los filtros de validación y cómo se retorna la información limpia. `[00:13:35]` Esto te va a dar el marco teórico perfecto para cuando tengamos que armar validaciones más complejas en tus tareas.

### 9. El viaje desde `.save()` hasta el método `create`

Cuando en tu vista llamás a `serializer.save()`, los datos no impactan de forma mágica ni directa en la base de datos.

- El método `.save()` actúa como un puente que llama internamente a una función propia del serializador llamada **`create()`**.
    
- El objetivo principal de `create()` es tomar los datos, construir el nuevo objeto y registrarlo en la base de datos a través del ORM de Django.
    

### 10. El parámetro `validated_data`

El método `create(self, validated_data)` recibe obligatoriamente un argumento llamado **`validated_data`**.

- Este parámetro es un diccionario de Python que contiene la información limpia y purificada que el cliente mandó.
    
- Se llama así porque antes de que `create()` empiece a correr, el serializador ya ejecutó con éxito el método `.is_valid()`, asegurándose de que los datos cumplan con todas las reglas de negocio y restricciones del modelo.
    

### 11. La obligación de retornar una instancia

Una regla estricta del método `create()` dentro de un serializador es que **debe retornar obligatoriamente la instancia del objeto que se acaba de crear**.

- Si modificas o sobreescribis este método y te olvidas de poner el `return` con el objeto (o devolves algo vacío), Django REST Framework lanzará un error indicando que la función no está retornando una instancia de objeto válida.
    
- Al retornar la instancia correctamente, esa información vuelve a viajar hacia la vista, permitiéndote guardarla en una variable o acceder a campos automáticos como el `id`.
    

### 12. ¿Cómo lo hace de forma manual vs de forma automática?

El video muestra la diferencia entre lo que hace DRF de forma nativa y cómo lo escribirías vos a mano si necesitaras personalizar la creación:

- **Escribiéndolo de forma explícita (a mano):** Usas el ORM tradicional de Django pasando el diccionario desempaquetado con los dos asteriscos :
    
    Python
    
    ```
    def create(self, validated_data):
        return Usuario.objects.create(**validated_data)
    ```


# Metodo update en serializer

### 13. El detonante del método `update`

Cuando en tu vista ejecutas `serializer.save()`, Django REST Framework (DRF) decide qué hacer dependiendo de los parámetros que le pasaste al inicializar el serializador:

- Si **solo** le pasaste la data (`Serializer(data=request.data)`), `.save()` llamará internamente al método `create()`.
    
- Si le pasaste **tanto una instancia existente como la nueva data** (`Serializer(instance, data=request.data)`), el método `.save()` detecta inteligentemente que se trata de una edición y llama internamente al método **`update()`**.
    

### 14. Los parámetros de `update`

El método tiene la estructura `update(self, instance, validated_data)` y recibe dos herramientas esenciales:

- **`instance`**: Es el objeto original de la base de datos que recuperaste (el usuario que vas a modificar).
    
- **`validated_data`**: Es el diccionario con los nuevos datos limpios que envió el cliente y que ya superaron con éxito la validación de `.is_valid()`.
    

### 15. ¿Cómo funciona la asignación por detrás?

El video detalla que, de forma automática, un `ModelSerializer` realiza un bucle interno. Toma cada campo definido en la configuración y reasigna los valores del objeto utilizando un método `.get()` del diccionario para evitar errores si algún dato no fue enviado:

Python

```
# Lo que hace DRF de manera interna para actualizar campo por campo:
instance.name = validated_data.get('name', instance.name)
instance.email = validated_data.get('email', instance.email)
instance.save() # Guarda los cambios del modelo en la base de datos
return instance # Retorna la instancia modificada
```

Al igual que en la creación, el método `update()` **debe retornar obligatoriamente la instancia actualizada**. Si no lo hace, DRF lanzará un error.

### 16. Compartir o separar validaciones

Un punto arquitectónico muy importante que menciona el instructor es el comportamiento de las validaciones:

- Las validaciones generales que escribas en el cuerpo del serializador se van a ejecutar **tanto para crear como para actualizar**.
    
- Si necesitas que una regla solo aplique al momento de registrarse (y no al editar), o viceversa, lo ideal es escribir esa lógica directamente dentro del método `create()` o del método `update()`.
    
- Como alternativa para proyectos grandes y escalables, se recomienda separar las aguas: crear un serializador exclusivo para la creación (ej. `UserCreateSerializer`) y otro para la actualización (ej. `UserUpdateSerializer`).

# Metodo save en un serializer
### 1. El método `.save()` del Serializador (En la Vista)

Cuando en tu archivo `views.py` escribís `serializer.save()`, estás llamando al método `.save()` perteneciente a la clase del **serializador**.

- **Su función principal:** No guarda directamente en la base de datos. Su trabajo es actuar como un "director de orquesta". Revisa internamente si la operación es una creación o una actualización.
    
- **El flujo interno:** Si detecta que es una creación, delega el trabajo llamando al método `create()`. Si detecta que es una actualización, delega llamando al método `update()`.
    
- Si decidís sobrescribir el método `.save()` en tu serializador (es decir, definís un `def save(self):`), vas a **interrumpir y cortar la secuencia automática** de DRF. El instructor muestra que, si lo haces y dejas el método vacío o solo con un `print`, los datos jamás se guardarán en la base de datos porque bloqueaste el llamado automático a `create()` o `update()`.
    

### 2. Casos de uso para sobrescribir el `.save()` del Serializador

¿Por qué alguien querría romper este flujo? El video menciona casos de uso muy prácticos donde necesitás usar un serializador para validar datos, pero **no querés registrar un modelo en la base de datos**:

- **Formularios de contacto:** Querés validar que el email y el mensaje del usuario sean correctos usando la potencia del serializador, pero en lugar de guardarlo en una base de datos, querés usar la función `send_mail()` de Django para enviarte esa información directamente a tu correo electrónico personal.
    
- **Enviar correos de bienvenida:** Cuando alguien se suscribe, capturás los datos en `validated_data` para gatillar acciones externas antes o en lugar del guardado tradicional.
    
- **Guardado multi-modelo:** Si un solo JSON enviado por el cliente contiene datos que deben repartirse y guardarse en dos o tres tablas de bases de datos distintas manualmente.
    

### 3. El método `.save()` del Modelo (En el Update/Create o en `models.py`)

Por otro lado, cuando estás dentro del método `update()` de tu serializador y escribís `instance.save()`, ese `.save()` ya **no pertenece al serializador, sino al modelo de Django**.

- **Su función principal:** Es el método nativo de Django de toda la vida que interactúa directamente con el ORM para realizar la consulta SQL (`INSERT` o `UPDATE`) en la base de datos.
    
- Al sobrescribir este método en tu archivo `models.py` (`def save(self, *args, kwargs):`), podés interceptar el objeto justo antes de que toque la base de datos. Es el lugar ideal para lógicas que deben ocurrir siempre, independientemente de la API, como por ejemplo, formatear un texto, calcular un campo automático, o encriptar una contraseña antes de ser almacenada.


# To representation en un serializer
### 1. El problema de usar un solo Serializador para todo

Por defecto, cuando usás un `ModelSerializer` y definís los campos en `fields = '__all__'`, Django REST Framework (DRF) espera que todas las operaciones (Crear, Editar y Listar) manejen exactamente los mismos campos.

- Si intentás optimizar una consulta `GET` en la vista usando `.values('id', 'username')` para traer solo esos datos desde la base de datos, el serializador fallará lanzando un error (como un `KeyError` por la contraseña), porque al hacer el listado buscará _todos_ los campos declarados en el modelo y no los encontrará.
    
- **Soluciones:** Podés crear serializadores separados (uno para leer y otro para escribir), o bien interceptar el proceso de lectura en el mismo serializador usando `to_representation`.
    

### 2. El método `to_representation`

Este método se ejecuta de forma automática **únicamente cuando se leen datos (`GET`)** para representar la información de la base de datos en el JSON de salida.

- Tiene la estructura `to_representation(self, instance)`.
    
- Su objetivo principal es tomar cada instancia que devuelve la base de datos y transformarla en el diccionario final que va a recibir el frontend.
    
- Al modificar este método, **no afectás en absoluto** los procesos de creación (`POST`) o actualización (`PUT/PATCH`), ya que estos usan lógicas internas diferentes (`create` y `update`).
    

### 3. Personalización y enmascaramiento de campos (Alias)

Una de las grandes ventajas de `to_representation` es que te permite cambiar los nombres de las claves del JSON final sin tocar el modelo de la base de datos. Podés traducir campos o darles nombres más claros:

Python

```
def to_representation(self, instance):
    return {
        'id': instance['id'],
        'nombre_usuario': instance['username'], # Cambias 'username' por 'nombre_usuario'
        'correo_electronico': instance['email']
    }
```

### 4. Cuidado con el tipo de consulta: ¿Diccionario u Objeto?

El instructor hace mucho énfasis en un detalle del ORM de Django que te puede ahorrar dolores de cabeza con los errores de código:

- **Si tu consulta usa `.values()`:** Django devuelve las instancias en forma de **diccionarios de Python**. Por lo tanto, dentro de `to_representation`, debés acceder a los datos usando corchetes: `instance['username']`.
    
- **Si tu consulta usa `.all()` o `.filter()` estándar:** Django devuelve las instancias como **objetos del modelo**. En este caso, debés acceder a los datos usando la nomenclatura de punto: `instance.username`. Si usás corchetes con un objeto, el código romperá tirando un error de tipo `TypeError`.


#  ENCRIPTAR contraseña en un SERIALIZER

### 1. Separación de Serializadores

El instructor decide aplicar una excelente práctica de diseño para organizar el código y prevenir conflictos con campos requeridos de lectura/escritura:

- Crea un serializador exclusivo para listar datos: `UserListSerializer`.
    
- Mantiene un serializador especializado para la creación y edición: `UserSerializer`.
    

### 2. Encriptación en la Creación (Método `create`)

Por defecto, si pasas una contraseña directa al ORM desde el serializador, Django la guardará tal cual la escribió el usuario (en texto plano), lo cual es un fallo de seguridad grave. Para solucionarlo, se sobrescribe el método `create`:

- Se extraen los datos limpios de `validated_data`.
    
- Se crea una instancia del modelo `User` pasándole esos datos.
    
- Se utiliza el método nativo de Django **`user.set_password(password)`**. Este método se encarga de tomar el texto plano y aplicar el algoritmo de encriptación (hashing) por defecto de Django (ej. PBKDF2).
    
- Finalmente, se ejecuta `user.save()` y se retorna la instancia.
    

Python

```
def create(self, validated_data):
    # Creamos la instancia con los datos correspondientes
    user = User(**validated_data)
    # Encriptamos la contraseña usando set_password
    user.set_password(validated_data['password'])
    user.save()
    return user
```

### 3. Encriptación en la Actualización (Método `update`)

Cuando un usuario actualiza su perfil o cambia su contraseña a través de una petición `PUT`, también es necesario encriptar el nuevo valor. Para no escribir código repetitivo campo por campo, el instructor utiliza una técnica muy elegante aprovechando la herencia:

- Llama al método `update` original de la clase padre mediante **`super().update(instance, validated_data)`**. Esto actualiza automáticamente todos los campos comunes (nombre, email, etc.) en la instancia y nos devuelve el objeto actualizado.
    
- Inmediatamente después, toma esa instancia modificada y le vuelve a aplicar el método `set_password()` usando la nueva contraseña que viene en `validated_data`.
    
- Ejecuta `.save()` para confirmar los cambios en la base de datos y retorna el objeto.