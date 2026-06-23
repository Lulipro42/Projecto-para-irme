## Resumen del Video para un Backend Engineer

El video se divide en dos decisiones arquitectónicas fundamentales:

### 1. Creación de una Capa Base Reutilizable

En lugar de ir directo a crear las tablas de productos, el instructor da un paso atrás y crea una app llamada `base`. Dentro, define un modelo abstracto (`BaseModel`) que contiene:

- Clave primaria explícita (`id`).
    
- Campos de auditoría temporal (`created_date`, `modified_date`, `deleted_date`).
    
- Un campo booleano de control (`state`).
    

**La mirada de ingeniería:** Esto establece la infraestructura para implementar **Borrado Lógico (Soft Delete)**. Como Backend Engineer, casi nunca vas a querer borrar registros físicos con un `DELETE` de SQL en producción (por integridad referencial y auditoría). En su lugar, cambias el campo `state` a `False`. Al hacerlo en un modelo abstracto, garantizás que **todas** las entidades del sistema hereden esta capacidad automáticamente.

### 2. Diseño de Relaciones y Normalización

El instructor desglosa el módulo de productos en entidades más pequeñas y relacionales: `MeasurementUnit` (Unidades de medida), `CategoryProduct` (Categorías), `Indicator` (Descuentos) y `Product` (Productos), todas conectadas mediante claves foráneas (`ForeignKey`).

**La mirada de ingeniería:** Esto es un ejercicio de **Normalización de Bases de Datos**. En lugar de meter la unidad de medida o el descuento como un texto plano dentro de la tabla de productos (lo que duplicaría datos y generaría inconsistencias), se separan en tablas independientes. Además, al delegar el control de stock e inventario a un módulo futuro, el instructor respeta el **Principio de Responsabilidad Única**: el modelo `Product` solo debe conocer la información de identidad del producto, no los movimientos de stock.

## ¿Qué es DRY (Don't Repeat Yourself)?

**DRY** (en español: _"No te repitas"_) es uno de los principios de diseño de software más importantes en la ingeniería backend. Fue formulado por Andy Hunt y Dave Thomas en el libro _The Pragmatic Programmer_ y su regla de oro es:

> "Cada pieza de conocimiento o lógica debe tener una representación única, inequívoca y autoritaria dentro de un sistema."

En criollo: **evitá duplicar código o lógica de negocio.** Si terminás copiando y pegando el mismo bloque de código (o la misma definición de campos) en dos o más lugares distintos, estás violando el principio DRY.

### ¿Cómo se aplicó DRY en el video?

Si el instructor no hubiera aplicado DRY, habría tenido que escribir los campos `id`, `state`, `created_date`, etc., manualmente dentro de `Product`, dentro de `CategoryProduct`, dentro de `MeasurementUnit` y en cada modelo nuevo.

Si el día de mañana el cliente te pide: _"Che, ahora necesito que la fecha de modificación guarde también la zona horaria"_, tendrías que ir a modificar esa lógica en 20 archivos distintos (rompiendo el sistema y aumentando la chance de mandarte una macana). Al usar **herencia de modelos abstractos**, aplicó DRY: modificás el `BaseModel` en un solo lugar y el cambio se propaga a todo el sistema.

### Beneficios de DRY para el Backend:

- **Mantenibilidad:** Menos líneas de código significan menos lugar para que se escondan los bugs.
    
- **Facilidad de cambio:** Si la lógica de negocio cambia, solo la editás en un punto central.
    
- **Legibilidad:** El código se vuelve mucho más limpio y fácil de entender para otros ingenieros del equipo.

## Serializadores de Aplicacion de productos

### 1. Refactorización de Estructura: De Archivos a Paquetes

Al inicio de un proyecto, es común ver un archivo único `serializers.py` o `views.py`. Sin embargo, en sistemas reales con docenas de modelos y lógicas de validación complejas, ese archivo crece hasta volverse ilegible (un "God File").

**La mirada de ingeniería:** El instructor aplica el principio de **Modularidad** y separación de conceptos convirtiendo el archivo en un paquete (una carpeta).

- Crea la carpeta `serializers/` dentro de la API.
    
- Separa la lógica en `general_serializers.py` (para modelos secundarios o de soporte) y `product_serializers.py` (exclusivo para el modelo principal).
    

Esto reduce el acoplamiento y facilita el mantenimiento. Si necesitas modificar cómo se procesa un producto, sabes exactamente en qué microarchivo buscar, sin interferir con el resto de la aplicación.

### 2. Clasificación de Modelos (Entidades Principales vs. Secundarias)

El instructor hace una distinción clave para el diseño del e-commerce:

- **Entidades Generales o de Soporte:** `MeasurementUnit` (Unidad de medida), `CategoryProduct` (Categoría) e `Indicator` (Descuentos). Son tablas tipo diccionario o _lookups_ que sirven para alimentar formularios o relaciones, pero rara vez contienen lógica de negocio compleja. Por eso se agrupan en un solo archivo general.
    
- **Entidad Principal:** `Product`. Es el núcleo del módulo. A lo largo del desarrollo, un modelo principal puede requerir hasta 4 o más serializadores distintos (uno para listar, uno para crear, uno para el frontend, uno para el panel de administración). Por ende, exige su propio archivo independiente.
    

### 3. El uso estricto de `exclude` para Campos de Infraestructura

En lugar de usar `fields = '__all__'`, el instructor define la propiedad `exclude = ('state',)` en el `class Meta` de todos los serializadores.

Python

```
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state',) # Excluye el campo de infraestructura
```

**La mirada de ingeniería:** El campo `state` (que creamos en el `BaseModel` del video anterior para el borrado lógico) es un campo de **infraestructura e integridad interna** del backend. El cliente (frontend) nunca debería poder enviar un `POST` alterando el estado de un producto directamente, ni necesita leerlo en un listado ordinario (ya que el backend se encarga de filtrar solo los activos). Al excluirlo, proteges la consistencia de los datos y reduces el payload de la API.

## Conexión con la Arquitectura de Microservicios

Hacia el final del video, el instructor menciona algo crucial para tu perfil como Software Engineer: la transición hacia **Microservicios**.

Aunque el curso construye una arquitectura **Monolítica** (todo corre en el mismo servidor y base de datos), organizarlo de forma modular (dividiendo estrictamente por carpetas de `products`, `users`, `serializers` y `views`) permite que el monolito sea **altamente cohesivo y desacoplado**.

Si en el futuro el tráfico del e-commerce explota y el módulo de productos necesita procesar millones de peticiones por segundo de forma independiente, un código organizado así se puede "arrancar" y convertir en un microservicio autónomo con un esfuerzo mínimo, ya que sus fronteras lógicas quedaron perfectamente definidas desde el primer día.