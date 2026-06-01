###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

from os import system
if system("clear") != 0: system("cls")



import re

# 1. El punto (.) coincide con cualquier caracter excepto el salto de linea
text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)
print(matches)

# --------------

text = "hola hola hila hela hula"
pattern = r"h.la"  # Coincide con cualquier caracter en la posicion del punto
matches = re.findall(pattern, text) 
print(matches)  # Salida: ['hola', 'hola', 'hila', 'hela', 'hula']

# como usar la barra invertida para anular el significado de 
text = "mi casa es blanca y el auto es rojo"
pattern = r"\."

matches = re.findall(pattern, text)
print(matches)  # Salida: []