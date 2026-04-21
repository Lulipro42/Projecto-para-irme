-- 1) CTE basica
WITH personas_cte AS (
  SELECT id, nombre, edad
  FROM personas
)
SELECT *
FROM personas_cte;
sql

-- 2) CTE con filtro (edad >= 18) y orden
WITH mayores_cte AS (
  SELECT nombre, edad
  FROM personas
  WHERE edad >= 18
)
SELECT nombre, edad
FROM mayores_cte
ORDER BY edad DESC;
sql

-- 3) CTE con agregacion (cantidad de inscripciones por persona)
WITH inscripciones_por_persona AS (
  SELECT persona_id, COUNT(*) AS cantidad
  FROM inscripciones
  GROUP BY persona_id
)
SELECT persona_id, cantidad
FROM inscripciones_por_persona;
sql

-- 4) ROW_NUMBER basico (orden por edad desc)
SELECT
  nombre,
  edad,
  ROW_NUMBER() OVER (ORDER BY edad DESC) AS fila
FROM personas;
sql

-- 5) ROW_NUMBER por grupo (por curso_id)
SELECT
  curso_id,
  persona_id,
  ROW_NUMBER() OVER (
    PARTITION BY curso_id
    ORDER BY persona_id
  ) AS fila_en_curso
FROM inscripciones;
sql

-- 6) RANK basico (empates por edad)
SELECT
  nombre,
  edad,
  RANK() OVER (ORDER BY edad DESC) AS ranking_edad
FROM personas;