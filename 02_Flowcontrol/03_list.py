###
# 03- listas
# secuencias mutables de elementos
# pueden contener elementos de distintos tipos
###

import os
os.system("clear")

# creacion de listas 
print("\ncrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["anana", "banana", "manzana"] # lista de cadenas de textos


lista_vacia = [] # lista vacia
lista_de_listas = [[1, 2], [3, 4], [5, 6]] # lista de listas
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # matriz (lista de listas)

print(lista1)
print(lista2)

print(lista_de_listas)
print(matrix)

# acceso a elementos por indice
print("\nacceso a elementos por indice")
print(lista2[0]) # anana
print(lista2[1]) # banana
print(lista2[-1]) # manzana

print(lista_de_listas[1][1]) # 1

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5] # lista de enteros
print(lista1[0:3]) # [2, 3, 4]
print(lista1[:4]) # [1, 2, 3, 4]
print(lista1[2:]) # [3, 4, 5]
print(lista1[:])

# HAY MAS MAGIA
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(lista1[::4]) # [0, 4, 8, 12] para devolver indices de 4 en 4
print(lista1[::-1]) # [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] para invertir la lista

# modificar una lista
lista1[0] = 20
print(lista1)


# añadir elementos a una lista
lista1 = [1, 2, 3]

lista1 = lista1 +[4, 5, 6] # concatenacion
print(lista1)


# forma corta y mas eficiente
lista1 += [7, 8, 9]
print(lista1)

# recuperar longitud de una lista
print("longitud de lista", len)