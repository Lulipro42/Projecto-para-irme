###

# 04  - list methods
# Los metodos mas importantes para trabajar con listas

###

import os 
os.system("cls")

# añadir o insertar elementos en una lista

lista1 = ["a", "b", "c", "d"]

lista1.append("e") # agrega un elemento al final de la lista
print(lista1)

lista1.insert(3,"0") # agrega un elemento en la posicion indicada
print(lista1)

lista1.extend(["f","g","h"]) # agrega varios elementos al final de la lista
print(lista1)

# eliminar elementos de una lista
lista1.remove("0")  # elimina el primer elemento que coincida con el valor indicado
print(lista1)

ultimo = lista1.pop(2)  # elimina el ultimo elemento de la lista
print(lista1)
print(lista1)

lista1.pop(1) # elimina el elemento en la posicion indicada
print(lista1)

# eliminar por lo bestia
del lista1[-1]  # elimina el elemento en la posicion indicada
print(lista1)

# eliminar en un rango de elementos
del lista1[1:3]  # elimina los elementos en el rango indicado
print(lista1)

# mas metodos utiles
print("ordernar listas")
numeros = [3, 10, 8, 99,101]
numeros.sort()  # ordena la lista de menor a mayor
print(numeros)

print("Ordenar listas creando una nueva lista")
numeros = [3, 10, 8, 99,101]
sorted_numeros = sorted(numeros)  # crea una nueva lista ordenada de menor a mayor
print(sorted_numeros)

print("ordenar una listade cadenas de texto {mezclas mayusculas y minusculas}")
frutas = ["banana", "manzana", "pera", "limon", "Mango"]
sorted_frutas = sorted(frutas)  # crea una nueva lista ordenada alfabeticamente
print(frutas)
frutas.sort(key=str.lower)  # ordena la lista alfabeticamente ignorando mayusculas y minusculas
print(frutas)

# mas metodos utiles
animales = ["perro", "gato", "pez", "loro", "hamster", "gato"]
print(len(animales))  # devuelve la cantidad de elementos en la lista
print(animales.count("gato"))  # devuelve la cantidad de veces que aparece un elemento en la lista
print("loro" in animales)