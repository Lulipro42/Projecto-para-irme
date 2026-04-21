import mysql.connector

print("INICIANDO ETL INCREMENTAL...")

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
        # Crear tabla destino incremental si no existe
        # -------------------------------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados_incremental (
                id_original INT PRIMARY KEY,
                nombre VARCHAR(50),
                edad INT,
                email VARCHAR(150),
                departamento_id INT,
                tipo_edad VARCHAR(20),
                estado_email VARCHAR(20)
            )
        """)
        conexion.commit()

        print("Tabla empleados_incremental lista")

        # -------------------------------------------------
        # EJERCICIO 2
        # Obtener el ultimo id cargado
        # -------------------------------------------------
        cursor.execute("SELECT MAX(id_original) FROM empleados_incremental")
        resultado = cursor.fetchone()

        ultimo_id = resultado[0]

        if ultimo_id is None:
            ultimo_id = 0

        print(f"Ultimo id cargado: {ultimo_id}")

        # -------------------------------------------------
        # EJERCICIO 3
        # Leer solo empleados nuevos
        # -------------------------------------------------
        cursor.execute(
            "SELECT id, nombre, edad, email, departamento_id FROM empleados WHERE id > %s",
            (ultimo_id,)
        )
        nuevos_empleados = cursor.fetchall()

        print(f"Empleados nuevos encontrados: {len(nuevos_empleados)}")

        # -------------------------------------------------
        # EJERCICIO 4
        # Pasar resultados a lista de diccionarios
        # -------------------------------------------------
        empleados_lista = []

        for fila in nuevos_empleados:
            empleado = {
                "id": fila[0],
                "nombre": fila[1],
                "edad": fila[2],
                "email": fila[3],
                "departamento_id": fila[4]
            }
            empleados_lista.append(empleado)

        print("Lista incremental armada")

        # -------------------------------------------------
        # EJERCICIO 5
        # Limpiar y transformar
        # -------------------------------------------------
        empleados_transformados = []

        for empleado in empleados_lista:
            if empleado["edad"] is None:
                continue

            if empleado["edad"] < 0:
                continue

            if empleado["email"] is None or empleado["email"] == "":
                empleado["email"] = "sin_email@demo.com"
                empleado["estado_email"] = "sin_email"
            else:
                empleado["estado_email"] = "con_email"

            if empleado["edad"] < 18:
                empleado["tipo_edad"] = "menor"
            else:
                empleado["tipo_edad"] = "adulto"

            empleados_transformados.append(empleado)

        print(f"Empleados transformados: {len(empleados_transformados)}")

        # -------------------------------------------------
        # EJERCICIO 6
        # Insertar solo nuevos registros en destino
        # -------------------------------------------------
        for empleado in empleados_transformados:
            cursor.execute("""
                INSERT INTO empleados_incremental
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
        print("Carga incremental completada")

        # -------------------------------------------------
        # EJERCICIO 7
        # Verificar resultado final
        # -------------------------------------------------
        cursor.execute("SELECT * FROM empleados_incremental ORDER BY id_original")
        verificacion = cursor.fetchall()

        print("\nDATOS EN empleados_incremental")
        for fila in verificacion:
            print(fila)

        # -------------------------------------------------
        # EJERCICIO 8
        # Resumen final
        # -------------------------------------------------
        print("\nRESUMEN FINAL")
        print(f"Ultimo id previo: {ultimo_id}")
        print(f"Nuevos leidos: {len(empleados_lista)}")
        print(f"Transformados: {len(empleados_transformados)}")
        print(f"Cargados: {len(empleados_transformados)}")

        cursor.close()
        conexion.close()
        print("\nConexion cerrada")

except Exception as e:
    print("Error:", e)




------------ EXPLICACION PAR PODER COMPRENDER ESTO ----------
import mysql.connector

print("INICIANDO ETL INCREMENTAL...")

