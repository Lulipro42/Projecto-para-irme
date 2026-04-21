-- SQL (Structured Query Language) es el lenguaje para trabajar con bases de datos relacionales, y toda la informacion se guarda en la base de datos 
--Bases de datos relacionales (SQL)
--Guardan datos en tablas (filas y columnas) y relacionan tablas entre sí con claves.

--Características:

--Esquema definido (tipos y estructura clara).
--Relaciones entre tablas (JOIN).
--SQL para consultar.
--Muy buenas para consistencia y datos estructurados.
--Ejemplos:

--PostgreSQL
--MySQL
--SQL Server
--Ejemplo de uso:

--Usuarios, pedidos, productos en e-commerce.

/*
Características:

Estructura más flexible.
Escalan bien para grandes volúmenes y datos cambiantes.
No siempre usan SQL clásico.

Tipos comunes:

Documentos: MongoDB
Clave-valor: Redis
Columnar: Cassandra
Grafos: Neo4j

Ejemplo de uso:

Logs, eventos, catálogos con campos variables, sesiones.
*/

--Bases de datos no relacionales (NoSQL)
--No dependen del modelo clásico de tablas relacionadas. Pueden guardar documentos, pares clave-valor, grafos, etc.


-- Sirve para:

-- Consultar datos (SELECT)
-- Filtrar (WHERE)
-- Agrupar y resumir (GROUP BY, COUNT, AVG, SUM)
-- Unir tablas (JOIN)
-- Insertar/actualizar/borrar (INSERT, UPDATE, DELETE)
/*
SELECT
Lección 8: https://youtu.be/OuJerKzV5T0?t=5618
*/

-- Obtiene todos los datos de la tabla "users"
SELECT * FROM users;

-- Obtiene todos los nombres de la tabla "users"
SELECT name FROM users;

-- Obtiene todos los identificadores y nombres de la tabla "users"
SELECT user_id, name FROM users;