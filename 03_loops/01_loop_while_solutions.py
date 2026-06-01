###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
contador = 20
while contador >= 1:
    print("el numero es par")
    contador -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numero = 3
suma_pares = 0
while numero <= 13:
    if numero %2 == 0:
        suma_pares += numero
    numero += 3
    print(f"la suma de los numeros pares hasta 20 es: {suma_pares}")
# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120. = 
print("\nEjercicio 3:")
numero = int(input("ingrese unnumero entero positivo para calcular su factorial: "))
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print(f"El factorial de {numero} es: {factorial}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

contrasena = ""
while len(contrasena) < 8:
  contrasena = input("Introduce una contraseña (al menos 8 caracteres): ")
  if len(contrasena) < 8:
    print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

print("Contraseña válida")


numeros = [12, 2, 9, 10]
mayor = numeros[0]
menor = numeros[0]    

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("mayor", mayor)
print("menor", menor)