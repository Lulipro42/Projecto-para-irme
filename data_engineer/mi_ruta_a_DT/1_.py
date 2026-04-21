### ESTE ES MI CAMINO PARA SER DATA ENGINEER ###

# Primer ejercicio: crear una calculadora simple
print("\n--- Dia 1: Ejercicio 1 - Calculadora simple ---")

def calculadora_simple():
    try:
        a = float(input("Ingrese el numero que desee ")) # El float convierte el valor ingresado en un numero decimal
        b = float(input("Ingrese el segundo numero que desee "))
    except ValueError:
        print("Porfavor ingrese solo numeros validos")
        return
    
    print("Operaciones disponibles son: + * - /")
    operacion = input("Elige una operacion:").strip() # El strip sirve liminar espacios en blanco, tabuladores, saltos de línea y caracteres específicos, tanto del inicio como del final de una cadena de texto, devolviendo una copia limpia sin modificar la original.
    if operacion == "+":
        resultado = a + b
    elif operacion == "-":
        resultado = a - b
    elif operacion == "*":
        resultado = a * b
    elif operacion == "/":
        if b == 0:
            print("No se puede dividir entre cero")
            return
        resultado = a / b
    else:
        print("Operacion no valida")
        return
    print(f"El resultado de {a} {operacion} {b} es: {resultado}")
calculadora_simple()

# Convertirdor de temperaturas
print("\n--- Dia 1: Ejercicio 2 - Convertidor de temperaturas ---")
def convertidor_de_temperaturas():
    try:
        celsiuis = float(input("ingrese la temperatura en grados Celsius:"))
    except ValueError:
        print("Porfavor ingrese solo numeros validos")
        return
    fahrenheit = (celsiuis * 9/5) + 32
    if fahrenheit.is_integer():
        fahrenheit = int(fahrenheit)
    print(f"{celsiuis} grados Celsius son {fahrenheit} grados Fahrenheit.")
convertidor_de_temperaturas()


# Saber si es impar o par
print("\n--- Dia 1: Ejercicio 3 - Saber si es impar o par ---")
def impar_o_par():
    try:
        numero = int(input("Ingrese un numero entero:"))
    except ValueError:
        print("Porfavor ingrese solo numeros validos")
        return
    if numero % 2 == 0:
        print(f"el numero {numero} es par")
    else:
        print(f"el numero lamentablemnte {numero} es impar")

impar_o_par()



# Calcular la edad con dias 
print("\n--- Dia 1: Ejercicio 4 - Calcular la edad ---")
def calcular_edad_en_dias():
    try:
        edad = int(input("Ingrese su edad en años: "))
    except ValueError:
        print("Por favor ingrese solo numeros validos.")
        return

    dias = edad * 365
    print(f"Usted ha vivido aproximadamente {dias} dias.")

calcular_edad_en_dias()


# Validar contraseña
print("\n--- Dia 1: Ejercicio 5 - Validar contraseña ---")
def validar_contraseña():
    contraseña_correcta = "Mami_pro42"
    contraseña_ingresada = input("Ingrese la contraseña: ")
    len_contraseña = len(contraseña_ingresada)
    if len_contraseña < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return
    if contraseña_correcta == contraseña_ingresada:
        print("Acceso concedido.")
    else:
        print("Acceso denegado. Contraseña incorrecta.")

validar_contraseña()

# diccionario simple
lista = [12, 20, 1, 8, 34 , 9]
total = 0

for numero in lista:
    total = total + numero
print(f"\nLa suma total de la lista es: {total}")
# ejercicio 2

numeros_mayores_a_10 = []
for numero in lista:
    if numero > 10:
        numeros_mayores_a_10.append(numero)
print(f"\nLos numeros mayores a 10 en la lista son: {numeros_mayores_a_10}")
# Ejercicio 3
numero_pares = []
for numero in lista:
    if numero % 2 == 0:
        numero_pares.append(numero)
