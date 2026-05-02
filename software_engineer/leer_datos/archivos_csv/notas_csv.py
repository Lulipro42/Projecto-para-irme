import csv

columnas = ["nombre", "posicion", "puntos"]

datos = [
    ["Pedro", "central", "120"],
    ["Ulises", "punta", "100"],
    ["Benja", "libero", "90"]
]

with open("voley_data.csv", "w", newline="") as archivo: # LA DIFERENCIA DE PONER newline="", le decís a Python: "No agregues saltos de línea por tu cuenta, dejá que la librería csv maneje el espacio entre filas". Esto hace que tus datos queden compactos y prolijos.
    escritor = csv.writer(archivo)
    
    escritor.writerow(columnas)
    
    escritor.writerows(datos)
    
print("Archivo CSV creado con exito. !Abirlo en VS Code para poder verlo!")
"""
NIVEL 7: EL DETECTOR DE CRACKS 🏆
-------------------------------
OBJETIVO: Leer 'voley_data.csv' y mostrar solo a los que tienen más de 90 puntos.

1. Abrir 'voley_data.csv' en modo lectura ("r").
2. Usar 'lector = csv.reader(archivo)'.
3. Usar 'next(lector)' para saltar los encabezados.
4. En el bucle 'for fila in lector:', convertir los puntos a entero: 'puntos = int(fila[2])'.
5. Si puntos > 90, imprimir: "Crack detectado: [fila[0]]".
"""

with open("voley_data.csv", "r", newline="") as lectura:
    lector = csv.reader(lectura)
    next(lector)
    
    for fila in lector:
        puntos = int(fila[2])
        if puntos > 90:
            print(f"Crack detectado: {fila[0]}")
            
"""
NIVEL 8: EL ACTUALIZADOR DE POSICIONES 🔄
-----------------------------------------
OBJETIVO: Crear un nuevo archivo cambiando una posición.

1. Crear una lista vacía llamada 'datos_actualizados'.
2. Leer el archivo original.
3. En el for, si 'fila[1]' es igual a "Punta", cambiarlo a "Capitán".
4. Guardar cada fila (modificada o no) en la lista 'datos_actualizados' usando .append(fila).
5. Al final, abrir un archivo NUEVO 'voley_final.csv' en modo escritura ("w") y usar .writerows(datos_actualizados).
"""

datos_actualizados = []

# 1. Leemos y modificamos
with open("voley_data.csv", "r", encoding="utf-8") as datos:
    lector = csv.reader(datos)
    encabezados = next(lector) # Guardamos los títulos
    datos_actualizados.append(encabezados) # Los metemos primeros en la lista
    
    for fila in lector:
        if fila[1] == "Punta": # Si la posición es Punta
            fila[1] = "Capitán" # La cambiamos
        
        datos_actualizados.append(fila) # ¡IMPORTANTE! Guardamos la fila en nuestra lista

# 2. Escribimos el nuevo archivo
with open("voley_final.csv", "w", newline="", encoding="utf-8") as actualizado:
    escrito2 = csv.writer(actualizado)
    escrito2.writerows(datos_actualizados) # Guardamos todo lo que juntamos

print("✅ Archivo 'voley_final.csv' creado con el Capitán actualizado.")



"""
NIVEL 9: EL CONTADOR DE EQUIPO 📊
---------------------------------
OBJETIVO: Contar cuántos jugadores hay en cada posición.

1. Crear dos variables: 'cuenta_puntas = 0' y 'cuenta_liberos = 0'.
2. Leer el CSV.
3. Usar un 'if' dentro del for:
   - Si fila[1] == "Punta", sumar 1 a su contador.
   - Si fila[1] == "Libero", sumar 1 al otro.
4. Imprimir: "El equipo tiene [X] Puntas y [Y] Liberos".
"""



cuenta_puntas = 0
cuenta_liberos = 0

# Ojo: corregí la extensión a .csv (pusiste .cvs) y el encoding
with open("voley_data.csv", "r", encoding="utf-8") as contar:
    lector4 = csv.reader(contar)
    next(lector4) # Siempre saltamos la cabecera
    
    for fila in lector4:
        # PREGUNTAMOS: ¿La posición es Punta?
        if fila[1] == "Punta":
            cuenta_puntas += 1 # SUMAMOS 1 al contador
            
        # PREGUNTAMOS: ¿La posición es Libero?
        elif fila[1] == "Libero":
            cuenta_liberos += 1 # SUMAMOS 1 al contador
            
print(f"El equipo tiene {cuenta_puntas} Puntas y {cuenta_liberos} Liberos")