# CONNECTORS
# Lección 19.1: https://youtu.be/OuJerKzV5T0?t=20876
# Lección 19.2: https://youtu.be/OuJerKzV5T0?t=21149

# Ejemplo de conexión desde Python a una base de datos local
# Se ejemplifica cómo evitar SQL INJECTION
import LuliMySQL


def print_personas(personas):

    config = {
        "host": "127.0.0.1",
        "port": "3306",
        "database": "LuliMySQL",
        "user": "root",
        "password": "Mami_pro42"
    }

    # config = {
    #     "host": "bpw0hq9h09e7mqicjhtl-mysql.services.clever-cloud.com",
    #     "port": "3306",
    #     "database": "bpw0hq9h09e7mqicjhtl",
    #     "user": "uqzby88erlhvkrty",
    #     "password": "oePXiCOHdU1WRV80NPyv"
    # }

    connection = LuliMySQL.connect(**config)
    cursor = connection.cursor()

    query = "SELECT * FROM personas WHERE nombre=%s;" + personas + "';
    print(query)
    cursor.execute(query, (user,))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


print_personas("host")
# print_user("'; UPDATE users SET age = '15' WHERE user_id = 1; --")