try:
    -- Paso 1: Conectamos a la base de datos de trabajo.
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
        # EJERCICIO 1: CREAR TABLA DE DESTINO
        # -------------------------------------------------
        # Creamos una tabla especial para recibir solo los datos nuevos y transformados.
        # 'id_original' nos servirá para saber cuál fue el último que trajimos de la tabla fuente.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados_incremental (
                id_original INT PRIMARY KEY,
                nombre VARCHAR(50),
                edad INT,
                email VARCHAR(150),
                departamento_id INT,
                tipo_edad VARCHAR(20),
                estado_email VARCHAR(20)
            )
        """)
     --   conexion.commit()
      --  print("Tabla empleados_incremental lista")

        # -------------------------------------------------
        # EJERCICIO 2: BUSCAR EL PUNTO DE CORTE
        # -------------------------------------------------
        # Buscamos el ID más alto que ya tenemos guardado en nuestra tabla de destino.
        cursor.execute("SELECT MAX(id_original) FROM empleados_incremental")
        resultado = cursor.fetchone()
        ultimo_id = resultado[0]

        # Si la tabla está vacía (es la primera vez), empezamos desde el ID 0.
       -- if ultimo_id is None:
         --   ultimo_id = 0
        --print(f"Ultimo id cargado: {ultimo_id}")

        # -------------------------------------------------
        # EJERCICIO 3: EXTRACCIÓN INCREMENTAL
        # -------------------------------------------------
       # Solo traemos los empleados cuyo ID sea mayor al último que ya procesamos.
        # Esto ahorra muchísima memoria y tiempo de procesamiento.
        #cursor.execute(
        -    "SELECT id, nombre, edad, email, departamento_id FROM empleados WHERE id > %s",
       -     (ultimo_id,)
       - )
        -nuevos_empleados = cursor.fetchall()
       - print(f"Empleados nuevos encontrados: {len(nuevos_empleados)}")

        # -------------------------------------------------
        # EJERCICIO 4: PASAR A ESTRUCTURA DE DICCIONARIO
        # -------------------------------------------------
        # Convertimos las filas en diccionarios para manipular los datos más fácilmente.
       - empleados_lista = []
       - for fila in nuevos_empleados:
           - empleado = {
            -    "id": fila[0],
            -    "nombre": fila[1],
           -    "edad": fila[2],
            -    "email": fila[3],
           -     "departamento_id": fila[4]
           - }
            -empleados_lista.append(empleado)

        # -------------------------------------------------
        # EJERCICIO 5: TRANSFORMACIÓN Y LIMPIEZA
        # -------------------------------------------------
        # Aquí aplicamos reglas de negocio para "limpiar" los datos antes de guardarlos.
        -empleados_transformados = []
       -for empleado in empleados_lista:
            # Filtro de seguridad: Si la edad no existe o es negativa, ignoramos el registro.
           - if empleado["edad"] is None or empleado["edad"] < 0:
            --    continue

            # Estandarización: Si no tiene email, le asignamos uno por defecto.
            -if empleado["email"] is None or empleado["email"] == "":
            -    empleado["email"] = "sin_email@demo.com"
           -     empleado["estado_email"] = "sin_email"
           - else:
           -     empleado["estado_email"] = "con_email"

            # Clasificación: Creamos una nueva columna basada en la edad.
           - if empleado["edad"] < 18:
           -     empleado["tipo_edad"] = "menor"
           - else:
           -     empleado["tipo_edad"] = "adulto"

           - empleados_transformados.append(empleado)

        # -------------------------------------------------
        # EJERCICIO 6: CARGA FINAL (LOAD)
        # -------------------------------------------------
        # Insertamos los datos ya limpios y clasificados en la tabla incremental.
        --for empleado in empleados_transformados:
            cursor.execute("""
              INSERT INTO empleados_incremental 
                (id_original, nombre, edad, email, departamento_id, tipo_edad, estado_email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
               -- empleado["id"],
               --empleado["nombre"],
               -- empleado["edad"],
               -- empleado["email"],
               -- empleado["departamento_id"],
              --  empleado["tipo_edad"],
              --  empleado["estado_email"]
          --  ))
       -- conexion.commit()
       -- print("Carga incremental completada")

        # -------------------------------------------------
        # EJERCICIO 7: VERIFICACIÓN
        # -------------------------------------------------
        # Consultamos la tabla de destino para confirmar que todo se guardó bien.
        --cursor.execute("SELECT * FROM empleados_incremental ORDER BY id_original")
        --verificacion = cursor.fetchall()
        --for fila in verificacion:
            print(fila)

        # -------------------------------------------------
        # EJERCICIO 8: RESUMEN DE EJECUCIÓN
        # -------------------------------------------------
        # Mostramos métricas finales para el control del ingeniero de datos.
        --print("\n--- RESUMEN FINAL ---")
        --print(f"Punto de partida (ID): {ultimo_id}")
        --print(f"Nuevos leídos: {len(empleados_lista)}")
        --print(f"Registros exitosos: {len(empleados_transformados)}")

        --cursor.close()
        --conexion.close()

--except Exception as e:
    # Atrapamos cualquier error de conexión o de lógica de Python.
    --print("Error detectado en el proceso:", e)