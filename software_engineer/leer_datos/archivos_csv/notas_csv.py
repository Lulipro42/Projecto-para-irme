import csv

columnas = ["nombre", "posicion", "puntos"]

datos = [
    ["Pedro", "central", "120"],
    ["Ulises", "punta", "100"],
    ["Benja", "libero", "90"],
    ["Mauro", "punta", "50"]
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


"""
EJERCICIO:
1. Pedir al usuario que ingrese un nombre por teclado usando input().
2. Abrir 'voley_data.csv' en modo lectura.
3. Recorrer el archivo y comparar: si fila[0] es igual al nombre ingresado.
4. Si lo encuentra, imprimir: "Jugador: [nombre], Posición: [posicion], Puntos: [puntos]".
5. Si termina el bucle y no lo encontró, avisar: "Jugador no encontrado".
"""


ingresar_algo = input("Por favor ingrese su nombre: ")
encontrado = False  # Esta es nuestra "bandera" o testigo

with open("voley_data.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)
    
    for fila in lector:
        # COMPARACIÓN: ¿El nombre en la columna 0 es igual al que ingresó el usuario?
        if fila[0] == ingresar_algo:
            print(f"Jugador: {fila[0]}, Posicion: {fila[1]}, Puntos: {fila[2]}")
            encontrado = True # Si lo encontramos, avisamos al testigo
            break # Cortamos el bucle porque ya lo encontramos

# Fuera del for, preguntamos: ¿El testigo sigue en False?
if encontrado == False:
    print("❌ Jugador no encontrado")
    
"""
EJERCICIO:
1. Crear dos variables: 'suma_puntos = 0' y 'cantidad_jugadores = 0'.
2. Abrir 'voley_data.csv'.
3. En el for (saltando la cabecera), sumar el valor de fila[2] a 'suma_puntos'.
   (No te olvides del int() ).
4. Sumar 1 a 'cantidad_jugadores' en cada vuelta.
5. Al final, calcular: promedio = suma_puntos / cantidad_jugadores.
6. Imprimir el resultado.
"""


suma_puntos = 0
cantidad_jugadores = 0

with open("voley_data.csv", "r", encoding="utf-8") as sumar:
    leer = csv.reader(sumar)
    next(leer) # Saltamos los títulos
    
    for fila in leer:
        # 1. Convertimos el texto a número y lo sumamos al balde
        puntos_del_jugador = int(fila[2]) 
        suma_puntos += puntos_del_jugador 
        
        # 2. Contamos que pasó un jugador más
        cantidad_jugadores += 1

# 3. Fuera del bucle, cuando ya tenemos los totales, dividimos
if cantidad_jugadores > 0:
    promedio = suma_puntos / cantidad_jugadores
    print(f"Total de puntos: {suma_puntos}")
    print(f"Cantidad de jugadores: {cantidad_jugadores}")
    print(f"El promedio de puntos del equipo es: {promedio}")
    

"""
EJERCICIO:
1. Crear una lista 'datos_limpios'.
2. Leer 'voley_data.csv'.
3. Para cada fila, transformar el nombre a MAYÚSCULAS usando .upper().
4. Asegurarse de que no haya espacios de más usando .strip().
5. Guardar las filas modificadas en la lista.
6. Crear un nuevo archivo 'voley_limpio.csv' con estos datos.
"""


datos_limpios = []

with open("voley_data.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezados = next(lector) # Guardamos los títulos
    datos_limpios.append(encabezados) # Los títulos también van a la lista limpia
    
    for fila in lector:
        # fila[0] es el nombre. Lo limpiamos:
        nombre_limpio = fila[0].upper().strip()
        
        # Reemplazamos el nombre original por el limpio en la lista 'fila'
        fila[0] = nombre_limpio
        
        # Guardamos la fila entera ya modificada en nuestra lista nueva
      


# Ahora escribimos el archivo nuevo con los datos relucientes
with open("voley_limpio.csv", "w", newline="", encoding="utf-8") as archivo_nuevo:
    escritor = csv.writer(archivo_nuevo)
    escritor.writerows(datos_limpios)

print("✨ Archivo 'voley_limpio.csv' creado con éxito!")


"""
EJERCICIO:
1. Crear una lista 'nombres_vistos = []' y 'datos_unicos = []'.
2. Leer 'voley_data.csv'.
3. Para cada fila, preguntar: ¿El nombre (fila[0]) ya está en 'nombres_vistos'?
4. Si NO está:
   - Agregarlo a 'nombres_vistos'.
   - Agregarlo a 'datos_unicos'.
5. Guardar 'datos_unicos' en un archivo nuevo 'voley_sin_repetidos.csv'.
"""

nombres_vistos = []
datos_unicos = []

with open("voley_data.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    datos_unicos.append(encabezado)
    
    for fila in lector:
        nombre = fila[0]
        
        if nombre not in nombres_vistos:
            nombres_vistos.append(nombre)
            
            datos_unicos.append(fila)
            


with open("voley_sin_repetidos.csv", "w", newline="", encoding="utf-8") as salida:
    escritor = csv.writer(salida)
    escritor.writerows(datos_unicos)
    
    print("✅ Filtro terminado. ¡Repetidos eliminados!")
    
    
"""
EJERCICIO:
1. Leer 'voley_data.csv'.
2. Crear la lista 'seleccion_especial'.
3. Usar un IF con 'and': 
   Si fila[1] == "Libero" AND int(fila[2]) > 80.
4. Guardar a esos elegidos en 'liberos_pro.csv'.
"""

seleccion_especial = []

with open("voley_data.csv", "r", newline="") as leer:
    lector = csv.reader(leer)
    encabezados = next(lector)
    
    for fila in lector:
        if fila[1] == "Liebro" and int(fila[2]) > 80:
            seleccion_especial.append(fila)

# 4. Guardamos el resultado en un nuevo CSV
with open("liberos_pro.csv", "w", newline="", encoding="utf-8") as salida:
    escritor = csv.writer(salida)
    escritor.writerows(seleccion_especial)

print(f"✅ Se encontraron {len(seleccion_especial) - 1} Líberos PRO.")


"""
1. Pedir al usuario: posicion_buscada = input("¿Qué posición querés exportar?: ")
2. Leer 'voley_data.csv'.
3. Crear una lista 'resultados'.
4. Si fila[1].lower() == posicion_buscada.lower() (para que no importe si escribe en mayúsculas), guardarlo.
5. Guardar el resultado en 'voley_posicion.csv'.
"""



posicion_buscada = input("¿Qué posición buscás? ")
resultado = [] # Esta es tu "bolsa" donde vas a guardar los encontrados

with open("voley_data.csv", "r", encoding="utf-8") as leer:
    lector = csv.reader(leer)
    encabezado = next(lector)
    
    for fila in lector:
        # Comparamos la columna 1 (posición) con lo que pidió el usuario
        if fila[1].lower() == posicion_buscada.lower():
            resultado.append(fila) # Si coincide, lo guardamos en la bolsa

# Ahora guardamos esa "bolsa" en un archivo nuevo
with open("voley_posicion.csv", "w", newline="", encoding="utf-8") as salida:
    escritor = csv.writer(salida)
    escritor.writerow(encabezado) # No te olvides de poner los títulos arriba
    escritor.writerows(resultado)

print(f"✅ Se exportaron {len(resultado)} jugadores de la posición {posicion_buscada}.")


"""
1. Leer 'voley_data.csv' y guardar todos los datos en una lista (sin los encabezados).
2. Investigar cómo usar .sort() o sorted() en Python para ordenar la lista por la columna de puntos.
   Pista: sorted(lista, key=lambda x: int(x[2]), reverse=True)
3. Imprimir los nombres de los primeros 3 de la lista ordenada.
"""

with open("voley_data.csv", "r", newline="") as leer:
    lector = csv.reader(leer)
    next(lector) # Saltamos encabezados
    datos = list(lector) # Convertimos el lector en una lista real

# Opción 1: Usando sorted() (Crea una nueva lista, no toca la original)
lista_ordenada = sorted(datos, key=lambda x: int(x[2]), reverse=True)

# Opción 2: Usando .sort() (Modifica la lista 'datos' directamente)
datos.sort(key=lambda x: int(x[2]), reverse=True)

print("--- TOP 3 JUGADORES ---")
for i in range(3):
    print(f"{i+1}. {lista_ordenada[i][0]} con {lista_ordenada[i][2]} puntos")
    
    
"""
1. Leer 'voley_data.csv'.
2. Crear la lista 'datos_validos'.
3. En el for, verificar: 'if len(fila) == 3 and fila[0] != ""'.
4. Si la fila tiene las 3 columnas y el nombre no está vacío, guardarla.
5. Imprimir cuántas filas "basura" eliminaste.
"""
datos_validos = []
filas_basura = 0

with open("voley_data.csv", "r", newline="") as leer:
    lector = csv.reader(leer)
    encabezado = next(lector)
    datos_validos.append(encabezado)
    
    for fila in lector:
        if len(fila) == 3 and fila[0] != "":
            datos_validos.append(fila)
        else:
            filas_basura += 1

print(f"✅ Limpieza completada. Se eliminaron {filas_basura} filas basura.")

"""
1. Calcular: Total de jugadores, Promedio de puntos y quién es el que más puntos tiene.
2. Abrir un archivo llamado 'reporte_final.txt' en modo escritura ('w').
3. Escribir adentro un párrafo que resuma todo: 
   "El equipo tiene X jugadores. El promedio es Y y el mejor es Z."
"""
suma_puntos = 0
cantidad_jugadores = 0
mejor_jugador = ""
max_puntos = -1

with open("voley_data.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)
    
    for fila in lector:
        nombre = fila[0]
        puntos = int(fila[2])
        
        suma_puntos += puntos
        cantidad_jugadores += 1
        
        if puntos > max_puntos:
            max_puntos = puntos
            mejor_jugador = nombre

if cantidad_jugadores > 0:
    promedio = suma_puntos / cantidad_jugadores
    
    with open("reporte_final.txt", "w", encoding="utf-8") as reporte:
        reporte.write(f"El equipo tiene {cantidad_jugadores} jugadores. "
                      f"El promedio es {promedio:.2f} y el mejor es {mejor_jugador}.")
    print("✅ Reporte generado en 'reporte_final.txt'")