print(f"\nLos numeros pares en la lista son: {numero_pares}")
# Ejercicio 4
suma = 0
for numero in lista:
    suma = suma + numero
    promedio = suma /len(lista) # El len sirve para contar y devolver el número total de caracteres en una cadena de texto, incluyendo letras, números, símbolos y espacios en blanco
    print(f"\nEl promedio de los numeros en la lista es: {promedio}")
    
    
# Ejercicios del Dia 2
print("\n--- Dia 2: Ejercicio 1 - Diccionario simple ---")
lista = [12, 8, 9, 40, 24, 4]
lista_de_myores_a_10 = []
for numero in lista:
    if numero > 10:
        lista_de_myores_a_10.append(numero)

print(f"\nLos numeros mayores a 10 en la lista son: {lista_de_myores_a_10}")

# Ejercicio 3 de cuantos pares hay en la lista
print("\n--- Dia 2: Ejercicio 2 - Numeros pares ---")
numeros = [9, 7, 5, 12, 4, 14, 74]
numeros_pares = []
len_n = 0

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
        len_n = len(numeros_pares)
print(f"\nLos numeros pares en la lista son: {numeros_pares} y hay {len_n} numeros pares")

# ejercicio 4 creare un diccionario
print("\n--- Dia 2: Ejercicio 3 - Promedio de numeros ---")
persona = {
    "nombre": "Ulises",
    "edad": 17,
    "ciudad": "La Plata",
    "altura": 1.77
}
print(f"\nEl nombre de la persona buscada es {persona["nombre"]}")
print(f"\nla edad de esa persona es {persona['edad']}")
print(f"\nla ciudad de esa persona es {persona['ciudad']}")
print(f"\nla altura de esa persona es {persona['altura']}")

# FUNCIONES
print("\n--- Dia 2: Ejercicio 4 - Funciones ---")
def sumar_dos_numeros(a, b):
    suma = a + b
    return suma 
resultado = sumar_dos_numeros(4,5)
print(f"\nEl resultado de la suma es: {resultado}")

# Ejercico 2 DE FUNCIONES
def el_mayor_dos_numeros(a, b):
    if a > b:
        return a
    else:
        return b
mayor = el_mayor_dos_numeros(21, 52)
print(f"\nEl mayor de los dos numeros es: {mayor}")

# Ejercicio 3 de FUNCIONES
lista = [2, 10, 53, 67, 99, 42]

def devolver_numeros_pares(lista):
    numeros_pares = []
    for numero in lista:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

resultado = devolver_numeros_pares(lista)
print(f"Los numeros pares son {resultado}")


# Ejercicio 3 DE FUNCIONES que calcule promedios
lista = [10, 21, 2, 8, 41, 5]
suma = 0

def calcular_el_promedio_de_la_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    return promedio

resultado = calcular_el_promedio_de_la_lista(lista)
print(f"esot es el promedio de los numeros {resultado}")

# Ejercicio 3 de FUNCIONES 
lista = [12, 2, 9, 24, 53, 4, 49]
nueva_lista = []
for numero in lista:
    if numero > 10:
        nueva_lista.append(numero)
cantidad = len(nueva_lista)
print(f"Los numeros que superan el 10 son {nueva_lista} y la cantidad es {cantidad}")

# Crear datos.txt con líneas de prueba
with open("datos.txt", "w", encoding="utf-8") as f:
    f.write("Linea 1\n")
    f.write("Linea 2\n")
    f.write("Linea 3\n")
    f.write("Linea 4\n")



# Ejercico nivel 4 del dia 4
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contador = 0
    for linea in archivo:
        contador += 1

print(f"Cantidad de lineas: {contador}")

# Segundo ejercicio del dia 4
with open("salida.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola este es mi nombre en una cadena de texto.\n")
    archivo.write("Me llamo Ulises Solis y tengo 17 años y mido 1,77.\n")
    archivo.write("Actualmente vivo en la plata pero mi sueño es irme a vivir a japon o a otro pais asiatico.\n")
    
print("Archivo 'salida.txt' creado y escrito.")

# Ejercicio 3 del dia 4 (Por revisar para poder entenderlo mejor)
lista = ["manzana", "pera", "uva", "limon"]
with open("lista.txt", "w", encoding="utf-8") as f:
    for elemento in lista:
        f.write(str(elemento) + "\n")

