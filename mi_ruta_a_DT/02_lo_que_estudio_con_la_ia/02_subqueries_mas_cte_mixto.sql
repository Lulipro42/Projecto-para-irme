-- 1) Personas con edad mayor al promedio general
SELECT p.id, p.nombre, p.edad
FROM personas p
WHERE p.edad > (
  SELECT AVG(edad)
  FROM personas
);


-----------


-- 2) Personas con cantidad de inscripciones mayor al promedio por persona
SELECT p.id, p.nombre, COUNT(i.id) AS cantidad_inscripciones
FROM personas p
JOIN inscripciones i ON p.id = i.persona_id
GROUP BY p.id, p.nombre
HAVING COUNT(i.id) > (
  SELECT AVG(t.cant)
  FROM (
    SELECT COUNT(*) AS cant
    FROM inscripciones
    GROUP BY persona_id
  ) t
);

---------


-- 3) Curso(s) con mayor cantidad de alumnos (con empates)
SELECT c.id, c.curso, COUNT(i.persona_id) AS cantidad_alumnos
FROM cursos c
LEFT JOIN inscripciones i ON c.id = i.curso_id
GROUP BY c.id, c.curso
HAVING COUNT(i.persona_id) = (
  SELECT MAX(t.cant)
  FROM (
    SELECT COUNT(*) AS cant
    FROM inscripciones
    GROUP BY curso_id
  ) t
);


----------

-- 4) Personas no inscriptas (NOT EXISTS)
SELECT p.id, p.nombre, p.edad
FROM personas p
WHERE NOT EXISTS (
  SELECT 1
  FROM inscripciones i
  WHERE i.persona_id = p.id
);


----------


-- 5) Cursos sin alumnos (NOT EXISTS)
SELECT c.id, c.curso
FROM cursos c
WHERE NOT EXISTS (
  SELECT 1
  FROM inscripciones i
  WHERE i.curso_id = c.id
);


------------


-- 6) Subconsulta en SELECT: nombre + cantidad_cursos
SELECT
  p.id,
  p.nombre,
  (
    SELECT COUNT(*)
    FROM inscripciones i
    WHERE i.persona_id = p.id
  ) AS cantidad_cursos
FROM personas p
ORDER BY p.nombre;



---------


-- 7) CTE alumnos_por_curso y filtro >= 2
WITH alumnos_por_curso AS (
  SELECT c.id, c.curso, COUNT(i.persona_id) AS cantidad_alumnos
  FROM cursos c
  LEFT JOIN inscripciones i ON c.id = i.curso_id
  GROUP BY c.id, c.curso
)
SELECT id, curso, cantidad_alumnos
FROM alumnos_por_curso
WHERE cantidad_alumnos >= 2
ORDER BY cantidad_alumnos DESC, curso;



----------


-- 8) CTE inscripciones_por_persona + tipo_inscripcion
WITH inscripciones_por_persona AS (
  SELECT p.id, COUNT(i.id) AS cantidad_inscripciones
  FROM personas p
  LEFT JOIN inscripciones i ON p.id = i.persona_id
  GROUP BY p.id
)
SELECT
  p.nombre,
  p.edad,
  ip.cantidad_inscripciones,
  CASE
    WHEN ip.cantidad_inscripciones >= 2 THEN 'alta'
    ELSE 'baja'
  END AS tipo_inscripcion
FROM personas p
JOIN inscripciones_por_persona ip ON p.id = ip.id
ORDER BY ip.cantidad_inscripciones DESC, p.nombre;
