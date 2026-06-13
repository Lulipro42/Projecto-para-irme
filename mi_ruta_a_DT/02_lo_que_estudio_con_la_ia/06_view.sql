-- 1) Crear vista empleados con departamento
CREATE VIEW vw_empleados_con_depto AS
SELECT e.nombre AS empleado, e.edad, e.email, d.nombre AS departamento
FROM empleados e
JOIN departamentos d ON e.departamento_id = d.id;

-- 2) Consultar vista con filtro
SELECT *
FROM vw_empleados_con_depto
WHERE edad >= 25;

-- 3) Crear vista cursos resumen
CREATE VIEW vw_cursos_resumen AS
SELECT c.curso, COUNT(i.persona_id) AS cantidad_alumnos
FROM cursos c
LEFT JOIN inscripciones i ON c.id = i.curso_id
GROUP BY c.id, c.curso;

-- 4) Consultar vista ordenada
SELECT *
FROM vw_cursos_resumen
ORDER BY cantidad_alumnos DESC;

-- 5) Eliminar una vista
DROP VIEW vw_cursos_resumen;

-- 6) Recrear vista con JOIN adicional (promedio edad)
CREATE VIEW vw_cursos_resumen AS
SELECT
  c.curso,
  COUNT(i.persona_id) AS cantidad_alumnos,
  AVG(p.edad) AS promedio_edad
FROM cursos c
LEFT JOIN inscripciones i ON c.id = i.curso_id
LEFT JOIN personas p ON i.persona_id = p.id
GROUP BY c.id, c.curso;

---------


-- 1) Crear vista empleados con departamento

----CREATE VIEW vw_empleados_con_depto AS
-- CREATE VIEW crea una vista (una tabla virtual basada en una consulta)

--SELECT e.nombre AS empleado, e.edad, e.email, d.nombre AS departamento
-- Selecciona columnas de dos tablas
-- e.nombre se renombra como "empleado"
-- d.nombre se renombra como "departamento"

--FROM empleados e
-- Tabla empleados con alias "e"

--JOIN departamentos d ON e.departamento_id = d.id;
-- JOIN conecta empleados con departamentos
-- Se relacionan cuando departamento_id de empleados coincide con id de departamentos


--------


-- 2) Consultar vista con filtro
-
--SELECT *
-- Selecciona todas las columnas de la vista

----FROM vw_empleados_con_depto
-- Usa la vista creada anteriormente

--WHERE edad >= 25;
-- Filtra solo empleados que tengan 25 años o más


-----------


-- 3) Crear vista cursos resumen

--CREATE VIEW vw_cursos_resumen AS
-- Se crea una vista llamada vw_cursos_resumen

--SELECT c.curso, COUNT(i.persona_id) AS cantidad_alumnos
-- c.curso muestra el nombre del curso
-- COUNT cuenta cuántas personas están inscritas en cada curso
-- El resultado se guarda como "cantidad_alumnos"

--FROM cursos c
-- Tabla cursos con alias c

--LEFT JOIN inscripciones i ON c.id = i.curso_id
-- LEFT JOIN incluye todos los cursos aunque no tengan alumnos
-- Si no hay alumnos, aparecerá NULL

--GROUP BY c.id, c.curso;
-- GROUP BY agrupa los resultados por curso
-- Es necesario para usar funciones como COUNT



-----------



-- 4) Consultar vista ordenada

--SELECT *
-- Selecciona todas las columnas

--FROM vw_cursos_resumen
-- Consulta la vista creada

--ORDER BY cantidad_alumnos DESC;
-- Ordena los cursos desde el que tiene más alumnos al que tiene menos



----------



-- 5) Eliminar una vista

---DROP VIEW vw_cursos_resumen;
-- DROP VIEW elimina la vista de la base de datos
-- No elimina las tablas originales, solo la vista



----------



-- 6) Recrear vista con JOIN adicional (promedio edad)

--CREATE VIEW vw_cursos_resumen AS
-- Se crea nuevamente la vista con más información

--SELECT
--  c.curso,
--  COUNT(i.persona_id) AS cantidad_alumnos,
  -- Cuenta cuántos alumnos tiene cada curso

--  AVG(p.edad) AS promedio_edad
  -- Calcula la edad promedio de los alumnos del curso

--FROM cursos c
-- Tabla cursos

--LEFT JOIN inscripciones i ON c.id = i.curso_id
-- Conecta cursos con inscripciones

--LEFT JOIN personas p ON i.persona_id = p.id
-- Conecta inscripciones con la tabla personas
-- Esto permite acceder a la edad de cada alumno

--GROUP BY c.id, c.curso;
-- Agrupa por curso para poder calcular COUNT y AVG