# Ejercicio 4 del dia 4
palabra = "linea"
with open("datos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        if palabra in linea:
            print(linea)

# Ejercicio 5 del dia 4
dato = [6, None, "", 10, None, 24]
resultado = []

for datos in dato:
    if datos is None:
        continue
    if datos == "":
        continue
    if datos % 2 == 0:
        resultado.append(datos)

print(f"datos limpios y pares {resultado}")

# MINI EJERCICIOS DE REPASO
# resultado = 0

# def calculadora_simple_de_sum():
#     try:
#         a = float(input("Ingrese el numero deseado:"))
#         b = float(input("Ingrese el segundo numero deseado:"))
#     except ValueError:
#         print("Porfavor ingrese solo numeros validos")
#         return
    
#     print("Operaciones disponibles + * / -")
#     operacion = input("Elige una opcion de estas").strip()
#     if operacion == "+":
#         resultado = a + b
#     if operacion == "*":
#         resultado = a * b
#     if operacion == "-":
#         resultado = a - b 
#     elif operacion == "/":
#         if b == 0:
#             print("No se puede dividir entre cero")    
#             return
#         resultado = a / b
#     else:
#         print("Operacion invalida")
#         return
#     print(f"El resultado de la suma es {a} {operacion}: {resultado}")
# calculadora_simple_de_sum()

# # Segundo ejercicio de repaso 
# lista = [25, 24, 54, 67, 89, 23, 22, 76]
# numeros_pares: list[int] = [] # list indica que es una lista #[int] indica que la lista contiene enteros.
# for numeros in lista:
#     if numeros % 2 == 0:
#         numeros_pares.append(numeros)
# print(f"Los numeros pares son {numeros_pares}")

# # otro ejercicio 
# def calcular_grados ():
#     try:
#         celcius = float(input("Ingrese la temperatura que desea:"))
#     except ValueError:
#         print("Porfavor solo ingrese numeros enteros")
#         return
#     fahrenheit = (celcius * 9/5) + 32
#     if fahrenheit.is_integer(): 
#         fahrenheit = int(fahrenheit)
#     print(f"{celcius} grados Celcius serian en {fahrenheit} grados Fahreinheit")
# calcular_grados()

# # Tercer ejercicio
# lista = [2,41,35,67,87,10]
# total = 0
# for numero in lista:
#     total = total + numero
# print(f"El total de la lista es {total}")

# # Ejercicio 4
# lista = [10, 21, 8, 4, -10, 3, 45,22, 54]
# numeros_mayores_a_10_y_pares = [] 
# for numero in lista:
#     if numero > 10 and numero % 2 == 0:
#         numeros_mayores_a_10_y_pares.append(numero)
# print(f"Los numeros mayores a 10 y pares{numeros_mayores_a_10_y_pares}")

# # Ejercicio 5
# lista = [12, 19, 65, 23, 10, 6, 42]
# pares = []
# for numero in lista:
#     if numero % 2 == 0:
#         pares.append(numero)
# print(f"los numeros pares son: {pares}")
# #print(f"Los numeros pares y contados son {len(pares)}") # me sirve pero yo solo quiero saber cuales son, no cuantos son

# # Ejercicio 6
# dato = [12, None, "", 42, None, ""]
# resultado = []
# for datos in dato:
#     if datos is None:
#         continue
#     if datos == "":
#         continue
#     if not isinstance(datos, int): # isinstance(objeto, tipo) sirve para verificar el tipo de un valor.
#         continue
#     if datos % 2 != 0:
#         continue
#     resultado.append(datos)
# print(f"datos limpios y pares {resultado}")

# Repaso de los diccionarios
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": True, "pais": "AR"},
    {"nombre": "Sanji", "edad": 21, "activo": True, "pais": "UY"},
    {"nombre": "Nami", "edad": 20, "activo": False, "pais": "AR"},
    {"nombre": "Usopp", "edad": 17, "activo": True, "pais": "CL"},
    {"nombre": "Chopper", "edad": 15, "activo": False, "pais": "AR"},
]
activos = []
for usuario in usuarios:
    if usuario["activo"]:
        activos.append(usuario["nombre"])
