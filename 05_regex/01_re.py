##
# 01-Expresiones regulares
#

from os import system
if system("clear") != 0: system("cls")
""" Las expresiones regulares (regex o regexp) son secuencias de caracteres que forman un patrón de búsqueda. Se utilizan para buscar, coincidir y manipular cadenas de texto basándose en patrones específicos. En"""

""" Porque aprender regex? 

- Busqueda avanzada: Permiten realizar búsquedas complejas y específicas en textos grandes.

- Busqueda avanzada: encotrar patrones en textos grandes de forma rapida y eficiente (un editor de texto, un motor de busqueda, etc).

- validacion de datos: Son utiles para validar formatos de datos como correos electronicos, numeros de telefono, codigos postales, etc que ingresa el usuario .

- manipulacion de texto: Facilitan la extraccion, sustitucion y modificacion de partes especificas de cadenas de texto facilmente.

"""
# 1. importar el modulo re
import re
#2. crear un patron de busqueda de cadena de texto 
pattern = r"hola"
#3. cadena de texto donde buscar el patron
text = "hola morronga"
#4. usar re.search() para buscar el patron en la cadena de texto
result = re.search(pattern, text)

if result:
    print("Patron encontrado:", result.group())
else:
    print("Patron no encontrado")    
    #caso de encontrar una coincidencia, las expresiones regulares pueden devolver información sobre la posición y el
    
# group(): Devuelve la cadena coincidente completa.
print("Cadena coincidente completa:", result.group()) 

# start(): Devuelve el índice de inicio de la coincidencia.
print(result.start())

# end(): Devuelve el índice final de la coincidencia.
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto y muestra la posición de inicio y fin de la coincidencia.
text = "La IA está transformando el mundo. La IA tiene un gran potencial. la IA es el futuro. la IA es fascinante."
pattern = r"IA"
found_ia  = re.search(pattern, text)

if found_ia:
    print(f"he encontrado el patron en el texto: {found_ia.group()}y termina en la posicion {found_ia.end()}")
else:
    print("Patron no encontrado")
    
### Encontrar todas las concidecncias en un texto
# .findall(): Devuelve una lista de todas las coincidencias en la cadena de texto.
text = "Me gusta python. Python es genial. Aprender python es divertido. aunque python puede ser desafiante. aguanye python."
pattern = r"py.hon"

matches = re.findall(pattern, text, re.IGNORECASE)  # re.IGNORECASE para ignorar mayusculas y minusculas
print("Todas las coincidencias encontradas:", matches)

print(len(matches))  # Numero de coincidencias encontradas  


# -----------------

# iter(): Devuelve un iterador que produce objetos de coincidencia para cada coincidencia encontrada.
text = "Me gusta python. Python es genial. Aprender python es divertido. aunque python puede ser desafiante. aguanye python."
pattern = r"py.hon"

matches = re.finditer(pattern, text, re.IGNORECASE)

for match in matches:
    print("Coincidencia encontrada:", match.group(), "en la posicion", match.start(), "-", match.end()) #contexto, las expresiones regulares son herramientas poderosas para trabajar con texto en programación y análisis de
    
### modificadores

# Los modificadpores son opciones que se pueden agregar a las expresiones regulares para cambiar su comportamiento. Algunos modificadores comunes incluyen:

# re.IGNORECASE (o re.I): Hace que la búsqueda sea insensible a mayúsculas y minúsculas.

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = r"python"
found_python = re.findall(pattern, text, re.IGNORECASE)
print(found_python) 