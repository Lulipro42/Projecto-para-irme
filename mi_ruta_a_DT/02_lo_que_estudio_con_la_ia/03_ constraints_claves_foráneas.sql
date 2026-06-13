-- 1) NOT NULL en departamentos.nombre
ALTER TABLE departamentos
MODIFY nombre VARCHAR(50) NOT NULL;

-- 2) UNIQUE en departamentos.nombre (si no existe)
ALTER TABLE departamentos
ADD CONSTRAINT uq_departamentos_nombre UNIQUE (nombre);

-- 3) Tabla proyectos con FK a departamentos
CREATE TABLE proyectos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  departamento_id INT,
  CONSTRAINT fk_proyectos_departamento
    FOREIGN KEY (departamento_id)
    REFERENCES departamentos(id)
);

-- 4) Insertar proyectos
INSERT INTO proyectos (nombre, departamento_id) VALUES
('Migracion DB', 1),
('ETL Ventas', 2),
('Dashboard BI', 3);

-- 5) Intento con departamento_id inexistente (debe fallar)
INSERT INTO proyectos (nombre, departamento_id)
VALUES ('Proyecto Invalido', 999);

-- 6) Cambiar FK a ON DELETE SET NULL
ALTER TABLE proyectos
DROP FOREIGN KEY fk_proyectos_departamento;

ALTER TABLE proyectos
ADD CONSTRAINT fk_proyectos_departamento
FOREIGN KEY (departamento_id)
REFERENCES departamentos(id)
ON DELETE SET NULL;

-- 7) Eliminar un departamento y ver efecto en proyectos
DELETE FROM departamentos
WHERE id = 3;

SELECT * FROM proyectos;

-- 8) CHECK edad >= 18 en empleados
ALTER TABLE empleados
ADD CONSTRAINT chk_edad CHECK (edad >= 18);

-- Prueba (debe fallar)
INSERT INTO empleados (nombre, edad, email, departamento_id)
VALUES ('menor', 17, 'menor@mail.com', 1);


-----1️⃣ NOT NULL en departamentos.nombre
--ALTER TABLE departamentos
--MODIFY nombre VARCHAR(50) NOT NULL;
--
--Qué hace:
--
--ALTER TABLE → modifica una tabla existente.
--
--MODIFY → cambia la definición de una columna.
--
--nombre VARCHAR(50) → la columna sigue siendo texto de máximo 50 caracteres.
--
--NOT NULL → ahora no se permiten valores vacíos (NULL).
--
--Ejemplo:
--
--❌ Esto fallaría:
--
--INSERT INTO departamentos (nombre) VALUES (NULL);
--
--Porque ahora el nombre es obligatorio.
--
--2️⃣ UNIQUE en departamentos.nombre
--ALTER TABLE departamentos
--ADD CONSTRAINT uq_departamentos_nombre UNIQUE (nombre);
--
--Qué hace:
--
--UNIQUE evita duplicados.
--
--Ningún departamento puede tener el mismo nombre.
--
--Ejemplo:
--
--Si ya existe:
--
--Ventas
--
--Esto fallará:
--
--INSERT INTO departamentos (nombre) VALUES ('Ventas');
--
--Porque el nombre debe ser único.
--
--3️⃣ Crear tabla proyectos con Foreign Key
--CREATE TABLE proyectos (
--  id INT PRIMARY KEY AUTO_INCREMENT,
--  nombre VARCHAR(100) NOT NULL,
--  departamento_id INT,
--  CONSTRAINT fk_proyectos_departamento
--    FOREIGN KEY (departamento_id)
--    REFERENCES departamentos(id)
--);
--
--Aquí pasan varias cosas importantes.
--
--id
--id INT PRIMARY KEY AUTO_INCREMENT
--
--PRIMARY KEY → identificador único.
--
--AUTO_INCREMENT → se genera automáticamente.
--
--Ejemplo:
--
--1
--2
--3
--4
--
--nombre
--nombre VARCHAR(100) NOT NULL
--
--Nombre del proyecto obligatorio.
--
--departamento_id
--departamento_id INT
--
--Esto guardará qué departamento pertenece al proyecto.
--
--Foreign Key
--FOREIGN KEY (departamento_id)
--REFERENCES departamentos(id)
--
--Esto significa:
--
--👉 departamento_id debe existir en departamentos.id.
--
--Ejemplo:
--
--Tabla departamentos
--
--id	nombre
--1	IT
--2	Ventas
--
--Entonces en proyectos puedes poner:
--
--departamento_id = 1
--departamento_id = 2
--
--Pero no:
--
--departamento_id = 99
--
--4️⃣ Insertar proyectos
--INSERT INTO proyectos (nombre, departamento_id) VALUES
--('Migracion DB', 1),
--('ETL Ventas', 2),
--('Dashboard BI', 3);
--
--Aquí agregas proyectos.
--
--Ejemplo:
--
--id	nombre	departamento_id
--1	Migracion DB	1
--2	ETL Ventas	2
--3	Dashboard BI	3
--
--5️⃣ Intentar insertar departamento inexistente
--INSERT INTO proyectos (nombre, departamento_id)
--VALUES ('Proyecto Invalido', 999);
--
--Esto debe fallar.
--
--Porque no existe departamento 999.
--
--La Foreign Key protege la base de datos para evitar errores.
--
--6️⃣ Cambiar comportamiento al borrar departamentos
--
--Primero eliminas la foreign key:
--
----ALTER TABLE proyectos
--DROP FOREIGN KEY fk_proyectos_departamento;
--
--Luego la vuelves a crear con una regla nueva:
--
--ALTER TABLE proyectos
--ADD CONSTRAINT fk_proyectos_departamento
--FOREIGN KEY (departamento_id)
--REFERENCES departamentos(id)
--ON DELETE SET NULL;

--Esto significa:

--Si borras un departamento…

--Antes → daba error.
--Ahora → el departamento_id del proyecto se vuelve NULL.

--7️⃣ Borrar un departament
DELETE FROM departamentos --
--WHERE id = 3;

--Si existía esto:

--proyecto	departamento_id
--Dashboard BI	3

--Después de borrar el departamento:

--proyecto	departamento_id
--Dashboard BI	NULL

--El proyecto sigue existiendo.

--Solo perdió su departamento.

--8️⃣ CHECK en edad
--ALTER TABLE empleados
--ADD CONSTRAINT chk_edad CHECK (edad >= 18);

--Esto crea una regla:

--👉 edad debe ser 18 o más.

--Prueba que debe fallar
--INSERT INTO empleados (nombre, edad, email, departamento_id)
--VALUES ('menor', 17, 'menor@mail.com', 1);

--Esto falla porque:

--17 < 18