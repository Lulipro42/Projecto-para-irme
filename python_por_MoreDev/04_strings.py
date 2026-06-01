### Strings ###

mi_string = "Mi string"
mi_other_string = "Mi otro string"

print(mi_string)
print(mi_other_string)

# concatenar
print(mi_string + " " + mi_other_string)

# los strings pueden llevar cierto caracteres y ademas el \n hace que las palabras adelante de ese n vallan para abajo
mi_nueva_linea_string = "este es un string \n con salto de linea"
print(mi_nueva_linea_string)

# esto es una tabulacion la \t
mi_tab_string = "\t este es un caracter especial"
print(mi_tab_string)

# el doble \\ hace que parece que estan atrapados
mi_escape_string = "\\t este es un string \\n escapado"
print(mi_escape_string)

# Formateo

# las cosas como nombre o alias o edad es llamado VARIABLE/S
nombre, alias, edad = "ulises", "pro", 17

print('mi nombres es {} {} y mi edad es {}'.format(nombre, alias, edad))
print('mi nombres es %s %s y mi edad es %d'%(nombre, alias, edad))
# inferencia de datos este es la MEJOR por midudev y mouredev
print(f"mi nombre es {nombre} {alias} y mi edad es {edad}")


# Desempaquetado de caracteres el error al solo poner a, b es que la palbra python tiene mas caracteres por ende tenes que poner mas letras 
lenguage = "python"
a, b, c, d, e, f = lenguage
print(a)
print(b)

# Division 

# el [1:3] en realidad se cuenta desde el 0 osea python seria p[0] y[1] t[2] h[3]
lenguage_slice = lenguage[1:3]
print(lenguage_slice)

# el [1:] ya abarcaria toda la palabra
lenguage_slice = lenguage[1:]
print(lenguage_slice)

# no comprendi porque es el [-2] despues lo veo bien
lenguage_slice = lenguage[-2]
print(lenguage_slice)

lenguage_slice = lenguage[0:3]
print(lenguage_slice)

# reverse

# El [::-1] da toda la vuelta
reversed_lenguage = lenguage[::-1]
print(reversed_lenguage)

# funciones
#pone en mayuscula la primera palabra
print(lenguage.capitalize())
# hace lo mismo
print(lenguage.upper())
# cuenta los caracteres que les indices
print(lenguage.count("y"))
#no se
print(lenguage.isnumeric())
# las pone en minusculas ahora
print(lenguage.lower())
# concateno dos (concatenar es juntar dos cosas) es True porque los dos son upper 
print(lenguage.upper().isupper())
# en cambio si le cambie por islower es false
print(lenguage.upper().islower())
# Se referie a con que palabras empieza la letra en este caso yo puse py y es true
print(lenguage.startswith("py"))