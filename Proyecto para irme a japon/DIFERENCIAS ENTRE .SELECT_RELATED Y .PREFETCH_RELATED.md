La diferencia principal es que `.select_related()` realiza uniones (**JOINs**) directamente a nivel de base de datos en una sola consulta, mientras que `.prefetch_related()` ejecuta consultas separadas y realiza la unión en **Python**. Ambos métodos optimizan el rendimiento para evitar el problema de "las consultas N+1". 

Aquí te detallo cómo funciona cada uno:

`.select_related()`

- **Cuándo usarlo:** Relaciones de un solo objeto, como `ForeignKey` o `OneToOneField`.
- **Cómo funciona:** Utiliza la cláusula `SQL JOIN` para traer los datos del objeto principal y del objeto relacionado en **una única consulta**.
- **Limitaciones:** No se puede usar en relaciones de muchos a muchos (`ManyToManyField`) ni en relaciones inversas (ej. múltiples libros relacionados a un autor) ya que esto multiplicaría excesivamente el tamaño de la tabla resultante en SQL.

`.prefetch_related()`

- **Cuándo usarlo:** Colecciones y múltiples objetos relacionados, como `ManyToManyField` o relaciones inversas de `ForeignKey`.
- **Cómo funciona:** Ejecuta **una consulta separada** para el modelo principal y otra para cada relación que se solicite. Luego, el motor de Django realiza la unión de los resultados directamente en **Python**.
- **Ventaja:** Puede hacer prefetch de cualquier cosa, incluso de objetos que ya pasaron por `select_related`