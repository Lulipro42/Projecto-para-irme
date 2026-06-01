## 🧠 Lo que estudiamos ayer: El problema de las consultas "pesadas" ($N+1$)

Imaginate que en tu tablero Kanban tenés **10 tareas** y cada tarea pertenece a un **proyecto** diferente.

Si vos querés mostrar en pantalla la lista de tareas con el nombre de su proyecto, el Django tradicional hace esto de forma automática (y muy ineficiente):

1. Hace **1 consulta** a la base de datos para traer las 10 tareas.
    
2. Al leer la primera tarea, ve que necesita el proyecto, así que hace **otra consulta** para traer ese proyecto.
    
3. Lee la segunda tarea y hace **otra consulta** para su proyecto... y así con cada una.
    

> **El resultado:** Para mostrar 10 tareas, Django terminó haciendo $1 + 10 = 11$ consultas a la base de datos. Si tuvieras 1000 tareas, haría 1001 consultas. Tu servidor se arrastraría por el piso y la página tardaría una eternidad en cargar.

### 🛠️ La solución que aplicaste: `.select_related()`

Ayer aprendiste a usar una herramienta del ORM de Django llamada `.select_related()`. Al meter eso en tu código, le dijiste a Django:

_"Che, no vayas y vengas mil veces. Hacé una sola consulta inteligente usando un **JOIN de SQL**; traeme las tareas y pegales al lado la información de sus proyectos de un solo viaje"_.

Pasaste de hacer 11 consultas a hacer **exactamente 1**. Un golazo total en rendimiento.

## 🔗 ¿Qué tiene que ver esto con el video de Software Engineer?

Tiene que ver **en un 100%**. En el video del otro programador, donde te explican qué diferencia a un programador que tira código de un **Software Engineer profesional**, el foco está en la **eficiencia, la arquitectura y el rendimiento**.

En las entrevistas de empresas como _Mercado Libre, Globant o Despegar_ (las que vas a buscar en Glassdoor), los entrevistadores técnicos no te van a preguntar si sabés crear una ruta en Django. Te van a poner un caso de estudio y te van a preguntar:

- _"Che, Ulises, nuestra aplicación tiene millones de usuarios y la base de datos está colapsando cuando listamos los productos. ¿Cómo lo solucionarías?"_
    

Si vos respondes: _"Uso `.select_related()` en el backend para hacer un JOIN en la base de datos y matar el problema de la Query $N+1$"_, la respuesta tiene el sello de un **Ingeniero de Software**. Demostrás que no solo hacés que las cosas "funcionen", sino que te importa cómo escala el sistema bajo mucha presión.

### 🚀 En resumen: Ayer y Hoy se dan la mano

Ayer aprendiste a optimizar la lógica y los datos en el backend. Hoy, con el video de Fazt, estás aprendiendo a agarrar esos mismos datos optimizados y empaquetarlos en un formato (JSON) para que viajen por internet hacia cualquier aplicación. ¡Estás armando el rompecabezas completo de la profesión!