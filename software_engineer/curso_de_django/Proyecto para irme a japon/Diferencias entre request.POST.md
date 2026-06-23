# request.POST

Una **solicitud POST** es un método del protocolo HTTP que se utiliza para **enviar datos desde un cliente** (como un navegador web o una aplicación móvil) **hacia un servidor**. Generalmente se emplea para crear nuevos registros o modificar información en una base de datos


Los aspectos clave de una solicitud POST incluyen:

- **Ocultación de datos:** A diferencia del método GET (que envía parámetros visibles en la URL), los datos de una solicitud POST viajan **dentro del cuerpo del mensaje** (payload o body). 
- **Uso en formularios:** Es el método estándar utilizado cuando un usuario completa y envía un formulario web (como registrarse en un sitio o enviar un mensaje de contacto) o al subir un archivo.
- **Seguridad y tamaño:** Permite enviar una cantidad mucho mayor de información y datos confidenciales de forma más segura que el método GET.

En lenguajes de programación y frameworks web (como Python con Flask/Django o JavaScript en Node.js), `request.POST` es comúnmente el objeto o diccionario donde el servidor recibe y almacena todos esos datos enviados por el usuario para que el backend pueda procesarlos.


# request.GET

Un **`request.GET`** es un objeto utilizado en frameworks de desarrollo web (como Django) que contiene todos los datos enviados por un usuario a través de la **URL**== (usando el método HTTP GET). Sirve para procesar búsquedas, filtros o identificadores que vienen en la dirección web. 
¿Cómo funciona en la práctica?

Cuando un usuario visita una URL con parámetros (por ejemplo: `://tusitio.com`), el servidor captura esta información.

En tu código, puedes acceder a ella como un diccionario:

- `categoria = request.GET.get('categoria')` guardaría el valor `"libros"`.
- `precio = request.GET.get('precio')` guardaría el valor `"bajo"`.

Características principales

- **Visibles en la URL:** Los datos siempre aparecen después del signo de interrogación `?`. 
- **Uso seguro:** Según los estándares web (protocolo HTTP), solo deben usarse para **recuperar o consultar datos**, nunca para modificar, crear o borrar información en la base de datos. 
- **Inseguro para contraseñas:** Como los datos van en la URL, **nunca** deben usarse para enviar información confidencial (como contraseñas o datos bancarios). 

Diferencia clave: `GET` vs `POST`

- **`request.GET`:** Se usa para obtener o filtrar información. Se envía a través de la barra de direcciones.
- **`request.POST`:** Se usa para enviar información delicada o pesada (como rellenar un formulario o registrarse). Se envía de forma oculta en el cuerpo de la petición. 