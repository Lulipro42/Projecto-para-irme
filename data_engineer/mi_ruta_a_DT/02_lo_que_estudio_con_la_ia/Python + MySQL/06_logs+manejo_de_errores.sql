# =================================================
# PIPELINE DE DATOS CON SISTEMA DE AUDITORÍA (LOGS)
# =================================================

import mysql.connector
from datetime import datetime -- Importamos datetime para marcar la hora exacta de cada evento.

print("INICIANDO PIPELINE CON LOGS...")

try:
    -- Paso inicial: Conexión a la base de datos.
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
        # EJERCICIO 1: CREAR LA BITÁCORA (TABLA DE LOGS)
        # -------------------------------------------------
        #Creamos una tabla que funcionará como el "caja negra" de un avión.
        # 'fecha' usa DATETIME para saber cuándo ocurrió el evento.
        # 'etapa' nos dice en qué parte del código estábamos (inicio, limpieza, fin).
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs_etl (
                id INT PRIMARY KEY AUTO_INCREMENT,
                fecha DATETIME,
                etapa VARCHAR(50),
                mensaje VARCHAR(255)
            )
        """)
        conexion.commit()

        # -------------------------------------------------
        # EJERCICIO 2: LOG DE ARRANQUE
        # -------------------------------------------------
        # Registramos el primer hito: El motor del pipeline se encendió.
        cursor.execute("""
            INSERT INTO logs_etl (fecha, etapa, mensaje)
            VALUES (%s, %s, %s)
        """, (datetime.now(), "inicio", "El pipeline comenzo correctamente"))
        conexion.commit()

        # -------------------------------------------------
        # EJERCICIO 3: AUDITORÍA DE LECTURA (EXTRACT)
        # -------------------------------------------------
        # Leemos los datos de la tabla empleados.
        cursor.execute("SELECT id, nombre, edad, email, departamento_id FROM empleados")
        resultados = cursor.fetchall()

        # Guardamos un log informando cuántos registros logramos extraer.
        # Esto sirve para detectar si la fuente de datos se está quedando vacía.
        cursor.execute("""
            INSERT INTO logs_etl (fecha, etapa, mensaje)
            VALUES (%s, %s, %s)
        """, (datetime.now(), "lectura", f"Se leyeron {len(resultados)} empleados"))
        conexion.commit()

        # -------------------------------------------------
        # EJERCICIO 4: PROCESAMIENTO EN MEMORIA
        # -------------------------------------------------
        # Convertimos las tuplas de SQL en diccionarios de Python (más fáciles de usar).
        empleados = []
        for fila in resultados:
            empleado = {
                "id": fila[0], "nombre": fila[1], "edad": fila[2],
                "email": fila[3], "departamento_id": fila[4]
            }
            empleados.append(empleado)

        # -------------------------------------------------
        # EJERCICIO 5: LIMPIEZA Y LOG DE CALIDAD
        # -------------------------------------------------
        empleados_limpios = []
        for empleado in empleados:
            # Si no tiene edad, lo descartamos (Data Quality).
            if empleado["edad"] is None:
                continue
            # Si no tiene email, le ponemos uno genérico.
            if empleado["email"] is None or empleado["email"] == "":
                empleado["email"] = "sin_email@demo.com"
            empleados_limpios.append(empleado)

        # Anotamos en los logs cuántos empleados sobrevivieron a la limpieza.
        cursor.execute("""
            INSERT INTO logs_etl (fecha, etapa, mensaje)
            VALUES (%s, %s, %s)
        """, (datetime.now(), "limpieza", f"Quedaron {len(empleados_limpios)} empleados limpios"))
        conexion.commit()

        # -------------------------------------------------
        # EJERCICIO 6 Y 7: CIERRE DEL PROCESO
        # -------------------------------------------------
        print("\nRESUMEN")
        print(f"Leidos: {len(empleados)} | Limpios: {len(empleados_limpios)}")

        # Registramos el log de éxito final.
        cursor.execute("""
            INSERT INTO logs_etl (fecha, etapa, mensaje)
            VALUES (%s, %s, %s)
        """, (datetime.now(), "fin", "El pipeline termino correctamente"))
        conexion.commit()

        # -------------------------------------------------
        # EJERCICIO 8: CONSULTA DE LA BITÁCORA
        # -------------------------------------------------
        # Traemos los logs ordenados por el ID más reciente (DESC) para ver qué pasó.
        cursor.execute("SELECT * FROM logs_etl ORDER BY id DESC")
        logs = cursor.fetchall()

        print("\nLOGS REGISTRADOS EN LA BASE DE DATOS:")
        for log in logs:
            print(log)

        cursor.close()
        conexion.close()

except Exception as e:
    # Si el código falla, este print nos salva la vida avisando qué pasó.
    print("Error:", e)