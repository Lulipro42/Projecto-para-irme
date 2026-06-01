import mysql.connector
from datetime import datetime
import pandas as pd

# Importamos pandas con el alias 'pd' (es el estándar en la industria

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
    
       
        
        cursor.close()
        conexion.close()

except Exception as e:
    print("Error:", e)
    