print(f"Los usarios activos son: {activos}")

# Segundo ejercicio de repaso
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": True, "pais": "AR"},
    {"nombre": "Sanji", "edad": 21, "activo": True, "pais": "UY"},
    {"nombre": "Nami", "edad": 20, "activo": False, "pais": "AR"},
    {"nombre": "Usopp", "edad": 17, "activo": True, "pais": "CL"},
    {"nombre": "Chopper", "edad": 15, "activo": False, "pais": "AR"},
]
activos = 0
inacticvos = 0
for usuario in usuarios:
    if usuario["activo"]:
        activos += 1 # Yo al poner el el += la lista o numero en este caso seria activos o inacticvos tienen que ser numeros no esto []
    else:
        inacticvos += 1
print(f"Los usarios activos son: {activos}")
print(f"Los usarios inactivos son:{inacticvos}")

# Tercer ejercicio de repaso
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": True, "pais": "AR"},
    {"nombre": "Sanji", "edad": 21, "activo": True, "pais": "UY"},
    {"nombre": "Nami", "edad": 20, "activo": False, "pais": "AR"},
    {"nombre": "Usopp", "edad": 17, "activo": True, "pais": "CL"},
    {"nombre": "Chopper", "edad": 15, "activo": False, "pais": "AR"},
]
suma_edades = 0
cantidad = 0
for usuario in usuarios:
    suma_edades += usuario["edad"]
    cantidad += 1
    if cantidad > 0:
        promedio = suma_edades / cantidad
    else:
        promedio = 0
print(f"El promedio de edades en la tripulacion es la concha tuya reportera: {promedio}")


# Cuarto ejercicio del repaso 
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": True, "pais": "AR"},
    {"nombre": "Sanji", "edad": 21, "activo": True, "pais": "UY"},
    {"nombre": "Nami", "edad": 20, "activo": False, "pais": "AR"},
    {"nombre": "Usopp", "edad": 17, "activo": True, "pais": "CL"},
    {"nombre": "Chopper", "edad": 15, "activo": False, "pais": "AR"},
]
mayores_activos = []
for usuario in usuarios:
    if usuario["activo"] and usuario["edad"] >= 18:
        mayores_activos.append(usuario["nombre"])
print(f"Los usarios activos y mayores son skibidi: {mayores_activos}")

# Quinto ejercicio de repaso de dicconarios 
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": True, "pais": "AR"},
    {"nombre": "Sanji", "edad": 21, "activo": True, "pais": "UY"},
    {"nombre": "Nami", "edad": 20, "activo": False, "pais": "AR"},
    {"nombre": "Usopp", "edad": 17, "activo": True, "pais": "CL"},
    {"nombre": "Chopper", "edad": 15, "activo": False, "pais": "AR"},
]
usuarios_activos_y_pais = []

for usuario in usuarios:
    if usuario["activo"] and usuario["pais"]:
        usuarios_activos_y_pais.append({"nombre": usuario["nombre"], "pais": usuario["pais"]})


print(f"Los usuarios activos y de los paises que son son: {usuarios_activos_y_pais}")

# Sexto ejercicio de repaso de diccionarios
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": True, "pais": "AR"},
    {"nombre": "Sanji", "edad": 21, "activo": True, "pais": "UY"},
    {"nombre": "Nami", "edad": 20, "activo": False, "pais": "AR"},
    {"nombre": "Usopp", "edad": 17, "activo": True, "pais": "CL"},
    {"nombre": "Chopper", "edad": 15, "activo": False, "pais": "AR"},
]
def filtrar_por_pais(usuarios,pais):
    resultado = []
    for usuario in usuarios:
        if usuario["pais"] == pais: # el El operador == en programación es un operador de comparación o igualdad que verifica si dos valores u operandos son equivalentes. Devuelve un valor booleano (true si son iguales, false si no)
            resultado.append(usuario)
    return resultado
