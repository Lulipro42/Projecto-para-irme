-- 1) Indice en empleados(nombre)
CREATE INDEX idx_empleados_nombre
ON empleados(nombre);

-- 2) Indice compuesto en empleados(departamento_id, edad)
CREATE INDEX idx_empleados_depto_edad
ON empleados(departamento_id, edad);

-- 3) Mostrar indices de empleados
SHOW INDEX FROM empleados;

-- 4) Query que usa el indice compuesto
SELECT *
FROM empleados
WHERE departamento_id = 1
  AND edad >= 25;

-- 5) Eliminar indice de empleados(nombre)
DROP INDEX idx_empleados_nombre ON empleados;

-- 6) Indice unico en proyectos(nombre)
ALTER TABLE proyectos
ADD CONSTRAINT uq_proyectos_nombre UNIQUE (nombre);

-- 7) Explicar plan de ejecucion
EXPLAIN
SELECT *
FROM empleados
WHERE departamento_id = 1
  AND edad >= 25;

-- 8) Comparar EXPLAIN antes/despues de indices
-- (Ejecuta el EXPLAIN antes de crear idx_empleados_dept