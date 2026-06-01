import re

# [:] Coincide con cualquier caracter dentro de los corchetes

username = "user_123+"
pattern = r"^[\w._%+-]+$"


match = re.search(pattern, username)
if match:
    print(f"Matched username: {match.group()}")
else:
    print("No match found.")


# buscar todas las vocales de una palabra
text = "Hello Worlaeioud!"
pattern = r"[aeiouAEIOU]"
matches = re.findall(pattern, text)
print(f"Vowels found: {matches}")

# una regex para encontrar las palabras man, fan y ban
# pero ignora al resto
text = "an ran fan lan van omniman"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print(f"Matched words: {matches}")
# \b

text = "22"
pattern = r"[4-9]"
matches = re.findall(pattern, text)
print(f"Matched digits: {matches}")


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo aeiou"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)