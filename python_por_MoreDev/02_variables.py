# variales 
#Las variables sirven para guardar datos en memoria
#Python es un leguaje de tipado dinamucio y tipado fuerte
# Asignar una variable
# solo hace falta poner esto

# para maracar una variable es en snake case osea asi hola_mundo

# String
my_name = "Ulises"
print(my_name)

# Int(numero)
my_int_variable = 6 
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Booleano
my_bool_variable = False
print(my_bool_variable)

# concateacion de variables en un print
# Esto sirve que va a madandar diferentes datos en cadenas de texto
print(my_name, my_int_variable, my_bool_variable)
# otra forma de seguir concatenando
print("Este es el valor de:", my_bool_variable)

# funciones del sistema
# los tipos len solo cuentan los caracteres como solo la variable que seria mi_nombre solo eso no lo de = para adelante no
print(len(my_name))

# variables en una sola linea para poder ahorrar codigo
# esta bueno hacerlo pero es complicado despues arreglarlo si fallas en algo
name, surname, alias, edad = "Ulises", "Solis", "lulipro", "17"
print("Me llamo:", name, surname,".Mi alias es:", alias,"y mi edad es ", edad)

# inputs(responder cosas en la terminal)
"""
first_city = input("¿Donde vives")
age = input("cuantos años tienes")

print(first_city)
print(age)

"""
# cambiamos su tipo 
name = "lazaro"
edad = "71"
print(name)
print(edad)

# Forzamos el tipo
address: str = "Mi direccion"
address = "32"

print(type(address))