
## 💡 Explicación de las Bases: Para entenderlo bien a fondo

Para dominar este capítulo, tenés que asimilar estos tres pilares conceptuales:

### A. La diferencia entre `request.data` y `request.FILES`

En el Django tradicional, los datos de texto van a `request.POST` y los archivos a `request.FILES`. Django Rest Framework unifica ambos mundos dentro del objeto `request.data` para que el flujo sea más limpio. Sin embargo, por detrás, DRF sabe perfectamente qué datos son strings y cuáles son objetos de tipo `UploadedFile`, pasándoselos de forma transparente al serializador.

### B. El objeto `UploadedFile` y sus propiedades

Cuando una imagen pasa la validación inicial, el serializador la manipula como una instancia de `UploadedFile`. Este objeto tiene propiedades clave que podés usar en tus validaciones de backend:

- `.name`: El nombre original del archivo (ej. `foto.png`).
    
- `.size`: El tamaño exacto en bytes.
    
- `.content_type`: El tipo MIME del archivo (ej. `image/jpeg`).
    

### C. Por qué el campo guarda un String en la Base de Datos

Es un error común pensar que la base de datos almacena la imagen real. Guardar binarios pesados en SQL destruye el rendimiento de las consultas. El modelo de Django lo que hace es guardar un `CharField` encubierto (un string con la ruta del archivo, ej: `products/2026/06/remera.jpg`), mientras que el archivo físico se aloja de forma eficiente en el sistema de archivos del servidor o en un servicio en la nube como AWS S3.

### 🔄 Cierre de Sincronización

Con este capítulo, cerrás el rompecabezas completo del manejo de archivos: controlás la mutabilidad en la vista para recibir el formulario limpio, y usás el serializador para validar que la imagen cumpla con los estándares de seguridad y peso del sistema. Tu API de Ecommerce ya es capaz de procesar de punta a punta altas y modificaciones complejas de productos con catálogo visual de forma profesional.