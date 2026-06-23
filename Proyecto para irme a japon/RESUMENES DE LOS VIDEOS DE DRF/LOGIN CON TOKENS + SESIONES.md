## 📋 Reporte de Evaluación Técnica (Login Custom + Control de Sesiones)

### 1. Criterios de Aprobación (¿Cumple con el nivel requerido?)

- **¿Es Arquitectura Limpia?:** **SÍ.** En lugar de usar la ruta por defecto que trae DRF (`obtain_auth_token`), el instructor sobreescribe la vista heredando de `ObtainAuthToken` Esto te permite meter mano en el método `post` para manipular la respuesta JSON y customizar la seguridad antes de devolver el token.
    
- **¿Aporta optimización?:** **Aporta Control de Estado.** El código que agrega para limpiar sesiones es destructivo pero sumamente efectivo si querés controlar de forma estricta quién está conectado.
    
- **¿Nivel Técnico Correcto?:** **SÍ.** El manejo de decodificación de sesiones encriptadas de Django (`session.decode()`) a nivel ORM es un recurso avanzado de backend que no se ve en cursos básicos 
    

### 2. Fundamentos de por qué SÍ o por qué NO te sirve

- **Por qué SÍ te sirve:** Es obligatorio para tu e-commerce. Si usás el login por defecto de Django REST, solo te devuelve un string con el token. Con este enfoque custom, podés devolverle al frontend un combo completo: el token de acceso, los datos del perfil del usuario (nombre, email) para pintarlos en el header de la web, y un mensaje de éxito estructurado 
    
- **Por qué NO te sirve:** La última parte del video donde explica el caso de uso de _"bloquear el re-login si ya existe un token"_ mandando un `HTTP 409 Conflict` puede ser molesta para la experiencia de usuario (UX) en un e-commerce. Es mejor la primera estrategia: si se loguea de nuevo, le refrescás el token y listo.
    

### 3. Explicación del Core del Video (Mecánica Avanzada)

El profesor resuelve un problema clásico: **¿Cómo evitar que dos personas usen la misma cuenta al mismo tiempo o cómo limpiar el rastro viejo si el usuario se loguea de nuevo?**

#### Mecánica 1: El truco del `get_or_create()` y renovación de Token [
Al usar el ORM de Django con `Token.objects.get_or_create(user=user)`, el backend averigua si el usuario ya tenía un token en SQLite:

- Si **no tenía**, lo crea (`created=True`) y se lo da
    
- Si **ya tenía** (`created=False`), el instructor toma una decisión de diseño: **borra el token viejo de la base de datos y genera uno nuevo**  Esto desautoriza instantáneamente a cualquier otra pestaña o dispositivo antiguo.
    

#### Mecánica 2: Destrucción de Sesiones Concurrentes de Django 

Si el usuario inició sesión en el panel de administración clásico de Django (`/admin`), Django guarda una cookie de sesión en la tabla `django_session`. El instructor tira este bloque de código quirúrgico para limpiar esa tabla:

1. Filtra todas las sesiones de la base de datos que no hayan expirado aún (`expire_date__gpg=datetime.now()`) 
    
2. Recorre cada sesión y la decodifica (`session.decode()`) para leer el diccionario interno que guarda Django 
    
3. Busca la clave `_auth_user_id` (que es el ID del usuario dueño de esa sesión) 
    
4. Si coincide con el usuario que está haciendo login en la API, ejecuta un `session.delete()`, **pateándolo inmediatamente del Admin de Django** 
    

### 4. Código Limpio: La Vista de Login Customizada

Filtrando las vueltas del video, este es el archivo `views.py` limpio dentro de tu app de usuarios (reemplazando los prints por la lógica real):

Python

```
from datetime import datetime
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sessions.models import Session
from apps.users.api.serializers import UserTokenSerializer # Tu serializador custom de perfil

class CustomLogin(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            
            # Validación de cuenta activa
            if not user.is_active:
                return Response({'error': 'Este usuario no puede iniciar sesión.'}, status=status.HTTP_401_UNAUTHORIZED)
            
            # MECÁNICA 1: Control y renovación del Token en BD
            token, created = Token.objects.get_or_create(user=user)
            if not created:
                token.delete()
                token = Token.objects.create(user=user)
            
            # MECÁNICA 2: Barrido de sesiones activas en el Admin/Web tradicional
            all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if str(user.id) == session_data.get('_auth_user_id'):
                        session.delete()
            
            # Serializamos los datos del usuario para el Frontend
            user_serializer = UserTokenSerializer(user)
            
            return Response({
                'token': token.key,
                'user': user_serializer.data,
                'message': 'Inicio de sesión exitoso.'
            }, status=status.HTTP_201_CREATED)
            
        return Response({'error': 'Nombre de usuario o contraseña incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)
```

**Veredicto del Tech Lead:** Con este capítulo ya tenés un endpoint de Login sólido que no solo autentica, sino que gestiona el estado de los tokens viejos y limpia sesiones residuales.