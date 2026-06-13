### 1. El problema de los errores "Huérfanos" (Non-Field Errors) 👤❌

En el video, el profesor muestra que cuando tirás un error dentro del método general `validate` (como el `if titulo == descripcion:` que hicimos recién), Django REST Framework genera un error global.

En la pantalla del programador frontend, el JSON llega así:

JSON

```
{
    "non_field_errors": ["El email no puede contener el nombre"]
}
```

- **¿Cuál es el problema real en el laburo?** El Frontend automatiza las pantallas. Si el error viene con la clave `"title"`, el Frontend sabe que tiene que pintar el cuadrito del título con un borde rojo y poner el cartelito abajo de ese cuadrito.
    
- Si el error viene como `"non_field_errors"`, el error queda "huérfano". El Frontend no sabe a qué cuadrito de la pantalla pertenece y tiene que inventar un cartel flotante arriba de todo. Eso arruina la experiencia del usuario.
    

### 2. La solución Pro: Validar con `context` asignando el error a un campo 🛡️

Para solucionar esto, el youtuber muestra un truco avanzado en el minuto . En vez de meter la comparación cruzada en el `validate` general, la mete **adentro de la validación de un campo específico** (por ejemplo, en `validate_email` o en tu caso, en `validate_description`), sacando los otros datos a través de `self.context` o llamando a los otros métodos de validación 

Al hacer eso, el error se asocia **directamente a un campo**. El JSON pasa a verse así:

JSON

```
{
    "description": ["¡Che! No podés poner el mismo título en la descripción."]
}
```

¡Ahora el Frontend sí sabe exactamente dónde mostrar el error!

### 🛠️ Refactorizando tu código con la lógica de este video

¿Te acordás de que en el último mensaje te dije que el código se podía mejorar (refactorizar) una vez que funcionaba? Vamos a aplicar la técnica de este video a tu serializador de tareas para que veas cómo se escribe a nivel profesional:

En lugar de usar el método `validate(self, data)` general, metemos el control cruzado **adentro del guardián de la descripción**, haciendo que valide su propio string y use la lógica cruzada de forma limpia.

Mirá cómo queda:

Python

```
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'done', 'project', 'user']

    # 1. Validador individual del título
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El título debe tener más de 5 caracteres.")
        return value

    # 2. 🚀 VALIDACIÓN PRO (Lógica del video): Cruzada pero asignada al campo 'description'
    def validate_description(self, value):
        # 'value' aquí es el texto de la descripción que mandó el usuario
        
        # Accedemos al diccionario de datos iniciales que mandó el frontend para pescar el título
        # 'initial_data' es una herramienta nativa de DRF para ver el JSON crudo
        titulo = self.initial_data.get('title')
        
        # Comparamos el título que pescamos con el valor de la descripción
        if value == titulo:
            # Al lanzarlo acá, DRF automáticamente sabe que el error pertenece a "description" 👏
            raise serializers.ValidationError("¡Che! La descripción no puede ser idéntica al título.")
            
        return value
```

### 📊 Conclusión: La capa del Serializador

Hacia el final del video (`[00:14:50]`), el profesor dice una frase que es la biblia del Backend:

> _"Las validaciones de los datos no se hacen en la Vista; se hacen en el Serializador. La Vista no tiene por qué llenarse de código feo tratando la información; la Vista solo recibe la información ya limpia y tratada por el serializador"_ 