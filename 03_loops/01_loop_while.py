numero = 3
suma_pares = 0
while numero <= 13:
    if numero % 2 == 0:        # ¿El número actual es par?
        suma_pares += numero   # Si es par, lo suma a la bolsa
    numero += 3                # El número salta: 3, 6, 9, 12...
    print(f"La suma es: {suma_pares}")

# EJERCICIO 2 

numero = 3
suma_pares = 0
while numero <= 13:
    if numero % 2 == 0:        # ¿El número actual es par?
        suma_pares += numero   # Si es par, lo suma a la bolsa
    numero += 3                # El número salta: 3, 6, 9, 12...
    print(f"La suma es: {suma_pares}")
    

# EJERCIIO 3 
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador  # Multiplica lo que ya tenía por el número actual
    contador += 1          # Pasa al siguiente número


# EJERCICIO 4
contrasena = ""
while len(contrasena) < 8:
    contrasena = input("Introduce una contraseña: ")
    
# ULTIMO EJERCICIO 
numeros = [12, 2, 9, 10]
mayor = numeros[0] # Empezamos asumiendo que el primero es el más grande
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero # Si encuentro uno más grande, actualizo mi "récord"
    if numero < menor:
        menor = numero # Si encuentro uno más chico, actualizo