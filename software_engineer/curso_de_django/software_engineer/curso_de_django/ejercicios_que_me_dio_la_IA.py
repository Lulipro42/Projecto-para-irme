### Ejercicios que me dio la IA ###

# EL primero ejercicio
mi_nombre = "Ulises"
mi_estatura = 1.77  # en metros
mi_edad = 17 # Años

print(f"Hola,mi nombre es {mi_nombre}, tengo {mi_edad} años y mido actualmente {mi_estatura} metros.")

# El segundo ejercicio

horas_estudiadas_hoy = 2 # horas
dias_de_la_semana_estudiar = 7 # días

total_horas_estudio_semana = horas_estudiadas_hoy * dias_de_la_semana_estudiar
print(f"Essta semana estudie al rededor de {total_horas_estudio_semana} horas.")

# El tercero ejercicio
numero = input("Ingresa un número: ")
numero = int(numero)
numero = int(input("Ingresa un número: "))
if numero > 10:
    print("El numero es mayor a 10")
else:
    print("El numero es menor o igual a 10")    
    
# El cuarto ejercicio
lista = [3, 21, 12, 5, 6]
print(f"Quiero mostrar el primero numero de la lista:{lista[0]}")
print(f"Quiero mostrar el ultimo numero de la lista:{lista[-1]}")

# El quinto ejercicio
lista_de_numeros = [10, 23, 45, 66, 12, 34]
for numero in lista_de_numeros: # El for sirve para repetir un bloque de código un número específico de veces.
    if numero % 2 == 0: # el if sirve para tomar decisiones en el código.
        print(f"{numero} es un número par.")
    else: # el else es la parte final de una estructura condicional if-else. y sirve para definir un bloque de código que se ejecutará cuando la condición del if sea falsa.
        print(f"{numero} es un número impar.")

# El sexto ejercicio
numeros = [2, 8, 10, 5, 23, 12, 67]
total = 20
for numero in numeros:
    total = total + numero

print(f"la suma total de todos los numeros es {total}")

# El séptimo ejercicio
numeros = [12, 42, 21, 5, 9, 2 ]
nueva_lista = []
for numero in numeros:
    if numero > 10:
        nueva_lista.append(numero)
print(f"La nueva lista con los números mayores a 10 es: {nueva_lista}")

# El octavo ejercicio
numeros = [12, 4, 52, 9, 19, 24, 3]
promedio = sum(numeros) / len(numeros)
print(f"El promedio de los números en la lista es: {promedio}")

# El noveno ejercicio
persona = {
    "nombre": "Ulises",
    "edad": 17,
    "calificaciones": [6,7,8,9,10],
    "estatura": 1.77
}
print(persona["nombre"])
print(persona["calificaciones"][3])
print(persona["edad"])
print(persona["estatura"])

# El décimo ejercicio
productos = {
    "producto1": "noteebook",
    "producto2": "smartphone",
    "producto3": "tablet",
    "stock": 50
    
    
}
print(f"nombre del producto es: {productos['producto1']}")
print(f"El stock que nos queda de las notebooks es de: {productos['stock']}")

# El undécimo ejercicio
numero = [-10]
numero = [5]
numero = [0]

def calcular_si_el_numero_es_positivo_o_negativo(numero):
    if numero > 0:
        return "el numero es positivo"
    elif numero < 0:
        return "el numero es negativo"
    else:
        return "el numero es cero"
print(calcular_si_el_numero_es_positivo_o_negativo(-10))
print(calcular_si_el_numero_es_positivo_o_negativo(5))
print(calcular_si_el_numero_es_positivo_o_negativo(0))

# El duodécimo ejercicio
lista_de_numeros = [4, 8, 15, 16, 23, 42]
def sumar_los_numeros_de_la_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
print(f"la suma completa de todos los numeros es:{sumar_los_numeros_de_la_lista(lista_de_numeros)}")

# El decimotercer ejercicio NIVEL 6
producto = {
    "nombre": "notebook",
    "precio": 1500,
    "stock": 0
}
def vender_productos(producto, cantidad):
    if cantidad <= producto["stock"]:
        producto["stock"] -= cantidad
        return f"Venta realizada. Stock restante: {producto['stock']}"
    elif cantidad > producto["stock"] and producto["stock"] > 0:
        return f"Solo quedan {producto['stock']} unidades en stock. No se puede completar la venta."
        
    else:
        return "No hay suficiente stock para completar la venta."
print(vender_productos(producto, 1))
# entender este CODIGO el DICCIONARIO(lo entiendo un 90%) la FUNCION (el producto es= un DICCIONARIO y la cantidad es= un NUMERO ENTERO estos son PARAMETROS) Condicion Clave (if cantidad <= producto["stock"]: esto lo que hace es que si la cantidad que quiero vender es menor o igual al stock disponible se realiza la venta y se actualiza el stock restante) el Return (La funcion lo que haces que .termina, .devuelve un resultado y no impreme nada en pantalla) el Else (bueno eso lo que hace es que si no se cumple el if se cumple el else ) 