print(f"El resultado de esto es: {filtrar_por_pais(usuarios, "AR")}")

# Ejercicio 7 del repaso de diccionarios
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": True, "pais": "AR"},
    {"nombre": "Sanji", "edad": 21, "activo": True, "pais": "UY"},
    {"nombre": "Nami", "edad": 20, "activo": False, "pais": "AR"},
    {"nombre": "Usopp", "edad": 17, "activo": True, "pais": "CL"},
    {"nombre": "Chopper", "edad": 15, "activo": False, "pais": "AR"},
]
def edad_promedio_de_los_activos(usuarios):
    suma = 0
    contador = 0
    
    for usuario in usuarios:
        if usuario["activo"]:
            suma += usuario["edad"]
            contador += 1
            
        if contador == 0:
            return 0
        return suma / contador

promedio = edad_promedio_de_los_activos(usuarios)
print(f"El promedio de edad de los muwigaras es: {promedio}")    


# Ultimo ejercicio de repaso de diccionarios 
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": True, "pais": "AR"},
    {"nombre": "Sanji", "edad": 21, "activo": True, "pais": "UY"},
    {"nombre": "Nami", "edad": 20, "activo": False, "pais": "AR"},
    {"nombre": "Usopp", "edad": 17, "activo": True, "pais": "CL"},
    {"nombre": "Chopper", "edad": 15, "activo": False, "pais": "AR"},
]
def devolver_usuario_mayor(usuarios):
    if not usuarios:
        return None

    mayor = usuarios[0]
    for usuario in usuarios:
        if usuario["edad"] > mayor["edad"]:
            mayor = usuario

    return mayor

print(f"El usuario de mayor edad es: {devolver_usuario_mayor(usuarios)}")


# Ejercicios de los diccionarios
persona = {
    "nombre": "Ulises",
    "edad": 17,
    "apellido": "Solis",
    "altura": 1.77,
}
print(f"\nMi nombre es: {persona['nombre']}")
print(f"\nMi apellido es: {persona['apellido']}")
print(f"\nMi edad es: {persona['edad']}")
print(f"\nMi altura es: {persona['altura']}")

# Segundo ejercicio de DICCIONARIOS
productos = {
    "producto1": "Tablet",
    "precio": 20,
    "stock": 5
}
productos["precio"] = 25
productos["stock"] = productos["stock"] - 2
print(f"Debido a la alta demanda del producto le tuvimos que subir el precio y ademas nos queda poco stock: {productos}")

# Tercer ejercicio
lista = ["hola", "adios", "chau", "sigma"]
conteo = {}
for palabra in lista:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print(conteo)

# Cuarto ejercicio de Diccionario
#usuario = {
#    "nombre": "ana",
#    "edad": 24,
#}
#print(usuario.get("ciudad", "desconocido")) # El get Sirve para acceder a una clave que puede no existir sin que el programa falle por ejemplo si "ciudad" no existe te tira "desconocido" en vez de KeyError

usuarios = [
    {"nombre": "juan", "edad": 24},
    {"nombre": "david", "edad": 44},
    {"nombre": "ana", "edad": 37}
]

for u in usuarios:
    print(u.get("activo", "no se sabe"))

# Ejercicio 5 del repaso de DICCIONARIOS
notas = {
    "matematicas": 9,
    "lengua": 8,
    "historia": 9,
}
for materia, nota in notas.items():
    print(f"{materia} -> {nota}")


# Ejercicios del dia 4




with open("datos.txt", "r", encoding="utf-8") as f:
    contador = 0
    for linea in f:
        contador += 1
print(contador)

#Ejercicios del dia 4
with open("salida.txt", "w", encoding="utf-8") as f:
    f.write("Linepro1\n")
    f.write("Linepro2\n")
    f.write("Linepro3\n")
    f.write("Linepro4\n")
print("lineapro")

# Ejercicios del Dia 4
lista = ["pera", "morronga", "nami", "x", "sanji"]
with open("lista.txt", "w", encoding="utf-8") as f:
    for elemento in lista:
        f.write(str(elemento) + "\n")
