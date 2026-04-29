"""
# Abrimos en modo 'r' (read/lectura)
archivo = open('asistencia_voley.txt', 'r', encoding="utf-8")

# Leemos el contenido
contenido = archivo.read() 

# ¡Imprimimos el contenido para verlo en la terminal!
print(contenido)

# Siempre cerramos el archivo al terminar
archivo.close()
"""

#with open('data2.txt', 'r') as archivo: #La instrucción with en Python (usada frecuentemente como with open(...)) sirve para gestionar el ciclo de vida de un archivo de forma segura, automática y concisa. Su propósito principal es abrir el archivo y garantizar que se cierre automáticamente una vez que se termina de leer, incluso si ocurre un error o excepción durante el proceso
#   lineas = archivo.readlines()
# print(lineas)
    
#or l in lineas:
#    print(l.replace('\n', ''))

#with open('data2.txt', 'r') as archivo:
#    contenido = archivo.read()
#    lineas = contenido.split('\n')
#    print(lineas)

#with open('data2.txt', 'r') as archivo:
#    contenido = archivo.read()
#    lineas = contenido.split('\n')
#    pos = archivo.tell()
#    print(pos)
#    print('El archivo tiene {0} caracteres de longitud'.format(pos))

#with open('data2.txt', 'r') as archivo:
#    siguentes4 = archivo.read(7)
#    print(siguientes4)

#with open('data2.txt', 'r') as archivo:
#    print(type(archivo.read()))
    
#with open('data2.txt', 'rb') as archivo2:
#    print(type(archivo2.read()))

#with open('data3.txt', 'a') as archivo:
#    archivo.write('Oscar\nAlejandro\nFlavio123231')





# 1. Pedimos datos al usuario
problema = input("¿Qué problema tiene el usuario?: ")
prioridad = input("¿Es prioridad Alta, Media o Baja?: ")