# Mini ejercicios de Data Engineering
datos = [10, None, 25, "", 49, None, 5]
# Limpieza de datos: Eliminar valores nulos o vacíos
datos_limpios = [dato for dato in datos if dato is not None and dato != ""]
print(f"Datos limpios: {datos_limpios}") 
# if dato is not None and dato != "" esto lo que hace es que si el dato no es nulo y el dato no es una cadena vacía se agrega a la nueva lista datos_limpios y no se usa == porque eso es para comparar identidad y no para asignar
# y and dato != "" elimina strings vacíos de la lista original.
# Dato lo que queda se agrega a la nueva lista datos_limpios.

# Ejercicio para hacer sin ia
lista_de_numeros = [4, 8, 15, 16, 23, 42]
mayores_a_10 = []
for numero in lista_de_numeros:
    if numero > 10:
        mayores_a_10.append(numero)
        
print(f"Los números mayores a 10 son: {mayores_a_10}")

# Ejercicio para hacer
lista = [2, 12, 7, 20, 3, 15]
numeros_pares = []
for numero in lista:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f"Numeros pares en la lista: {numeros_pares}")

# Ejercicio para hacer
def devolver_numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero %2 == 0:
            pares.append(numero)
    return pares
lista_de_numeros = [3, 6, 9, 12, 15, 18]
print(devolver_numeros_pares(lista_de_numeros))

# Ejercicio para hacer
dato = [6, None, 18, "", 24, None, 30]
resultado = []
for datos in dato:
    if datos is None:
        continue
    if datos == "":
        continue
    if not isinstance(datos, int):
        continue
    if datos % 2 != 0:
        continue
    resultado.append(datos)
print(f"Datos limpios y pares: {resultado}")

# Ejercicio para hacer
usuarios = [
    {"nombre": "Ana", "edad": 28, "activo": True},
    {"nombre": "Luis", "edad": 34, "activo": False},
    {"nombre": "Marta", "edad": 22, "activo": True},
    {"nombre": "Carlos", "edad": 45, "activo": False}
]

usuarios_activos = []
for usuario in usuarios:
    if usuario["activo"] and usuario["edad"] >= 18:
        usuarios_activos.append(usuario["nombre"])
print(f"Usuarios activos mayores de edad: {usuarios_activos}")

# Ejercicio para hacer
usuarios = [
    {"nombre": "Ana", "edad": 28, "activo": True},
    {"nombre": "Luis", "edad": 34, "activo": False},
    {"nombre": "Marta", "edad": 22, "activo": True},
    {"nombre": "Carlos", "edad": 45, "activo": False}
]

total = 0
activos = 0
mayores = 0
activos_y_mayores = 0

for usuario in usuarios:
    total += 1

    if usuario["activo"]:
        activos += 1

    if usuario["edad"] >= 18:
        mayores += 1

    if usuario["activo"] and usuario["edad"] >= 18:
        activos_y_mayores += 1

print(f"Total de usuarios: {total}")
print(f"Usuarios activos: {activos}")
print(f"Usuarios mayores de edad: {mayores}")
print(f"Usuarios activos y mayores de edad: {activos_y_mayores}")

# Ejercicio para hacer
usuarios = [
    {"nombre": "Ana", "edad": 28, "activo": True},
    {"nombre": "Luis", "edad": 34, "activo": False},
    {"nombre": "Marta", "edad": 22, "activo": True},
    {"nombre": "Carlos", "edad": 45, "activo": False}
]

def calcular_estadisticas_usuarios(usuarios):
    total = 0
    activos = 0
    mayores = 0
    activos_y_mayores = 0

    for usuario in usuarios:
        total += 1

        if usuario["activo"]:
            activos += 1

        if usuario["edad"] >= 18:
            mayores += 1

        if usuario["activo"] and usuario["edad"] >= 18:
            activos_y_mayores += 1

    return {
        "total": total,
        "activos": activos,
        "mayores": mayores,
        "activos_y_mayores": activos_y_mayores
    }

# Ejercicio para hacer
usuarios_que_pagan = [
    {"nombre": "Ana", "edad": 28, "activo": True, "paga": True},
    {"nombre": "Luis", "edad": 34, "activo": True, "es activo pero no paga hace un mes": False, "debe hace un mes o mas": 1},
    {"nombre": "Marta", "edad": 22, "activo": False, "es activo pero paga": True},
    {"nombre": "Carlos", "edad": 45, "activo": False, "paga": False, "debe hace un mes o mas": 3}
]

