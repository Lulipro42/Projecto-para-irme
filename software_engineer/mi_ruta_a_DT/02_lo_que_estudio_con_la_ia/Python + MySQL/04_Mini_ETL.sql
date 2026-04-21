# MINI ETL: leer -> limpiar -> transformar -> cargar

import mysql.connector

print("INICIANDO MINI ETL...")

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mami_pro42",
        database="camino a dt 2"
    )

    if conexion.is_connected():
        print("Conectado a MySQL correctamente")

        cursor = conexion.cursor()

        # -------------------------------------------------
        # EJERCICIO 1
        # Leer empleados desde MySQL
        # -------------------------------------------------
        cursor.execute("SELECT id, nombre, edad, email, departamento_id FROM empleados")
        resultados = cursor.fetchall()

        empleados = []

        for fila in resultados:
            empleado = {
                "id": fila[0],
                "nombre": fila[1],
                "edad": fila[2],
                "email": fila[3],
                "departamento_id": fila[4]
            }
            empleados.append(empleado)

        print("\nEMPLEADOS LEIDOS DESDE MYSQL")
        for empleado in empleados:
            print(empleado)

        # -------------------------------------------------
        # EJERCICIO 2
        # Limpiar datos
        # -------------------------------------------------
        empleados_limpios = []

        for empleado in empleados:
            if empleado["edad"] is None:
                continue

            if empleado["edad"] < 0:
                continue

            if empleado["email"] is None or empleado["email"] == "":
                empleado["email"] = "sin_email@demo.com"

            empleados_limpios.append(empleado)

        print("\nEMPLEADOS LIMPIOS")
        for empleado in empleados_limpios:
            print(empleado)

        # -------------------------------------------------
        # EJERCICIO 3
        # Transformar datos
        # -------------------------------------------------
        for empleado in empleados_limpios:
            if empleado["edad"] < 18:
                empleado["tipo_edad"] = "menor"
            else:
                empleado["tipo_edad"] = "adulto"

            if empleado["email"] == "sin_email@demo.com":
                empleado["estado_email"] = "sin_email"
            else:
                empleado["estado_email"] = "con_email"

        print("\nEMPLEADOS TRANSFORMADOS")
        for empleado in empleados_limpios:
            print(empleado)

        # -------------------------------------------------
        # EJERCICIO 4
        # Crear tabla destino
        # -------------------------------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados_limpios (
                id_original INT,
                nombre VARCHAR(50),
                edad INT,
                email VARCHAR(150),
                departamento_id INT,
                tipo_edad VARCHAR(20),
                estado_email VARCHAR(20)
            )
        """)
        conexion.commit()

        print("\nTabla empleados_limpios creada o ya existente")

        # -------------------------------------------------
        # EJERCICIO 5
        # Vaciar tabla destino antes de recargar
        # -------------------------------------------------
        cursor.execute("DELETE FROM empleados_limpios")
        conexion.commit()

        print("Tabla empleados_limpios vaciada")

        # -------------------------------------------------
        # EJERCICIO 6
        # Cargar datos transformados
        # -------------------------------------------------
        for empleado in empleados_limpios:
            cursor.execute("""
                INSERT INTO empleados_limpios
                (id_original, nombre, edad, email, departamento_id, tipo_edad, estado_email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                empleado["id"],
                empleado["nombre"],
                empleado["edad"],
                empleado["email"],
                empleado["departamento_id"],
                empleado["tipo_edad"],
                empleado["estado_email"]
            ))

        conexion.commit()
        print("Datos cargados en empleados_limpios")

        # -------------------------------------------------
        # EJERCICIO 7
        # Verificar datos cargados
        # -------------------------------------------------
        cursor.execute("SELECT * FROM empleados_limpios")
        verificacion = cursor.fetchall()

        print("\nDATOS CARGADOS EN empleados_limpios")
        for fila in verificacion:
            print(fila)

        # -------------------------------------------------
        # EJERCICIO 8
        # Resumen final en Python
        # -------------------------------------------------
        conteo_tipo_edad = {}
        conteo_estado_email = {}

        for empleado in empleados_limpios:
            tipo = empleado["tipo_edad"]
            estado = empleado["estado_email"]

            if tipo in conteo_tipo_edad:
                conteo_tipo_edad[tipo] += 1
            else:
                conteo_tipo_edad[tipo] = 1

            if estado in conteo_estado_email:
                conteo_estado_email[estado] += 1
            else:
                conteo_estado_email[estado] = 1

        print("\nRESUMEN FINAL")
        print("Conteo por tipo_edad:")
        print(conteo_tipo_edad)

        print("Conteo por estado_email:")
        print(conteo_estado_email)

        cursor.close()
        conexion.close()
        print("\nConexion cerrada")

except Exception as e:
    print("Error:", e)


------------ RESPASO -------------------
# =================================================
# PIPELINE DE DATOS COMPLETO (ETL + ANALYTICS)
# =================================================