# 2. Guardamos los datos en el archivo
# Usamos "a" (append) para que los tickets se vayan acumulando uno abajo del otro
with open("registro_tickets.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"TICKET: {problema} | PRIORIDAD: {prioridad}\n")

print("\n--- ✅ TICKET GUARDADO ---")

# 3. AHORA: Vamos a leer el archivo para contar cuántos tickets tenemos
with open("registro_tickets.txt", "r", encoding="utf-8") as lectura:
    todas_las_lineas = lectura.readlines() # Esto mete cada línea en una lista
    cantidad = len(todas_las_lineas) # Contamos cuántos elementos tiene la lista

print(f"En total tenés {cantidad} tickets registrados en el sistema.")


"""
NIVEL 1: EL DIARIO DEL PROGRAMADOR ✍️
------------------------------------
OBJETIVO: Crear un sistema de registro de progreso diario.

1. Pedir al usuario mediante input() su nombre y qué aprendió hoy.
2. Abrir el archivo 'diario.txt' en modo "a" (append) para no borrar lo anterior.
3. Usar encoding="utf-8" para que soporte acentos.
4. Escribir una línea con el formato: "Nombre: [nombre] | Aprendizaje: [texto] \n".
5. Imprimir en consola: "✅ Registro guardado en el diario".
"""

username = input("Porfavor escriba su nombre:")
aprendisaje = input("Porfavor di que aprendiste hoy:")

with open("diario.txt", "a", encoding="utf-8") as diario:
    diario.write(f"Nombre:{username} | Aprendisaje: {aprendisaje}")

print("\n --- REGISTRO GUARDADO EN EL DIARIO ---")

"""
NIVEL 2: FILTRADO DE ASISTENCIA 🏐 (RUBRO DEPORTES)
-------------------------------------------------
OBJETIVO: Leer una lista y filtrar datos específicos.

1. Usar el archivo 'asistencia_voley.txt' que creaste antes.
2. Abrir el archivo en modo "r" (lectura).
3. Recorrer el archivo línea por línea con un bucle 'for'.
4. REGLA: Si la línea contiene el nombre "Ulises", imprimir: "⭐ El capitán está presente".
5. Si la línea contiene otro nombre, simplemente imprimir: "Jugador registrado: [nombre]".
"""
with open("asistencia_voley.txt", "r", encoding="utf-8") as lectura:
    for linea in lectura:
        linea = linea.strip()
        if "Ulises" in linea:
            print("El capitan esta abordo") 
        else:
            print(f"Jugador registrado: {linea}")
            


"""
NIVEL 3: EL PROCESADOR DE DATOS ⚙️ (DATA ENGINEERING)
----------------------------------------------------
OBJETIVO: Leer de un archivo, transformar los datos y guardar en otro.

1. Leer el archivo 'datos_ingeniero.txt'.
2. Guardar todo su contenido en una variable usando .read().
3. Transformar ese contenido a MAYÚSCULAS usando el método de strings .upper().
4. Crear un archivo NUEVO llamado 'BACKUP_PROCESADO.txt' en modo "w".
5. Escribir el texto en mayúsculas dentro de este nuevo archivo.
6. Imprimir: "🚀 Proceso de transformación completado con éxito".
"""
# Este código crea el archivo que el ejercicio necesita leer
with open("datos_ingeniero.txt", "r", encoding="utf-8") as datos:
    # Guardamos todo el contenido en una variable
    contenido_original = datos.read()

# 2. Transformamos el texto (Procesamiento)
contenido_en_mayusculas = contenido_original.upper()

# 3. Creamos el archivo nuevo para GUARDAR el resultado
with open("BACKUP_PROCESADO.txt", "w", encoding="utf-8") as backup:
    backup.write(contenido_en_mayusculas)

print("🚀 Proceso de transformación completado con éxito")


"""
NIVEL 4: EL BUSCADOR DE PALABRAS 🔍
------------------------------------
OBJETIVO: Contar cuántas veces mencionás algo en tus archivos.

1. Pedir con input() qué palabra querés buscar (ej: "Python" o "Japón").
2. Abrir 'diario.txt' o 'datos_ingeniero.txt' en modo lectura ("r").
3. Leer todo el contenido con .read().
4. Usar el método .count(palabra) para saber cuántas veces aparece.
5. Imprimir el resultado: "Se encontró la palabra [X] veces".
"""

palabras_num = input("Dime que palabras deseas buscar y contaremos cuantas veces aparece:")

with open("diario.txt", "r", encoding="utf-8") as buscar:
    contenido = buscar.read()

    total = contenido.count(palabras_num)
    
print(f"se encontro la palabra{palabras_num} un total de: {total}veces")

"""
NIVEL 5: EL CENSURADOR DE TEXTO 🚫
-----------------------------------------------------------
OBJETIVO: Limpiar archivos de palabras que no querés que aparezcan.

1. Crear (o leer) un archivo llamado 'mensaje.txt' con una frase.
2. Leer el contenido y usar el método .replace("palabra_vieja", "********").
3. Guardar el texto ya modificado en un archivo NUEVO llamado 'mensaje_limpio.txt'.
4. Imprimir: "✅ El archivo ha sido censurado con éxito".
"""
# 1. CREAR EL MENSAJE (Esto ya lo tenías bien)
with open("mensaje.txt", "w", encoding="utf-8") as frase:
    frase.write("El mensaje que dejo es que me voy a pasar dark souls pro sigma")

# 2. LEER Y REEMPLAZAR
with open("mensaje.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read() # Metemos el texto en el 'balde' (variable)
    
    # Reemplazamos "sigma" por asteriscos
    # (El replace siempre pide: "lo que está", "lo nuevo")
    contenido_censurado = contenido.replace("sigma", "*****")

# 3. GUARDAR EL RESULTADO
with open("mensaje_limpio.txt", "w", encoding="utf-8") as nuevo_archivo:
    nuevo_archivo.write(contenido_censurado)

print("✅ El archivo ha sido censurado. ¡Chau 'sigma'!")