def calcular_estadisticas_usuarios_que_pagan_o_deben_meses(usuarios):
    total = 0
    activos = 0
    mayores = 0
    activos_y_mayores = 0
    que_pagan = 0
    que_deben = 0
    
    for usuario in usuarios:
        total += 1
        if usuario["activo"]:
            activos += 1
        if usuario["edad"] >= 18:
            mayores += 1
        if usuario["activo"] and usuario["edad"] >= 18:
            activos_y_mayores += 1
        if usuario.get("paga"):
            que_pagan += 1
        if usuario.get("debe hace un mes o mas", 0) >= 1:
            que_deben += 1
    return {
        "total": total,
        "activos": activos,
        "mayores": mayores,
        "activos_y_mayores": activos_y_mayores,
        "que_pagan": que_pagan,
        "que_deben": que_deben
    }

# --- Nuevos Ejercicios de Data Engineering ---

# Ejercicio 16: Limpieza y Transformación de Datos Avanzada
# Tienes una lista de productos con datos inconsistentes.
# Tu tarea es limpiar y estandarizar esta lista.
# - Los precios deben ser números flotantes (float).
# - Las fechas deben estar en formato YYYY-MM-DD.
# - Si falta una clave, debe añadirse con un valor por defecto (ej: 'categoría' -> 'desconocida').
print("\n--- Ejercicio 16: Limpieza y Transformación Avanzada ---")
productos_sucios = [
    {"id": 1, "nombre": "Laptop", "precio": "1200.50", "fecha_registro": "2023/03/15"},
    {"id": 2, "nombre": "Mouse", "precio": 25, "fecha_registro": "18-04-2023"},
    {"id": 3, "nombre": "Teclado", "precio": "75.99", "fecha_registro": "2023-05-20", "categoría": "Periférico"},
    {"id": 4, "nombre": "Monitor", "precio": "300", "fecha_registro": "2023/01/01"}
]

from datetime import datetime
import json

def limpiar_productos(lista_productos):
    productos_limpios = []
    for producto in lista_productos:
        # Copiamos el diccionario para no modificar el original
        p_limpio = producto.copy()

        # 1. Limpiar y convertir precio a float
        if isinstance(p_limpio["precio"], str):
            p_limpio["precio"] = float(p_limpio["precio"])
        else:
            p_limpio["precio"] = float(p_limpio["precio"])

        # 2. Estandarizar fechas a YYYY-MM-DD
        fecha_str = p_limpio["fecha_registro"]
        try:
            # Intenta formato YYYY/MM/DD
            fecha_obj = datetime.strptime(fecha_str, '%Y/%m/%d')
        except ValueError:
            try:
                # Intenta formato DD-MM-YYYY
                fecha_obj = datetime.strptime(fecha_str, '%d-%m-%Y')
            except ValueError:
                # Asume que ya está en YYYY-MM-DD
                fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d')
        
        p_limpio["fecha_registro"] = fecha_obj.strftime('%Y-%m-%d')

        # 3. Añadir claves faltantes
        if "categoría" not in p_limpio:
            p_limpio["categoría"] = "desconocida"
            
        productos_limpios.append(p_limpio)
    return productos_limpios

productos_limpios = limpiar_productos(productos_sucios)
print(json.dumps(productos_limpios, indent=2))

### RAPASO DEVUELTA 
lista = [12, 5, 6, 52, 42, 8, 9, 21, 32]
numeros_mayores_a_10 = []
numeros_mayores_a_10_sumados = 0
for numero in lista:
    if numero > 10:
        numeros_mayores_a_10.append(numero)
        numeros_mayores_a_10_sumados += numero
print(f"Los numeros mayores a 10 son:{numeros_mayores_a_10} y los que se suman son: {numeros_mayores_a_10_sumados} ")


### SEWGUNDO EJERCICIO DE REPASO
dato = [10, None, 25, "", 40, "50", 8, None, 3]
resultado = []
for datos in dato:
    if datos is None:
        continue
    if datos == "":
        continue
    if not isinstance(datos, int):
        continue
    if datos <= 10 :
        continue
    resultado.append(datos)
print(f"Datos limpios y superiories a 10: {resultado}")

# Otro ejercicio para repasar
usuarios = [
    {"nombre": "Ana", "edad": 28, "activo": True},
    {"nombre": "Luis", "edad": 17, "activo": False},
    {"nombre": "Marta", "edad": 22, "activo": True},
    {"nombre": "Carlos", "edad": 45, "activo": False},
    {"nombre": "Elena", "edad": 13, "activo": True}
]
total_f = 0
activos_f = 0
mayores_f = 0
activos_y_mayores_f = 0
suma_edades_f = 0

for usuario in usuarios:
    total_f += 1
    suma_edades_f += usuario["edad"]

    if usuario["activo"]:
        activos_f += 1

    if usuario["edad"] >= 18:
        mayores_f += 1

    if usuario["activo"] and usuario["edad"] >= 18:
        activos_y_mayores_f += 1

