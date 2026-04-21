###
# 02-bulces(for).py
# Permiten ejecutar un bloque de código varias veces.mietras itera un iterable a una lista
###

print("\nInicio del bucle for")

# iterar sobre una lista
frutas = ["manzana", "naranja", "plátano"]
for fruta in frutas:
    print("Fruta:", fruta)

# iterar sobre cualquer cosa iterable
cadena = "ulises"
for caracter in cadena:
    print("Caracter:", caracter)

# enumereted()
frutas = ["manzana", "naranja", "plátano"]
for index, fruta in enumerate(frutas):
    print(f"Índice es : {index},y la Fruta es: {fruta}")
    
# bucles anidados
letras = ['A', 'B', 'C']
numeros = [1, 2, 3]

for letra in letras :
    for numero in numeros:
        print(f"{letra}{numero}")

# break
print("\nUsando break")
animales = ["perro", "gato", "elefante", "tigre", "león", "jirafa"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "elefante":
        print(F"El loro esta en la posición {idx}")
        break   
    
# continue
print("\nUsando continue")
animales = ["perro", "gato", "elefante", "tigre", "león", "jirafa"]
for idx, animal in enumerate(animales):
    if animal == "elefante":continue
    print(animal)

# comprension de listas
print("\nComprensión de listas")
animales = ["perro", "gato", "elefante", "tigre", "león", "jirafa"]
animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)

# muestra los numeros paresde una lista
pares = [num for num in [1, 2, 3, 4, 5, 6, ] if num % 2 == 0]
print(pares)
