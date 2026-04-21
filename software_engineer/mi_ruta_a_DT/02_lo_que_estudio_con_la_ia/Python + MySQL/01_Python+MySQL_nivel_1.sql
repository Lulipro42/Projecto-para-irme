import mysql.connector

print("INICIANDO...")

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

        # EJERCICIO 1
        # Traer id, nombre, edad, email de personas
        # cursor.execute("SELECT id, nombre, edad, email FROM personas")
        # resultados = cursor.fetchall()
        # for id, nombre, edad, email in resultados:
        #     print(f"Id: {id}, Nombre: {nombre}, Edad: {edad}, Email: {email}")

        # EJERCICIO 2
        # Traer personas mayores o iguales a 18
        # cursor.execute("SELECT nombre, edad FROM personas WHERE edad >= 18")
        # resultados = cursor.fetchall()
        # for nombre, edad in resultados:
        #     print(f"Nombre: {nombre}, Edad: {edad}")

        # EJERCICIO 3
        # Traer edades y calcular suma + promedio en Python
        # cursor.execute("SELECT edad FROM personas")
        # resultados = cursor.fetchall()
        # suma_edades = 0
        # cantidad = 0
        # for (edad,) in resultados:
        #     suma_edades += edad
        #     cantidad += 1
        # if cantidad > 0:
        #     promedio = suma_edades / cantidad
        #     print(f"Suma: {suma_edades}")
        #     print(f"Promedio: {promedio}")

        # EJERCICIO 4
        # Insertar una persona nueva
        # cursor.execute(
        #     "INSERT INTO personas (nombre, edad, email) VALUES (%s, %s, %s)",
        #     ("Pedro", 29, "pedro@mail.com")
        # )
        # conexion.commit()
        # print("Persona insertada correctamente")

        # EJERCICIO 5
        # Actualizar email de una persona
        # cursor.execute(
        #     "UPDATE personas SET email = %s WHERE nombre = %s",
        #     ("nuevo_correo@mail.com", "Pedro")
        # )
        # conexion.commit()
        # print("Email actualizado correctamente")

        # EJERCICIO 6
        # Eliminar persona por nombre
        # cursor.execute(
        #     "DELETE FROM personas WHERE nombre = %s",
        #     ("Pedro",)
        # )
        # conexion.commit()
        # print("Persona eliminada correctamente")

        cursor.close()
        conexion.close()
        print("Conexion cerrada")

except Exception as e:
    print("Error:", e)




----------- EXPLICACION DE CADA EJERCICIO PARA PODER COMPRENDERLLO ---------------
# -------------------------------------------------
        # EJERCICIO 1: LECTURA DE DATOS (SELECT)
        # -------------------------------------------------
        Enviamos la orden de traer 4 columnas específicas de la tabla personas.
        --cursor.execute("SELECT id, nombre, edad, email FROM personas")
        fetchall() descarga toda la información y la guarda en la variable resultados.
        --resultados = cursor.fetchall()
        Usamos un bucle for para desempaquetar cada fila en variables individuales.
        --for id, nombre, edad, email in resultados:
        --     print(f"Id: {id}, Nombre: {nombre}, Edad: {edad}, Email: {email}")

        # -------------------------------------------------
        # EJERCICIO 2: FILTRADO POR CONDICIÓN (WHERE)
        # -------------------------------------------------
        Usamos el operador >= para que la base de datos solo nos mande los adultos.
        --cursor.execute("SELECT nombre, edad FROM personas WHERE edad >= 18")
        --resultados = cursor.fetchall()
        --for nombre, edad in resultados:
        --     print(f"Nombre: {nombre}, Edad: {edad}")

        # -------------------------------------------------
        # EJERCICIO 3: CÁLCULOS MATEMÁTICOS EN PYTHON
        # -------------------------------------------------
        Traemos solo la columna edad para procesarla fuera de la base de datos.
        cursor.execute("SELECT edad FROM personas")
        --resultados = cursor.fetchall()
        --suma_edades = 0
        --cantidad = 0
        Recorremos cada edad (vienen en tuplas de un elemento) y las acumulamos.
        --for (edad,) in resultados:
        --     suma_edades += edad
        --     cantidad += 1
        Verificamos que haya datos antes de dividir para evitar errores.
        --if cantidad > 0:
            -- promedio = suma_edades / cantidad
            -- print(f"Suma: {suma_edades} | Promedio: {promedio}")

        # -------------------------------------------------
        # EJERCICIO 4: INSERTAR NUEVOS REGISTROS (CREATE)
        # -------------------------------------------------
        Usamos %s para pasar los datos de forma segura (evita inyección SQL).
        --cursor.execute(
        --     "INSERT INTO personas (nombre, edad, email) VALUES (%s, %s, %s)",
        --     ("Pedro", 29, "pedro@mail.com")
        --)
        Importante: commit() guarda los cambios físicamente en el disco.
        --conexion.commit()
        --print("Persona insertada correctamente")

        # -------------------------------------------------
        # EJERCICIO 5: ACTUALIZAR DATOS (UPDATE)
        # -------------------------------------------------
        Cambiamos el email buscando a la persona por su nombre.
        --cursor.execute(
        --     "UPDATE personas SET email = %s WHERE nombre = %s",
        --     ("nuevo_correo@mail.com", "Pedro")
        -- )
        ---conexion.commit()
        --print("Email actualizado correctamente")

        # -------------------------------------------------
        # EJERCICIO 6: ELIMINAR REGISTROS (DELETE)
        # -------------------------------------------------
        Borramos la fila. Recordá que ("Pedro",) con coma al final indica una tupla.
        --cursor.execute(
        --     "DELETE FROM personas WHERE nombre = %s",
        --     ("Pedro",)
       -- )
       -- conexion.commit()
       -- print("Persona eliminada correctamente")

        Paso final: Cerramos el cursor y la conexión para no gastar recursos.
        --cursor.close()
        --conexion.close()
        --print("Conexion cerrada")