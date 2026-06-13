### 1. El Detalle de un objeto (GET con `pk`)

Para obtener la información de un solo usuario, la función de la vista debe recibir la `pk` desde la URL.

- El instructor prefiere usar un filtrado simulado en lugar de `.get()`. Utiliza `.filter(id=pk).first()` para evitar que Django lance una excepción (un error que rompa el servidor) si el usuario no existe; en su lugar, simplemente devuelve un valor vacío (`None`).
    
- Al pasar este único objeto al serializador, **no** se utiliza el parámetro `many=True`, ya que se está serializando una única instancia y no un listado.
    

### 2. Actualización de datos (Método PUT)

En el estándar REST no se utiliza el método POST para actualizar, sino el método **PUT**.

- Para actualizar un registro, el serializador recibe una combinación clave: **la instancia actual del usuario y los nuevos datos**. Se escribe de la siguiente forma: `UserSerializer(user, data=request.data)`.
    
- Al pasarle ambos parámetros, el serializador entiende de forma interna que su trabajo no es crear un registro desde cero, sino modificar la instancia existente con la nueva información que viene en `request.data`.
    
- El proceso posterior es idéntico a la creación: se ejecuta `.is_valid()`, luego `.save()` para impactar los cambios en la base de datos, y se retorna el `.data` actualizado.
    

### 3. Eliminación de datos (Método DELETE)

Para borrar un registro de la base de datos se utiliza el método HTTP **DELETE**.

- La lógica dentro de la función es directa: se busca la instancia del usuario mediante la `pk` recibida y se ejecuta el método nativo de Django `.delete()` sobre esa instancia (por ejemplo, `user.delete()`).
    
- Como el objeto ya no existe en la base de datos, no se puede serializar. En su lugar, la vista responde devolviendo un mensaje de confirmación (como un diccionario con un aviso de "eliminado").
    

### 4. Configuración en el decorador y las URLs

- **El decorador:** Para que todo esto funcione en una sola función de detalle, el decorador de la vista debe declarar explícitamente los tres métodos permitidos en su lista: `@api_view(['GET', 'PUT', 'DELETE'])`. Si falta alguno, Django REST Framework bloqueará la petición del cliente para ese método.
    
- **La URL:** En el archivo `urls.py`, la ruta debe configurarse para aceptar la variable de la clave primaria. Se define utilizando la sintaxis de Django tradicional, por ejemplo: `path('usuario/<int:pk>/', tu_vista)`.
### 5. El truco del "Update" (`PUT`) que tenés que guardarte en la cabeza 🧠

Hay una línea en el minuto `[00:08:43]` que es una joya de lógica de Django REST Framework y que aplica exactamente igual para tus clases.

Cuando vas a **actualizar** una tarea, el serializador recibe **dos cosas**:

Python

```
# La lógica del video aplicada a tu arquitectura:
serializador = UserSerializer(instance=tarea, data=request.data)
```

- **¿Cuál es la lógica acá?** * Si al serializador solo le pasás `data=`, él asume que querés **CREAR** algo nuevo.
    
    - Si le pasás `instance=` y `data=`, el serializador entiende automáticamente: _"Ah, agarro los datos viejos de esta `instance` (tarea) y los reemplazo con la nueva `data` que viene del frontend"_ `[00:08:50]`.
        

¡Esa es la magia del ORM! Con una sola línea sabe si tiene que hacer un `INSERT` o un `UPDATE` en la base de datos SQL.