"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

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

# --------------------

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

# \d: coincide con cualquier digito (0-9)

text = "el numero de telefono es 12465698"
found = re.findall(r"\d{8}", text)

print(found)

# ejercicio: detectar si hay un número de teléfono en el texto
text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono {found.group()}")

# \w: coincide con cualquier alfa numerico  (a-z, A-Z, 0-9, _)

text = "el_rubios_69"
pattern= r"\w"
found = re.findall(pattern, text)
print(found)

# \s: coincide con cualquier espacio en blanco (espacio tabulacion, salto de linea)
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el principio de una cadena
username = "423_name22" 
pattern = r"^\w" # validar nombre de usuario

valid = re.search(pattern, username)

if valid: print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

phone = "+34 688999999"
pattern = r"^\+34 \d{9}$" # validar número de teléfono

valid = re.search(pattern, phone)
if valid: print("El número de teléfono es válido")
else: print("El número de teléfono no es válido")

# $: Coincide con el final de una cadena
text = "final de la frase."
pattern = r"frase\.$"

valid = re.search(pattern, text)

if valid: print("El texto termina correctamente")
else: print("El texto no termina correctamente")

# EJERCICIO: validar un email
text = "ulisessolis422@gmail.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
valid = re.search(pattern, text)   
if valid: print("El email es válido")
else: print("El email no es válido")


# EJERCICIO:
# tenemos una lista de archivos necesitamos saber los nombres de los ficheros de extension .txt y 
files = "file1.txt, file2.doc, image.png, notes.txt, presentation.pptx"
pattern = r"\b\w+\.txt\b"
matches = re.findall(pattern, files)
print("Archivos .txt encontrados:", matches)
# Resultado esperado: ['file1.txt', 'notes.txt']

# \b: coicide con el principio o el final de una palabra
text = "hola mundo, bienvenidos al mundo mudopo mdo de la programación"
pattern = r"\bmundo\b"

found = re.findall(pattern, text)
print(found)  # ['mundo', 'mundo']

# |: Coincidr con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)