print("ok")

# Ejercicios del dia 4
palabra = "sanji x nami"
with open("datos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        if palabra in linea:
            print(linea)
            
# Ultimo ejercicio del dia 4
dato = [24, None, "", 84, None, 5, ""]
resultado = []

for datos in dato:
    if datos is None:
        continue
    if datos == "":
        continue
    if datos % 2 == 0:
        resultado.append(datos)
print(f"Los datos limpios y pares son: {resultado}")

# Ejercicios del dia 5
lista = ["hola como estas", "pana", "yo estoy"]
normalizada = []
for texto in lista:
    texto_limpio = texto.strip().upper() # El upper sirve para hacer todos los textos en mayusculas en cambio el, lower es lo contrario osea todas las palabras en minuscula
    normalizada.append(texto_limpio)
print(normalizada)

# Ejercicios del dia 5
lista = {3, 12, 21, 54,}
resultado = []
for n in lista: # Me parece que el N es para abreviar la palabra numero
    if n > 10:
        resultado.append(n * 2) # Esto lo que hace es que los nuemeros que superan el diez seran multiplicados por dos o por el numero que yo quiera y puedo cambier el * por cualquier otro signo como "/, +,-"
print(resultado)

# Ejercicio 4 del dia 5
lista = ["rojo", "azul", "rojo","amarillo", "azul", "rojo", "verde", "azul"]
conteo = {}
for color in lista:
    if color in conteo: 
        conteo[color] += 1
    else:
        conteo[color] = 1
print(f"el conteo es: {conteo}")

# Ejercicio 5 del dia 5
with open("resultado.txt", "w", encoding="utf-8") as f:
    f.write("Resultado 1: Hola me llamo\n")
    f.write("Resultado 2: Ulises Solis y quiero que sanji se coja a nami\n")
print("Archivo guardado")

# EJercicios del dia 6 FUNCIONES CON LISTAS
lista = [12, 43, -12, 54, 32, 3, 7]
def maximo_de_una_lista(lista):
    max_val = lista[0]
    for n in lista:
        if n > max_val:
            max_val = n
    return max_val
print(f"El numero mas alto de la lista es:{maximo_de_una_lista(lista)}")

# Ejercicio 2 del dia 6
lista = [12, 23, -1, 5, 54, 2]
def minimo(lista):
    min_val = lista[0]
    for n in lista:
        if n < min_val:
            min_val = n
    return min_val
print(f"El numero mas bajo de la lista seria: {minimo(lista)}")

# Ejercicio 3 del dia 6 
lista = [12, 2, 4, 42, 22, 8]
def sumar_los_numeros_pares(lista):
    suma = 0
    for n in lista:
        if n % 2 == 0:
            suma += n
    return suma
print(f"La suma de los numeros pares son: {sumar_los_numeros_pares(lista)}")

# Ejercicio 4 del dia 6
def filtrar_rango(lista, minimo, maximo):
    resultado = []
    for n in lista :
        if minimo <= n <= maximo:
            resultado.append(n)
    return resultado
print(filtrar_rango([1, 5, 10, 15, 20], 5, 15)) # Significa: “de la lista, qué números están entre 5 y 15”. Puedes usar tu propia lista y tu propio rango.

# Ejercicio 5 del dia 6 
def promedio_sin_negativos(lista):
    suma = 0
    contador = 0
    for n in lista:
        if n >= 0:
            suma += n
            contador += 1
    if contador == 0:
        return 0
    return suma / contador
print(promedio_sin_negativos([3, -2, 5, -1, 10]))

# Ejercicios del dia 7
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": None},
    {"nombre": "Sanji", "edad": 21, "activo": True},
    {"nombre": "Nami", "edad": 20, "activo": None},
    {"nombre": "Ussop", "edad": 65, "activo": True}
]

usuarios_activos = []
for usuario in usuarios:
    if usuario["activo"] and usuario["edad"] >= 18:
        usuarios_activos.append(usuario["nombre"])
print(f"Los usuarios activos y mayores son: {usuarios_activos}")

