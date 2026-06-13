###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re

# * El cuantificador '*' coincide con cero o más ocurrencias del carácter o grupo precedente.
text = "aaaba"
patter = r"a*"
matches = re.findall(patter, text)
print("Matches for '*a':", matches)  # Salida: ['a', 'a', 'a', 'a', 'a']

# ejercicio 1
# ¿cuantas palbras tiene de 0 a mas "a" y despues una b=

# +: El cuantificador '+' coincide con una o más ocurrencias del carácter o grupo precedente.
text = "ddd aaa ccc aba bb aa ccaasa"
patter = r"a+"
matches = re.findall(patter, text)
print("Matches for '+a':", matches)  # Salida: ['aaa', 'a', 'aa', 'aaa']

import re

# --- EL SIGNO DE INTERROGACIÓN (?) ---
# Significa: "Lo que está antes puede estar 0 o 1 vez" (es opcional).
text = "aabacb"
patter = r"a?b" # Busca una 'a' opcional seguida de una 'b'.
matches = re.findall(patter, text)
# Resultado: ['ab', 'b'] -> 'ab' (en "aab") y 'b' (al final de "aabacb").
print("Matches para 'a?b':", matches)

# EJERCICIO TELÉFONO: Hacer el prefijo +34 opcional.
phone_text = "Llamame al 612345678 o al +34612345678"
# (\+34)? -> El grupo +34 es opcional. El \ es para que no crea que el + es un comando.
# 6\d{8}  -> Empieza con 6 y sigue con exactamente 8 dígitos.
patter = r"(?:\+34)?6\d{8}" # Usamos ?: para que findall no se confunda con grupos.
matches = re.findall(patter, phone_text)
print("Números encontrados:", matches)

# --- CUANTIFICADOR EXACTO {n} ---
# Busca exactamente la cantidad de veces que digas.
text = "aaaaa-------aaa-----aa"
patter = r"a{3}" # Busca grupos de exactamente tres letras 'a'.
matches = re.findall(patter, text)
# En "aaaaa" encuentra 3 y sobran 2 (que no llegan a ser 3). Luego encuentra otro trío.
print("Matches para exactamente 3 'a':", matches)

# --- RANGO {n, m} ---
# Busca un mínimo de 'n' y un máximo de 'm'.
text = "uuu uuu u uuu u u uuu"
patter = r"u{2,3}" # Busca entre 2 y 3 letras 'u'.
matches = re.findall(patter, text)
print("Secuencias de 2 a 3 'u':", matches)

# EJERCICIO PALABRAS: Palabras de entre 4 y 6 letras.
# \b es el "límite de palabra" (evita que agarre pedazos de palabras largas).
words = "ala casa arbol leon circo murci guacamayo pionono"
patter = r"\b\w{4,6}\b" # \w son letras. Busca palabras de 4, 5 o 6 letras.
matches = re.findall(patter, words)
print("Palabras de 4 a 6 letras:", matches)

# EJERCICIO CÓDIGO POSTAL: Exactamente 4 o 6 dígitos.
digit_text = "Los codigos postales son 280132, 0218001, 46020 y 5000"
# Cambiamos el patrón para que busque exactamente 6 dígitos o 4 según tu código.
patter = r"\b\d{6}\b|\b\d{4}\b" 
matches = re.findall(patter, digit_text)    
print("Códigos de 4 o 6 dígitos:", matches)