# -------------------------------------------------
# EJERCICIO 1: EXTRACCIÓN (EXTRAER)
# -------------------------------------------------
# Traemos la información cruda desde la tabla original de MySQL.
cursor.execute("SELECT id, nombre, edad, email, departamento_id FROM empleados")
resultados = cursor.fetchall()

empleados = []

# Convertimos cada fila (tupla) en un diccionario para poder trabajar con nombres.
--for fila in resultados:
    empleado = {
        "id": fila[0],
        "nombre": fila[1],
        "edad": fila[2],
        "email": fila[3],
        "departamento_id": fila[4]
    }
    empleados.append(empleado)

print("\nEMPLEADOS LEIDOS DESDE MYSQL")
for empleado in empleados:
    print(empleado)

# -------------------------------------------------
# EJERCICIO 2: LIMPIEZA DE DATOS (DATA CLEANING)
# -------------------------------------------------
#  Un Data Engineer nunca confía en la calidad de los datos de origen.
empleados_limpios = []

for empleado in empleados:
    #  El 'continue' salta al siguiente si la edad es nula o negativa (datos basura).
    if empleado["edad"] is None:
        continue

    if empleado["edad"] < 0:
        continue

    #  Si no hay email, le ponemos uno por defecto para que no rompa futuros procesos.
    if empleado["email"] is None or empleado["email"] == "":
        empleado["email"] = "sin_email@demo.com"

    empleados_limpios.append(empleado)

print("\nEMPLEADOS LIMPIOS")
for empleado in empleados_limpios:
    print(empleado)

# -------------------------------------------------
# EJERCICIO 3: TRANSFORMACIÓN (AGREGAR VALOR)
# -------------------------------------------------
#  Aquí creamos "Categorías" nuevas que no existían originalmente.
for empleado in empleados_limpios:
    #  Clasificamos por rango de edad para que sea más fácil de analizar después.
    if empleado["edad"] < 18:
        empleado["tipo_edad"] = "menor"
    else:
        empleado["tipo_edad"] = "adulto"

    #  Etiquetamos el estado del email para saber qué datos son reales y cuáles pusimos nosotros.
    if empleado["email"] == "sin_email@demo.com":
        empleado["estado_email"] = "sin_email"
    else:
        empleado["estado_email"] = "con_email"

print("\nEMPLEADOS TRANSFORMADOS")
for empleado in empleados_limpios:
    print(empleado)

# -------------------------------------------------
# EJERCICIO 4 Y 5: PREPARACIÓN DEL DESTINO
# -------------------------------------------------
#   Creamos la tabla donde guardaremos los datos ya procesados (con las nuevas columnas).
cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados_limpios (
        id_original INT,
        nombre VARCHAR(50),
        edad INT,
        email VARCHAR(150),
        departamento_id INT,
        tipo_edad VARCHAR(20),
        estado_email VARCHAR(20)
    )
""")
conexion.commit()

print("\nTabla empleados_limpios creada o ya existente")

#  Vaciamos la tabla para hacer una "carga completa" (Full Load) limpia.
cursor.execute("DELETE FROM empleados_limpios")
conexion.commit()

print("Tabla empleados_limpios vaciada")

# -------------------------------------------------
# EJERCICIO 6: CARGA (LOAD)
# -------------------------------------------------
#  Insertamos los diccionarios ya transformados en la nueva tabla de MySQL.
for empleado in empleados_limpios:
    cursor.execute("""
        INSERT INTO empleados_limpios
        (id_original, nombre, edad, email, departamento_id, tipo_edad, estado_email)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        empleado["id"],
        empleado["nombre"],
        empleado["edad"],
        empleado["email"],
        empleado["departamento_id"],
        empleado["tipo_edad"],
        empleado["estado_email"]
    ))

conexion.commit()
print("Datos cargados en empleados_limpios")

# -------------------------------------------------
# EJERCICIO 7: VERIFICACIÓN FINAL
# -------------------------------------------------
#  Consultamos la base de datos para estar 100% seguros de que se guardó bien.
cursor.execute("SELECT * FROM empleados_limpios")
verificacion = cursor.fetchall()

print("\nDATOS CARGADOS EN empleados_limpios")
for fila in verificacion:
    print(fila)

# -------------------------------------------------
# EJERCICIO 8: RESUMEN ANALÍTICO (EL VALOR DEL NEGOCIO)
# -------------------------------------------------
#  Usamos la lógica de "cajas" (diccionarios) que aprendiste antes para contar.
conteo_tipo_edad = {}
conteo_estado_email = {}

for empleado in empleados_limpios:
    tipo = empleado["tipo_edad"]
    estado = empleado["estado_email"]

    #  Lógica para contar cuántos menores/adultos hay.
    if tipo in conteo_tipo_edad:
        conteo_tipo_edad[tipo] += 1
    else:
        conteo_tipo_edad[tipo] = 1

    #   Lógica para contar cuántos tienen email o no.
    if estado in conteo_estado_email:
        conteo_estado_email[estado] += 1
    else:
        conteo_estado_email[estado] = 1

print("\nRESUMEN FINAL")
print("Conteo por tipo_edad:")
print(conteo_tipo_edad)

print("Conteo por estado_email:")
print(conteo_estado_email)