###
# 04 - variables()
#Las variables sirven para guardar datos en memoria
#Python es un leguaje de tipado dinamucio y tipado fuerte
# Asignar una variable
# solo hace falta poner esto
my_name = "ulises"

###

#  print(my_name)

edad = 32
# print(edad)

# edad = 17 
# print(edad)

# Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion que no tienes que declaralo explicitamente
name = "ulises"
print(type(name))

name = 17 
print(type(name))

# Tipado fuerte: Python no reliza conversione de tipo automatico
# print(10 + "2")
# f-string (literal de cadena de formarto)
print (f"Hola {my_name}, tengo {edad + 5} años")

# No recomendada forma de asignar variables
name, edad, city = "ulises", 32, "La Plata"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

MiNombreDeVariable = "ko" # Pascalcase
minombredevariable = "ko" # todpjunto

MI_CONSTANTE = 3.14

# nombres no validos en variables 
# 123123_variable = "ko"
# mi-variable = "ko"
# mi variable = "ko"


is_user_logged_in: bool = True
print(is_user_logged_in)

