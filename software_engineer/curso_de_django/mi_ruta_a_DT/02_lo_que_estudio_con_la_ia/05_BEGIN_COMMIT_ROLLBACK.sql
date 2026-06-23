-- 1) UPDATE + ROLLBACK
START TRANSACTION;

UPDATE empleados
SET edad = edad + 1
WHERE departamento_id = 1;

ROLLBACK;

-- 2) UPDATE + COMMIT
START TRANSACTION;

UPDATE empleados
SET edad = edad + 1
WHERE departamento_id = 2;

COMMIT;

-- 3) Insert con error + ROLLBACK (usa UNIQUE en email)
START TRANSACTION;

INSERT INTO empleados (nombre, edad, email, departamento_id)
VALUES ('temp1', 25, 'dup@mail.com', 1);

INSERT INTO empleados (nombre, edad, email, departamento_id)
VALUES ('temp2', 30, 'dup@mail.com', 2); -- debe fallar por email duplicado

ROLLBACK;

-- 4) SAVEPOINT
START TRANSACTION;

UPDATE empleados
SET edad = edad + 2
WHERE departamento_id = 3;

SAVEPOINT sp1;

UPDATE empleados
SET edad = edad + 5
WHERE departamento_id = 1;

ROLLBACK TO sp1;

COMMIT;

UPDATE + ROLLBACK
START TRANSACTION;

UPDATE empleados
SET edad = edad + 1
WHERE departamento_id = 1;

ROLLBACK;

--Qué pasa aquí:
--
--Paso 1
--START TRANSACTION;
--
--Empieza una transacción.
--Los cambios aún no se guardan definitivamente.
--
--Paso 2
--UPDATE empleados
--SET edad = edad + 1
--WHERE departamento_id = 1;
--
--Esto aumenta la edad en 1 año a todos los empleados del departamento 1.
--
--Ejemplo:
--
--Antes:
--
--nombre	edad	departamento
--Ana	30	1
--Luis	25	1
--
--Después del UPDATE (temporal):
--
--nombre	edad	departamento
--Ana	31	1
--Luis	26	1
--Paso 3
--ROLLBACK;
--
--Aquí cancelas la transacción.
--
--Resultado final:
--
--Las edades vuelven a su valor original.
--
--Es como si nunca hubieras hecho el UPDATE.

--2️⃣ UPDATE + COMMIT
--START TRANSACTION;

--UPDATE empleados
--SET edad = edad + 1
--WHERE departamento_id = 2;

--COMMIT;

--Esto es parecido al anterior, pero cambia el final.

--Paso 1

--Empieza la transacción.

--Paso 2

--Aumenta la edad a los empleados del departamento 2.

--Paso 3
--COMMIT;

--Aquí confirmas los cambios.

--Ahora los cambios se guardan permanentemente en la base de datos.

--Ya no se pueden deshacer con ROLLBACK.

--3️⃣ Insert con error + ROLLBACK
--START TRANSACTION;

--Empieza una transacción.

--Primer insert
--INSERT INTO empleados (nombre, edad, email, departamento_id)
--VALUES ('temp1', 25, 'dup@mail.com', 1);

--Se agrega un empleado.

--Segundo insert
--INSERT INTO empleados (nombre, edad, email, departamento_id)
--VALUES ('temp2', 30, 'dup@mail.com', 2);

--Este debería fallar porque:

--El campo email tiene UNIQUE.

--No puede haber dos iguales.

--Entonces ocurre:

--❌ Error → email duplicado.

--Después haces
--ROLLBACK;

--Esto cancela toda la transacción.

--Resultado final:

--Ninguno de los dos empleados se guarda.

--Ni temp1 ni temp2.

--Esto es muy importante porque evita datos inconsistentes.

--4️⃣ SAVEPOINT

--Esto es más avanzado.

--Permite crear puntos de control dentro de una transacción.

--Paso 1
--START TRANSACTION;

--Empieza la transacción.

--Paso 2
--UPDATE empleados
--SET edad = edad + 2
--WHERE departamento_id = 3;

--Aumenta la edad en 2 a los empleados del departamento 3.

--Paso 3
--SAVEPOINT sp1;

--Aquí creas un punto de guardado.

--Es como decir:

--👉 “si algo sale mal, puedo volver hasta aquí”.

---Paso 4
--UPDATE empleados
--SET edad = edad + 5
--WHERE departamento_id = 1;

--Ahora aumentas 5 años a empleados del departamento 1.

--Paso 5
--ROLLBACK TO sp1;

--Esto deshace solo el último UPDATE.

--Pero mantiene el cambio anterior.

--Entonces:

--departamento 3 → +2 años ✔

---departamento 1 → vuelve a como estaba ❌

--Paso 6
--COMMIT;

--Guardas definitivamente los cambios que quedaron.

--🔑 Resumen mental rápido

---Transacciones funcionan así:

--START TRANSACTION
  -- ↓
--haces cambios
  -- ↓
--COMMIT  → guardar
--ROLLBACK → cancelar

--Con SAVEPOINT puedes volver a un punto intermedio.