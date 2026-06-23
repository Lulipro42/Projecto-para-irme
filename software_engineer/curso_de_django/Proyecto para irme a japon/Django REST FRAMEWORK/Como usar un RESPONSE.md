### 1. El uso explícito de los Status Codes (`HTTP_201_CREATED`, etc.)

El youtuber explica que si no le ponés un `status` a la respuesta, Django por defecto clava un `200 OK` .

- **Por qué te sirve:** En el código que armamos para tu `api.py` la semana pasada, nosotros ya incluimos esto (`status=status.HTTP_201_CREATED` o `status=status.HTTP_400_BAD_REQUEST`). El video te sirve para entender la teoría de **por qué** hicimos eso: el navegador y los Frontend usan esos números (200, 201, 400, 404) para saber si la app andó bien o explotó, y para pintarte los errores en rojo en la consola .
    

### 2. Devolver un JSON con mensajes claros (`{"message": "..."}`)

Mirá lo que hace en el minuto . Cuando elimina un usuario, en vez de devolver una pantalla vacía, devuelve un diccionario de Python (que DRF transforma en JSON) con un mensaje:

Python

```
return Response({"message": "Usuario eliminado correctamente"}, status=status.HTTP_200_OK)
```

- **Por qué te sirve:** Esto es ley en el desarrollo profesional. El programador que haga el Frontend (en React, Angular o celular) necesita que vos le mandes ese texto para él poder meter un cartel flotante lindo en la pantalla del usuario que diga _"¡Éxito! Tu tarea se borró"_.
    
- _Nota técnica:_ Nosotros en tu `api.py` usamos el estándar estricto de APIs (`status.HTTP_204_NO_CONTENT`) que no devuelve texto `[00:10:46]`. Pero si el Líder Técnico de tu empresa te pide: _"Ulises, pasame un mensaje confirmando el borrado"_, ya sabés que tenés que meter un diccionario como muestra el video.
    

### 3. La filosofía de Refactorizar (¡Esto te hace Senior!)

En el minuto `[00:00:24]`, el profesor dice algo espectacular: _"No solo importa que el código funcione. Una vez que funciona, hay que acomodarlo mejor para optimizarlo y que se vea más limpio"_.

- **Por qué te sirve:** Esto es exactamente lo que venimos haciendo con tus tickets. No te quedes con la primera solución que te tira Python. Volver al código, limpiarlo, ordenarlo en clases y estructurarlo, es lo que diferencia a un programador que copia y pega de un Ingeniero de Software.
    

### 💡 En resumen:

Miralo tranquilo. Ignorá que él usa funciones (`@api_view`) , porque vos ya estás un paso adelante usando Clases (`APIView`). Enfocate en cómo usa la consola del navegador para espiar los estados y cómo estructura los mensajes de respuesta.

Cuando termines de procesar este video, avisame y te tiro el próximo ticket para aplicar estas estructuras de respuestas y mensajes personalizados. ¡Cada video es un pasito más cerca de subirte a ese avión! 🚀✈️🇯🇵