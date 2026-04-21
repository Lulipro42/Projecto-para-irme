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

        # -------------------------------------------------
        # EJERCICIO 1
        # Verificar si una persona existe antes de insertarla
        # -------------------------------------------------
        cursor.execute(
            "SELECT COUNT(*) FROM personas WHERE email = %s",
            ("python_user@mail.com",)
        )
        existe = cursor.fetchone()[0]
        print(f"Existe esa persona? {existe}")

        # -------------------------------------------------
        # EJERCICIO 2
        # Insertar solo si no existe
        # -------------------------------------------------
        if existe == 0:
            cursor.execute(
                "INSERT INTO personas (nombre, edad, email) VALUES (%s, %s, %s)",
                ("python_user", 26, "python_user@mail.com")
            )
            conexion.commit()
            print("Persona insertada correctamente")
        else:
            print("La persona ya existe, no se inserto")

        # -------------------------------------------------
        # EJERCICIO 3
        # Buscar persona por nombre usando variable
        # -------------------------------------------------
        nombre_buscar = "Ana"

        cursor.execute(
            "SELECT id, nombre, edad, email FROM personas WHERE nombre = %s",
            (nombre_buscar,)
        )
        resultados = cursor.fetchall()

        for fila in resultados:
            print(f"Busqueda por nombre: {fila}")

        # -------------------------------------------------
        # EJERCICIO 4
        # Guardar filas en lista de diccionarios
        # -------------------------------------------------
        cursor.execute("SELECT id, nombre, edad, email FROM personas")
        resultados = cursor.fetchall()

        personas_lista = []

        for fila in resultados:
            persona = {
                "id": fila[0],
                "nombre": fila[1],
                "edad": fila[2],
                "email": fila[3]
            }
            personas_lista.append(persona)

        print("Lista de diccionarios:")
        for persona in personas_lista:
            print(persona)

        # -------------------------------------------------
        # EJERCICIO 5
        # Contar cuantas personas tienen email y cuantas no
        # -------------------------------------------------
        con_email = 0
        sin_email = 0

        for persona in personas_lista:
            if persona["email"] is None or persona["email"] == "":
                sin_email += 1
            else:
                con_email += 1

        print(f"Personas con email: {con_email}")
        print(f"Personas sin email: {sin_email}")

        # -------------------------------------------------
        # EJERCICIO 6
        # Promedio de edad desde Python
        # -------------------------------------------------
        suma_edades = 0
        cantidad = 0

        for persona in personas_lista:
            suma_edades += persona["edad"]
            cantidad += 1

        if cantidad > 0:
            promedio = suma_edades / cantidad
            print(f"Promedio de edad: {promedio}")
        else:
            print("No hay personas para calcular promedio")

        # -------------------------------------------------
        # EJERCICIO 7
        # Actualizar email solo si esta vacio o null
        # -------------------------------------------------
        cursor.execute(
            """
            UPDATE personas
            SET email = %s
            WHERE nombre = %s
            AND (email IS NULL OR email = '')
            """,
            ("ana_nueva@mail.com", "Ana")
        )
        conexion.commit()
        print("Update ejecutado")

        # -------------------------------------------------
        # EJERCICIO 8
        # Borrar una persona solo si existe
        # -------------------------------------------------
        nombre_borrar = "python_user"

        cursor.execute(
            "SELECT COUNT(*) FROM personas WHERE nombre = %s",
            (nombre_borrar,)
        )
        existe_para_borrar = cursor.fetchone()[0]

        if existe_para_borrar > 0:
            cursor.execute(
                "DELETE FROM personas WHERE nombre = %s",
                (nombre_borrar,)
            )
            conexion.commit()
            print("Persona eliminada correctamente")
        else:
            print("La persona no existe, no se elimino")

        cursor.close()
        conexion.close()
        print("Conexion cerrada")

except Exception as e:
    print("Error:", e)
