## 📋 Reporte de Evaluación Técnica (Mecanismos de Autenticación)

### 1. Criterios de Aprobación (¿Cumple con el nivel requerido?)

- **¿Es Arquitectura Limpia?:** **SÍ.** El análisis que hace el instructor sobre desacoplar la sesión tradicional de Django (basada en cookies que dependen del navegador) y pasar a una autenticación stateless por Headers es fundamental para que tu backend pueda atender en un futuro tanto a una app mobile como a un frontend SPA de manera agnóstica.
    
- **¿Aporta optimización?:** **Aporta balance de infraestructura.** Como explica en el video, usar `TokenAuthentication` nativo requiere golpear la base de datos en cada consulta HTTP para validar si el token existe [[27:19](http://www.youtube.com/watch?v=2EemvteGLr4&t=1639)]. No es tan rápido en memoria como JWT, pero para un e-commerce en desarrollo evita dolores de cabeza con la invalidación de sesiones (un token robado se borra de la tabla de SQLite y queda revocado al instante).
    
- **¿Nivel Técnico Correcto?:** **SÍ.** El instructor toma una postura de ingeniería muy madura: en vez de instalar una librería para meter "código mágico", decide usar el core de Django REST Framework para personalizar el flujo y tener control absoluto sobre el tiempo de expiración y las sesiones simultáneas [[03:54](http://www.youtube.com/watch?v=2EemvteGLr4&t=234)].
    

### 2. Fundamentos de por qué SÍ o por qué NO te sirve

- **Por qué SÍ te sirve:** Te da el mapa exacto de cómo viaja la identidad del usuario en un entorno API Rest. Al no estar usando el renderizado clásico de templates de Django, necesitás entender cómo `request.user` se rellena de forma dinámica en cada petición a través de los Middleware de DRF usando la cabecera `Authorization` [[26:26](http://www.youtube.com/watch?v=2EemvteGLr4&t=1586)].
    
- **Por qué NO te sirve:** No te sirve la teoría pura de JWT en este punto del curso porque, tal como el profesor advierte en el minuto [[27:46](http://www.youtube.com/watch?v=2EemvteGLr4&t=1666)], **él no va a utilizar JWT para el proyecto del e-commerce**. Va a construir sobre `TokenAuthentication`. No te enredes con conceptos de firmas asimétricas si tu backend va a operar con tokens planos guardados en la BD.
    

### 3. Explicación del Core del Video (Análisis de Ingeniería)

El secreto mejor guardado de este capítulo se encuentra cuando el instructor analiza el código fuente de DRF en el minuto **[[33:17](http://www.youtube.com/watch?v=2EemvteGLr4&t=1997)]**:

#### El modelo interno de DRF (`authtoken`)

La autenticación nativa por token de Django no es criptografía compleja; bajo el capó es una simple tabla relacional que se mapea así en tu base de datos:

SQL

```
CREATE TABLE authtoken_token (
    key VARCHAR(40) PRIMARY KEY,
    created DATETIME NOT NULL,
    user_id INTEGER UNIQUE REFERENCES auth_user(id)
);
```

#### Mecánica de Generación de la Clave [[34:27](http://www.youtube.com/watch?v=2EemvteGLr4&t=2067)]:

Cuando un usuario hace login exitoso, la función `generate_key()` de DRF ejecuta este proceso a bajo nivel en Python:

1. Toma 20 bytes aleatorios utilizando el sistema operativo (`os.urandom`).
    
2. Lo codifica en formato hexadecimal (`binascii.hexlify`), lo que da como resultado un string plano de **40 caracteres**.
    
3. Ese string se guarda directamente en la columna `key` de la tabla de arriba.
    

**El flujo de la petición [[26:26](http://www.youtube.com/watch?v=2EemvteGLr4&t=1586)]:** Cuando el cliente (Frontend) hace un request, manda en los headers: `Authorization: Token 40_characters_string`. El middleware de DRF intercepta ese string, hace un `SELECT * FROM authtoken_token WHERE key = '...'` y, si lo encuentra, asocia el `user_id` correspondiente al objeto `request.user` de tu vista.

### 4. Plan de Implementación (Preparando el terreno)

Para cuando salgamos a la cancha a escribir el código del Login/Logout, tu configuración de infraestructura base en Django debe quedar lista de la siguiente manera:

#### 1. Modificación de `settings.py`

Debemos registrar la app interna de DRF encargada de manejar el ciclo de vida y las migraciones de la tabla de tokens:

Python

```
INSTALLED_APPS = [
    # ... apps por defecto
    'rest_framework',
    'rest_framework.authtoken', # Aplicación nativa que crea la tabla authtoken_token
    # ... tus aplicaciones locales
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # Activamos la autenticación por cabeceras de Token
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

#### 2. Ejecución de Migraciones (Consola)

Al agregar `rest_framework.authtoken`, se generan nuevas tablas relacionales. Necesitamos impactar tu base de datos antes de escribir las vistas de autenticación:

Bash

```
python manage.py migrate
```

**Veredicto del Tech Lead:** **¡Concepto asimilado y optimizado!** Ya sabés exactamente cómo viajan los hilos de la seguridad en el backend, qué pasa en la base de datos cuando se genera un token y por qué no vamos a usar JWT por ahora.