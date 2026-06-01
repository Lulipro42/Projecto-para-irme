###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\nejercicio 1:")
num1 = int(input("introduce el primer numero:"))
num2 = int(input("introduce el segundo numero:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Los numeros son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario que introduzca dos números y una operación ("+,-,/,*)
# Realiza la operación y muestra el resultado (maneja la division entre zero)
print("\nejercicio 2:")
num1 = float(input("introduce el primer numero:"))
num2 = float(input("introduce el segundo numero:"))
operacion = input("introduce la operacion (+, -, *, /): ")

if operacion == "+":
    print(f"El resultado es {num1 + num2}")
elif operacion == "-":
    print(f"El resultado es {num1 - num2}")
elif operacion == "*":
    print(f"El resultado es {num1 * num2}")
elif operacion == "/":
    if num2 == 0:
        print("Error: no se puede dividir entre cero.")
    else:
        print(f"El resultado es {num1 / num2}")
else:
    print("Operación no válida.")
    

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("\nEjercicio 3:")
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
    
    
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduce una edad: "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif edad <= 2:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")