if total_f > 0:
    promedio_edades = suma_edades_f / total_f
else:
    promedio_edades = 0

print(f"El total de personas registradas es: {total_f}")
print(f"El total de activos es: {activos_f}")
print(f"El total de personas mayores es: {mayores_f}")
print(f"El total de personas activas y mayores es: {activos_y_mayores_f}")
print(f"El promedio de edades es: {promedio_edades}")

# Otro ejercicio
lista = [5, 12, 7, 30,-12, 22, 1, 18]
def numero_mayor(lista):
    mayor = lista[0]
    for n in lista:
        if n > mayor:
            mayor = n
    return mayor
print(numero_mayor(lista))
def numero_menor(lista):
    menor = lista[0]
    for n in lista:
        if n < menor:
            menor = n
    return menor
print(numero_menor(lista))
def cantidad_de_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:
            contador += 1
    return contador
print(cantidad_de_pares(lista))
def suma_de_impares(lista):
    suma = 0
    for n in lista:
        if n % 2 != 0:
            suma += n
    return suma
print(suma_de_impares(lista))


# Otro repaso 
ventas = [
    {"producto": "Notebook", "precio": 1200, "cantidad": 2},
    {"producto": "Mouse", "precio": 25, "cantidad": 10},
    {"producto": "Teclado", "precio": 75, "cantidad": 4},
    {"producto": "Monitor", "precio": 300, "cantidad": 3},
]

ingreso_total = 0
max_ingreso = -1
producto_top = None

for venta in ventas:
    ingreso = venta["precio"] * venta["cantidad"]
    ingreso_total += ingreso

    if ingreso > max_ingreso:
        max_ingreso = ingreso
        producto_top = venta["producto"]

if len(ventas) > 0:
    promedio_ingreso = ingreso_total / len(ventas)
else:
    promedio_ingreso = 0

print(f"Ingreso total: {ingreso_total}")
print(f"Producto que genero mas ingreso: {producto_top} ({max_ingreso})")
print(f"Promedio de ingreso por producto: {promedio_ingreso}")






# Ejercicio 17: Escritura y Lectura de archivos CSV
# CSV (Comma-Separated Values) es un formato muy común para intercambiar datos.
# Tarea 1: Crea una función que tome la lista de `usuarios` y la guarde en un archivo llamado `usuarios.csv`.
# Tarea 2: Crea otra función que lea `usuarios.csv` y muestre los datos en la consola.
print("\n--- Ejercicio 17: Trabajando con archivos CSV ---")
import csv

def guardar_usuarios_csv(lista_usuarios, nombre_archivo):
    if not lista_usuarios:
        return
    
    cabeceras = lista_usuarios[0].keys()
    
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=cabeceras)
        
        escritor_csv.writeheader()
        escritor_csv.writerows(lista_usuarios)
    print(f"Datos guardados en {nombre_archivo}")

def leer_usuarios_csv(nombre_archivo):
    print(f"Leyendo datos desde {nombre_archivo}:")
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            print(dict(fila))

nombre_fichero_csv = "usuarios.csv"
guardar_usuarios_csv(usuarios, nombre_fichero_csv)
leer_usuarios_csv(nombre_fichero_csv)


# Ejercicio 18: Consumo de una API REST
# Tarea: Usa la librería `requests` para obtener datos de la API pública JSONPlaceholder.
# Obtén la lista de "todos" (tareas) y muestra el título de las primeras 5.
print("\n--- Ejercicio 18: Consumo de API REST ---")
import requests

def obtener_tareas_api():
    url = "https://jsonplaceholder.typicode.com/todos"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() 
        tareas = respuesta.json()
        print("Primeras 5 tareas obtenidas de la API:")
        for tarea in tareas[:5]:
            print(f"- {tarea['title']}")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")

obtener_tareas_api()


# Ejercicio 19: Introducción a Pandas
# Tarea: Instala pandas (pip install pandas), convierte la lista `usuarios` a un DataFrame de Pandas y úsalo para filtrar y analizar los datos.
print("\n--- Ejercicio 19: Introducción a Pandas ---")
try:
    import pandas as pd
    df_usuarios = pd.DataFrame(usuarios)
    print("DataFrame de usuarios:")
    print(df_usuarios)
    print("\nUsuarios activos (filtrado con Pandas):")
    usuarios_activos_pd = df_usuarios[df_usuarios["activo"] == True]
    print(usuarios_activos_pd)
    edad_promedio = df_usuarios["edad"].mean()
    print(f"\nLa edad promedio es: {edad_promedio}")
except ImportError:
    print("\nPara completar este ejercicio, necesitas instalar la librería pandas.")
    print("Ejecuta en tu terminal: pip install pandas")