# BLOQUE SIGUIENTE: Python + MySQL nivel 2
# Objetivo: leer empleados, calcular metricas y mostrar un reporte

import mysql.connector

print("INICIANDO REPORTE...")

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
        # Traer todos los empleados con su departamento
        # -------------------------------------------------
        cursor.execute("""
            SELECT e.id, e.nombre, e.edad, e.email, d.nombre
            FROM empleados e
            INNER JOIN departamentos d ON e.departamento_id = d.id
        """)
        resultados = cursor.fetchall()

        print("\nEMPLEADOS CON DEPARTAMENTO")
        for fila in resultados:
            print(fila)

        # -------------------------------------------------
        # EJERCICIO 2
        # Guardar resultados en lista de diccionarios
        # -------------------------------------------------
        empleados_lista = []

        for fila in resultados:
            empleado = {
                "id": fila[0],
                "nombre": fila[1],
                "edad": fila[2],
                "email": fila[3],
                "departamento": fila[4]
            }
            empleados_lista.append(empleado)

        print("\nLISTA DE DICCIONARIOS")
        for empleado in empleados_lista:
            print(empleado)

        # -------------------------------------------------
        # EJERCICIO 3
        # Contar cuantos empleados hay por departamento
        # -------------------------------------------------
        conteo_departamentos = {}

        for empleado in empleados_lista:
            depto = empleado["departamento"]

            if depto in conteo_departamentos:
                conteo_departamentos[depto] += 1
            else:
                conteo_departamentos[depto] = 1

        print("\nCANTIDAD DE EMPLEADOS POR DEPARTAMENTO")
        print(conteo_departamentos)

        # -------------------------------------------------
        # EJERCICIO 4
        # Calcular promedio de edad general
        # -------------------------------------------------
        suma_edades = 0
        cantidad = 0

        for empleado in empleados_lista:
            suma_edades += empleado["edad"]
            cantidad += 1

        if cantidad > 0:
            promedio_edad = suma_edades / cantidad
            print(f"\nPromedio general de edad: {promedio_edad}")
        else:
            print("\nNo hay empleados")

        # -------------------------------------------------
        # EJERCICIO 5
        # Calcular promedio de edad por departamento
        # -------------------------------------------------
        suma_por_departamento = {}
        cantidad_por_departamento = {}

        for empleado in empleados_lista:
            depto = empleado["departamento"]
            edad = empleado["edad"]

            if depto in suma_por_departamento:
                suma_por_departamento[depto] += edad
                cantidad_por_departamento[depto] += 1
            else:
                suma_por_departamento[depto] = edad
                cantidad_por_departamento[depto] = 1

        print("\nPROMEDIO DE EDAD POR DEPARTAMENTO")
        for depto in suma_por_departamento:
            promedio = suma_por_departamento[depto] / cantidad_por_departamento[depto]
            print(f"{depto}: {promedio}")

        # -------------------------------------------------
        # EJERCICIO 6
        # Encontrar el empleado de mayor edad
        # -------------------------------------------------
        if len(empleados_lista) > 0:
            mayor = empleados_lista[0]

            for empleado in empleados_lista:
                if empleado["edad"] > mayor["edad"]:
                    mayor = empleado

            print("\nEMPLEADO DE MAYOR EDAD")
            print(mayor)

        # -------------------------------------------------
        # EJERCICIO 7
        # Mostrar empleados sin email
        # -------------------------------------------------
        print("\nEMPLEADOS SIN EMAIL")
        for empleado in empleados_lista:
            if empleado["email"] is None or empleado["email"] == "":
                print(empleado)

        # -------------------------------------------------
        # EJERCICIO 8
        # Insertar un reporte en una tabla nueva
        # -------------------------------------------------
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reporte_departamentos (
                id INT PRIMARY KEY AUTO_INCREMENT,
                departamento VARCHAR(50),
                cantidad_empleados INT,
                promedio_edad FLOAT
            )
        """)
        conexion.commit()

        for depto in suma_por_departamento:
            promedio = suma_por_departamento[depto] / cantidad_por_departamento[depto]
            cantidad_empleados = cantidad_por_departamento[depto]

            cursor.execute("""
                INSERT INTO reporte_departamentos (departamento, cantidad_empleados, promedio_edad)
                VALUES (%s, %s, %s)
            """, (depto, cantidad_empleados, promedio))

        conexion.commit()
        print("\nReporte insertado en la tabla reporte_departamentos")

        cursor.close()
        conexion.close()
        print("\nConexion cerrada")

except Exception as e:
    print("Error:", e)


# ==========================================
# REPORTE DE EMPLEADOS - NIVEL 2 (DATA ENG)
# ==========================================

--import mysql.connector

--print("--- INICIANDO PROCESO DE DATOS ---")

--try:
     Paso 1: Establecemos la conexión con la base de datos local.
     El 'host' es tu PC, 'user' es el administrador y 'database' es tu proyecto.
    --conexion = mysql.connector.connect(
       -- host="localhost",
       -- user="root",
       -- password="Mami_pro42",
       -- database="camino a dt 2"
   -- )

    --if conexion.is_connected():
       -- print("--- CONEXIÓN EXITOSA ---")
       -- cursor = conexion.cursor()

        # -------------------------------------------------
        # EJERCICIO 1: EXTRACCIÓN CON JOIN
        # -------------------------------------------------
        Usamos INNER JOIN para 'pegar' la tabla empleados con departamentos.
         Así en vez de un número de ID, traemos el nombre real del sector.
        query_extraccion = """
          --  SELECT e.id, e.nombre, e.edad, e.email, d.nombre
          --  FROM empleados e
         --   INNER JOIN departamentos d ON e.departamento_id = d.id
        """
        cursor.execute(query_extraccion)
        resultados = cursor.fetchall()

        # -------------------------------------------------
        # EJERCICIO 2: TRANSFORMACIÓN A DICCIONARIOS
        # -------------------------------------------------
        Las tuplas son difíciles de leer (fila[0], fila[1]).
         Los diccionarios nos permiten usar etiquetas como 'nombre' o 'edad'.
       -- empleados_lista = []
       -- for fila in resultados:
          --  empleado = {
             --   "id": fila[0],
             --   "nombre": fila[1],
            --    "edad": fila[2],
            --    "email": fila[3],
            --    "departamento": fila[4]
           -- }
             El .append() guarda cada diccionario dentro de nuestra lista maestra.
            empleados_lista.append(empleado)

        # -------------------------------------------------
        # EJERCICIO 3: CONTEO DINÁMICO
        # -------------------------------------------------
        Creamos un diccionario vacío para contar cuánta gente hay por sector.
        conteo_departamentos = {}
       -- for empleado in empleados_lista:
            depto = empleado["departamento"]
             Si el departamento ya está en el diccionario, sumamos 1.
           -- if depto in conteo_departamentos:
               conteo_departamentos[depto] += 1
             Si es la primera vez que aparece ese depto, lo iniciamos en 1.
           -- else:
                conteo_departamentos[depto] = 1

        # -------------------------------------------------
        # EJERCICIO 5: CÁLCULO DE PROMEDIOS POR GRUPO
        # -------------------------------------------------
        Necesitamos dos diccionarios: uno para sumar edades y otro para contar personas.
       -- suma_edades_depto = {}
       -- cantidad_personas_depto = {}

      --  for empleado in empleados_lista:
           -- depto = empleado["departamento"]
           -- edad = empleado["edad"]

          --  if depto in suma_edades_depto:
             --   suma_edades_depto[depto] += edad
             --   cantidad_personas_depto[depto] += 1
          --  else:
               -- suma_edades_depto[depto] = edad
              --  cantidad_personas_depto[depto] = 1

        # -------------------------------------------------
        # EJERCICIO 6: BÚSQUEDA DEL MÁXIMO (EL MÁS VIEJO)
        # -------------------------------------------------
        Algoritmo clásico: comparamos a todos contra una variable 'mayor'.
        --if len(empleados_lista) > 0:
           -- mayor_empleado = empleados_lista[0]
            --for emp in empleados_lista:
             --   if emp["edad"] > mayor_empleado["edad"]:
                    mayor_empleado = emp
           -- print(f"--- EL MÁS GRANDE ES: {mayor_empleado['nombre']} ---")

        # -------------------------------------------------
        # EJERCICIO 8: CARGA (EL CIERRE DEL ETL)
        # -------------------------------------------------
        Paso A: Creamos la tabla de reportes si no existe todavía.
        --cursor.execute("""
            ---CREATE TABLE IF NOT EXISTS reporte_departamentos (
                --id INT PRIMARY KEY AUTO_INCREMENT,
               -- departamento VARCHAR(50),
               --- cantidad_empleados INT,
               -- promedio_edad FLOAT
           -- )
        """)

        -- Paso B: Limpiamos datos viejos para que el reporte sea siempre nuevo.
        --cursor.execute("TRUNCATE TABLE reporte_departamentos")

        -- Paso C: Recorremos nuestros cálculos de Python e insertamos en MySQL.
        --for depto in suma_edades_depto:
            --promedio = suma_edades_depto[depto] / cantidad_personas_depto[depto]
            --cantidad = cantidad_personas_depto[depto]

            ---cursor.execute("""
                --INSERT INTO reporte_departamentos (departamento, cantidad_empleados, promedio_edad)
                --VALUES (%s, %s, %s)
            """, (depto, cantidad, promedio))

        -- Paso D: El 'commit' guarda los cambios en el disco duro.
        --conexion.commit()
        --print("--- REPORTE FINALIZADO Y GUARDADO EN DB ---")

        Paso E: Cerramos todo para liberar memoria de la PC.
        --cursor.close()
       ---- conexion.close()

--except Exception as e:
    Si hay un error de contraseña o de SQL, saltará este mensaje.
    --print(f"--- ERROR EN EL PROCESO: {e} ---")