# Ejercicio 2 del dia 7
usuarios = [
    {"nombre": "brook", "edad": 78},
    {"nombre": "momo", "edad": 45},
    {"nombre": "jimbe", "edad": 34},
    {"nombre": "Mihawk", "edad": 12}
]

suma = 0
contador = 0

for usuario in usuarios:
    suma += usuario["edad"]
    contador += 1

promedio = suma / contador
print(f"El promedio de edades de los usuarios es: {promedio}")

# Ejercicio 3 del dia 7
usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": None},
    {"nombre": "Sanji", "edad": 21, "activo": True},
    {"nombre": "Nami", "edad": 20, "activo": None},
    {"nombre": "Ussop", "edad": 65, "activo": True}
]
activos = 0
inacticvos = 0
for usuario in usuarios:
    if usuario["activo"] == True:
        activos += 1
    else:
        inacticvos += 1
print(activos)
print(inacticvos)

# Ejercicio 4 del dia 7

usuarios = [
    {"nombre": "Robin", "edad": 29, "activo": None},
    {"nombre": "Sanji", "edad": 12, "activo": True},
    {"nombre": "Nami", "edad": 20, "activo": True},
    {"nombre": "Ussop", "edad": 14, "activo": True}
]

mayores_activos = []

for usuario in usuarios:
    if usuario["activo"] and usuario["edad"] >= 18:
        mayores_activos.append(usuario["nombre"])

print(f"Los usuarios activos y mayores de edad son: {mayores_activos}")


### EJERCICIOS PARA ESTAR LISTO PARA SQL ###
# Ejercicio 1 
lita = [12, 5, 67, 23, 14, 7, 9, 21]
numeros_mayores_a_10 = []
numeros_mayores_a_10_sumados = 0
for numero in lista:
    if numero > 10:
        numeros_mayores_a_10.append(numero)
        numeros_mayores_a_10_sumados += numero
print(f"Los numeros mayores a 10 son: {numeros_mayores_a_10} y los numeros sumados son: {numeros_mayores_a_10_sumados}")



# Ejercicio 2 de poder estar listo para SQL
dato = [None, "", 12, 54, "", None, 8]
resultado = []
for datos in dato:
    if datos is None:
        continue
    if datos == "":
        continue
    if not isinstance(datos,int): # if not isinstance(datos, int): significa:“Si datos no es entero, entra al bloque”.
        continue
    if datos <= 10:
        continue
    resultado.append(datos)
print(f"Los datos limpios y superiores a 10:{resultado}")



# Ejercicio 3 para poder pasar a SQL
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
    promedio_edades = suma_edades / total_f
else:
    promedio_edades = 0


print(f"El total de personas registradas es: {total_f}")
print(f"El total de activos es: {activos_f}")
print(f"El total de personas mayores es: {mayores_f}")
print(f"El total de personas activas y mayores es: {activos_y_mayores_f}")
print(f"El promedio de edades es: {promedio_edades}")



# Ejercicio 4 de Repaso antes de pasar a SQL
lista = [15, 12, 5, 7, 2, -2, 54]
def numero_mayor(lista):
    mayor = lista[0]
    for n in lista:
        if n > mayor:
            mayor = n
    return mayor
print(numero_mayor(lista))
def numero_menor(lista):
    menor= lista[0]
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
        if n % 2 == 0:
            suma += n
    return suma
print(suma_de_impares(lista))




# Ultimo ejercicio para saber si estoy listo para SQL
ventas = [
    {"producto": "Notebook", "precio": 1200, "cantidad": 2},
    {"producto": "Mouse", "precio": 25, "cantidad": 10},
    {"producto": "Teclado", "precio": 75, "cantidad": 4},
    {"producto": "Monitor", "precio": 300, "cantidad": 3},
]
ingreso_total = 0
max_ingreso = -4
producto_top = None #usa como valor inicial cuando todavía no sabes cuál será el producto top.Luego, dentro del for, lo reemplazas por un producto real cuando encuentras uno con mayor ingreso.

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

