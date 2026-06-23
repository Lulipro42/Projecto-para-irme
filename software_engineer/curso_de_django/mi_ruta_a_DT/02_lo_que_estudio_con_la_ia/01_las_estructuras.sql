-- 1) tipo_edad (<18 menor, >=18 adulto)
SELECT
  p.id,
  p.nombre,
  p.edad,
  CASE
    WHEN p.edad < 18 THEN 'menor'
    ELSE 'adulto'
  END AS tipo_edad
FROM personas p;

------------

-- 2) estado_email (NULL o '' => sin_email)
SELECT
  p.id,
  p.nombre,
  p.email,
  CASE
    WHEN p.email IS NULL OR p.email = '' THEN 'sin_email'
    ELSE 'con_email'
  END AS estado_email
FROM personas p;

-----------

-- 3) Conteo por tipo_edad
SELECT
  CASE
    WHEN p.edad < 18 THEN 'menor'
    ELSE 'adulto'
  END AS tipo_edad,
  COUNT(*) AS cantidad
FROM personas p
GROUP BY
  CASE
    WHEN p.edad < 18 THEN 'menor'
    ELSE 'adulto'
  END;

-- 4) Conteo por estado_email
SELECT
  CASE
    WHEN p.email IS NULL OR p.email = '' THEN 'sin_email'
    ELSE 'con_email'
  END AS estado_email,
  COUNT(*) AS cantidad
FROM personas p
GROUP BY
  CASE
    WHEN p.email IS NULL OR p.email = '' THEN 'sin_email'
    ELSE 'con_email'
  END;

-----

-- 5) Join cursos + rango_edad
SELECT
  p.nombre,
  c.curso,
  p.edad,
  CASE
    WHEN p.edad < 18 THEN '<18'
    WHEN p.edad BETWEEN 18 AND 29 THEN '18-29'
    ELSE '30+'
  END AS rango_edad
FROM inscripciones i
INNER JOIN personas p ON i.persona_id = p.id
INNER JOIN cursos c ON i.curso_id = c.id;


-----------

-- 6) Conteo de alumnos por curso y rango_edad
SELECT
  c.curso,
  CASE
    WHEN p.edad < 18 THEN '<18'
    WHEN p.edad BETWEEN 18 AND 29 THEN '18-29'
    ELSE '30+'
  END AS rango_edad,
  COUNT(*) AS cantidad_alumnos
FROM inscripciones i
INNER JOIN personas p ON i.persona_id = p.id
INNER JOIN cursos c ON i.curso_id = c.id
GROUP BY
  c.id, c.curso,
  CASE
    WHEN p.edad < 18 THEN '<18'
    WHEN p.edad BETWEEN 18 AND 29 THEN '18-29'
    ELSE '30+'
  END
ORDER BY c.curso, rango_edad;



----------

-- 7) Bandera inscripto / no_inscripto (desde personas + LEFT JOIN)
SELECT
  p.id,
  p.nombre,
  CASE
    WHEN i.id IS NULL THEN 'no_inscripto'
    ELSE 'inscripto'
  END AS estado_inscripcion
FROM personas p
LEFT JOIN inscripciones i ON p.id = i.persona_id
GROUP BY p.id, p.nombre,
  CASE
    WHEN i.id IS NULL THEN 'no_inscripto'
    ELSE 'inscripto'
  END;



-------------


-- 8) Reporte final por persona
SELECT
  p.nombre,
  p.edad,
  CASE
    WHEN p.edad < 18 THEN 'menor'
    ELSE 'adulto'
  END AS tipo_edad,
  CASE
    WHEN p.email IS NULL OR p.email = '' THEN 'sin_email'
    ELSE 'con_email'
  END AS estado_email,
  CASE
    WHEN COUNT(i.id) > 0 THEN 'inscripto'
    ELSE 'no_inscripto'
  END AS estado_inscripcion
FROM personas p
LEFT JOIN inscripciones i ON p.id = i.persona_id
GROUP BY p.id, p.nombre, p.edad, p.email
ORDER BY p.nombre;

