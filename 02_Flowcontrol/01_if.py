###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###
import os
import platform

# Limpiar la consola según el sistema operativo
os.system("cls" if platform.system() == "Windows" else "clear")

print("\n Sentencias simple condicionada")

edad = 18
if edad >= 18: 
    print("Eres mayor de edad.")
    print("¡Felicidades!")

edad = 15 
if edad >= 18: 
    print("Eres mayor de edad.")
    print("¡Felicidades!")
else:
    print("Eres menor de edad.") # Añadido para claridad

print("\n Sentencia condicionada con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
        
print("\n Sentencia condicionada con elif")
nota = 1
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >=5:
    print("Aprobado")
else:
    print("No estas calificado")
    
print("\n Sentencia condicionada multimples")
edad = 25
tiene_carnet = True

# JavaScritp
# && -> and
# || -> or

if edad >= 18 and tiene_carnet:
    print("podes andar en auto")
    
else:
    print("POLICIA")
    
# un pueblo chico san juan
if edad >= 18 or tiene_carnet:
    print("podes andar en auto")
else:
    print("Si le pagas a la policia podes andar en auto")
    
es_fin_de_semana = True
if not es_fin_de_semana:
    print("A estudiar!")
else:
    print("Es fin de semana, ¡a descansar!")
    
print("\n Anidar condicionales")

tiene_plata = True
edad = 24
if edad >= 18:
    if tiene_plata:
        print("Vamos a la joda")
    else:
        print("Nos quedamos en casa")
else:
        print("No podes ir a la joda")

# Mas facil de leer
# if edad < 18:
#     print("No podes ir a la joda")
# else:
#    if tiene_plata:
#        print("Vamos a la joda total pago yo")
#    else:
#        print("Quedate en house")    

numero = 5
if numero: # True
    print("El numero no es cero")

numero = 0
if numero: # False
    print("Aqui no entrara nunca")
    
nombre = ""
if nombre:     
    print("el nombre no es vacio")
# variable un =
# comparacion dos ==
    
numero = 3 # Asignacion
es_el_tres =  numero == 3 # Comparacion

if es_el_tres:
    print("El numero es tres")
    
print("\n La condicion terniaria:")
# es una forma concisa de un  if-else en una linea de codigo
# (codigo si cumple la condicion) if (y si no cumple la condicion si no cumple) else

edad = 17 
mensaje = "eres mayor de edad" if edad >= 18 else "eres menor de edad"
print(mensaje)