# REPASO
ventas = [
    {"producto": "Auriculares", "precio": 80, "cantidad": 15},
    {"producto": "Webcam", "precio": 120, "cantidad": 6},
    {"producto": "Microfono", "precio": 150, "cantidad": 4},
    {"producto": "Mousepad", "precio": 20, "cantidad": 25},
    {"producto": "Parlantes", "precio": 200, "cantidad": 3},
]

def analizar_ventas(ventas):
    if not ventas:
        return 0, None, 0, 0
    
    ingreso_total = 0
    max_ingreso = -1
    producto_top = None
    
    for venta in ventas:
        ingreso = venta["precio"] * venta["cantidad"]
        ingreso_total += ingreso
        
        if ingreso > max_ingreso:
            max_ingreso = ingreso
            producto_top = venta["producto"]

    
    promedio_ingreso = ingreso_total / len(ventas)
    return ingreso_total, producto_top, max_ingreso, promedio_ingreso


ingreso_total,  producto_top, max_ingreso, promedio_ingreso = analizar_ventas(ventas)

print(f"Ingreso total: {ingreso_total}")
print(f"Producto top: {producto_top} ({max_ingreso})")
print(f"Promedio por producto: {promedio_ingreso}")


# --- Simulacion de SQL en Python: JOIN, GROUP BY y HAVING ---
# Concepto:
# 1. JOIN: Unir datos de dos listas diferentes usando una clave común (id).
# 2. GROUP BY: Agrupar datos por una categoría (ej. departamento) y calcular algo (suma, promedio).
# 3. HAVING: Filtrar esos grupos resultantes (ej. solo mostrar departamentos con sueldos altos).

print("\n--- Simulacion SQL: JOIN, GROUP BY y HAVING ---")

# Tablas simuladas (Listas de diccionarios)
empleados = [
    {"id": 1, "nombre": "Ana", "departamento_id": 101, "salario": 3000},
    {"id": 2, "nombre": "Luis", "departamento_id": 102, "salario": 2500},
    {"id": 3, "nombre": "Marta", "departamento_id": 101, "salario": 3200},
    {"id": 4, "nombre": "Pedro", "departamento_id": 103, "salario": 2800},
    {"id": 5, "nombre": "Sofia", "departamento_id": 102, "salario": 2600},
    {"id": 6, "nombre": "Carlos", "departamento_id": 101, "salario": 3100}
]

departamentos = [
    {"id": 101, "nombre": "Ventas"},
    {"id": 102, "nombre": "Marketing"},
    {"id": 103, "nombre": "Soporte"}
]

# Paso 1: JOIN (Unir empleados con nombres de departamentos)
empleados_unidos = []
for emp in empleados:
    nombre_depto = "Sin Departamento"
    # Buscamos el departamento correspondiente (Logica de JOIN)
    for depto in departamentos:
        if emp["departamento_id"] == depto["id"]:
            nombre_depto = depto["nombre"]
            break
    
    # Creamos un nuevo registro con la info unida
    empleados_unidos.append({
        "nombre": emp["nombre"],
        "departamento": nombre_depto,
        "salario": emp["salario"]
    })

print("1. Resultado del JOIN (primeros 3):")
for e in empleados_unidos[:3]:
    print(e)

# Paso 2: GROUP BY (Agrupar por departamento y sumar salarios)
salarios_por_depto = {}
for emp in empleados_unidos:
    depto = emp["departamento"]
    # Si el departamento no esta en el diccionario, lo inicializamos en 0
    if depto not in salarios_por_depto:
        salarios_por_depto[depto] = 0
    # Acumulamos el salario (Logica de SUM)
    salarios_por_depto[depto] += emp["salario"]

print("\n2. Resultado del GROUP BY (Suma de salarios):")
print(salarios_por_depto)

# Paso 3: HAVING (Filtrar departamentos que gastan mas de 8000)
deptos_costosos = {}
for depto, total in salarios_por_depto.items():
    if total > 8000: # Condicion HAVING (Filtrar sobre el resultado agrupado)
        deptos_costosos[depto] = total

print("\n3. Resultado del HAVING (Gastos > 8000):")
print(deptos_costosos)