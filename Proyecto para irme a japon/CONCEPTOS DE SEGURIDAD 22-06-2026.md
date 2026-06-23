## 🛡️ Los 3 Escudos de Seguridad Backend

### 1. El Escudo de Identidad (Seguridad a nivel de Registro)

Este lo dominaste ayer y hoy lo reforzamos. El peligro se llama **IDOR** (Insecure Direct Object Reference). Ocurre cuando un usuario malicioso intenta cambiar un número en la URL (por ejemplo, pasar de `tarea/15` a `tarea/16`) para ver o borrar los datos de otra persona.

- **El error común:** Buscar el dato solo por su identificador único: `Task.objects.get(id=task_id)`.
    
- **La solución profesional:** Forzar a la base de datos a cruzar el ID de la tarea con el usuario que tiene la sesión iniciada en ese milisegundo (`request.user`).
    

Python

```
# Django solo va a traer la tarea si el ID coincide Y si pertenece al proyecto de ese usuario logueado
tarea = get_object_or_404(Task, id=task_id, project__user=request.user)
```

Si el usuario intenta adivinar el ID de otra persona, el sistema le dice "404 Not Found" en la cara. No sabe si existe o no, pero no lo dejamos pasar.

### 2. El Escudo de Integridad (Transacciones Atómicas)

Este protege al sistema de los errores internos o caídas de conectividad. El peligro es que la base de datos quede en un estado "asincrónico" o corrupto (por ejemplo, restar el dinero de una billetera virtual pero que se caiga el sistema antes de crear la factura).

- **La solución profesional:** Envolver las operaciones que dependen la una de la otra en un bloque **`with transaction.atomic():`**.
    
- Si el código dentro del bloque se ejecuta al 100% sin fallos, se hace un **Commit** (los cambios se escriben con tinta indeleble).
    
- Si salta un error en cualquier línea intermedia, se hace un **Rollback** (un `Ctrl + Z` automático). El saldo vuelve a la normalidad y es como si nunca hubiera pasado nada.
    

### 3. El Escudo de Sanitización (Protección contra XSS)

Este fue tu gran razonamiento de recién. El peligro se llama **XSS** (Cross-Site Scripting). Ocurre cuando un usuario inyecta código malicioso en forma de texto (como etiquetas `<script>`) en campos como el título o la descripción de una tarea.

- **La solución profesional (Tu Opción B):** No prohibimos caracteres de forma estricta (para no romper la experiencia de usuario si escribe signos matemáticos como `>`). En su lugar, el **Serializer** intercepta el texto antes de guardarlo y usa una librería de limpieza.
    

Python

```
# El serializer analiza el string, desarma el código malicioso y deja pasar el texto limpio
title_limpio = nh3.clean(data.get("title"))
```

De esta forma, si el hacker intenta meter código para robar cookies, el backend lo desarma y guarda solo texto inofensivo en MySQL.


------- TAREA 2
Tu otra idea de usar `get_object_or_404(Project, id=project_id, ...)` demuestra que tenés el chip de la seguridad metido en la cabeza, pero te explico por qué en los **Custom Permissions** no hace falta escribir esa línea:

Django REST Framework es extremadamente inteligente. Cuando vos usás un permiso personalizado, la vista se encarga de buscar el objeto por su ID automáticamente tras bambalinas y te lo regala ya cocinado adentro de la variable **`obj`**.

Por lo tanto, en `permissions.py` vos ya no tenés que ir a buscar el proyecto a la base de datos de vuelta. Directamente agarrás ese `obj` (que ya es el proyecto real) y le hacés la pregunta lógica que escribiste vos: _"Che, ¿el creador de este proyecto (`obj.creator`) es el mismo usuario que está haciendo la petición ahora (`request.user`)?"_. Si da `True`, pasa; si da `False`, Django lo rebota automáticamente con un error 403 Forbidden.

### 🛠️ Cómo queda tu Vista Senior Limpia y Reutilizable

Mirá la locura de código que lográs al aislar la seguridad. Tu vista pasa de ser un lío de `if/else` repetitivos a convertirse en una roca minimalista:

Python

```
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Importamos el escudo que creaste vos recién en permissions.py
from .permissions import IsProjectOwner 
from .models import Project

class DeleteProjectAPIView(APIView):
    # 🔥 METEMOS TU NUEVO ESCUDO ACÁ. 
    # El usuario tiene que estar logueado Y además pasar tu prueba de creador.
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def delete(self, request, project_id):
        # 1. Buscamos el proyecto común. No hace falta cruzarlo acá...
        # ¡Porque tus permission_classes se ejecutan antes y blindan la vista!
        project = get_object_or_404(Project, id=project_id)
        
        # 2. Django REST Framework corre automáticamente tu método 'has_object_permission'
        # pasándole este 'project' como 'obj'. Si no es el dueño, el código ni llega acá abajo.
        self.check_object_permissions(request, project)
        
        # 3. Si llegó acá, es el creador real. Borramos sin miedo.
        project.delete()
        return Response({"status": "Proyecto eliminado con éxito"}, status=status.HTTP_200_OK)
```

### 💎 La ventaja estratégica de lo que hiciste:

Si mañana el jefe te pide crear la vista `UpdateProjectAPIView` (para editar el nombre del proyecto), no tenés que volver a inventar la rueda ni copiar código. Simplemente creás la vista y le clavás la misma línea arriba: `permission_classes = [IsAuthenticated, IsProjectOwner]`. Tu seguridad quedó centralizada en un solo lugar. Si el día de mañana cambia una regla, la modificás en tu archivo de permisos y impacta en todo el sistema al mismo tiempo.