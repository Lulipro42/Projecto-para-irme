###
# 05 - Entrada de usuario(input()) - Version simplificada
# La funcion input() permite obter datos del usuiario a traves de la consola
###

nombre = "Ulises"
print(type(nombre))


nombre = input("Hola, ¿como te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("¿Cuantos años tienes?\n")
try:
    age = int(age)
    print(f"Tenes {age} años")
except ValueError:
    print("Por favor, ingresa tu edad como un número entero.")

print("Obtener multiples valores a la vez")
try:
    # Usamos .split(' ', 1) para dividir la entrada solo en el primer espacio.
    # Esto permite que la ciudad pueda tener espacios en su nombre (ej: "La Plata").
    entrada = input("¿En que pais y ciudad vives? (ej: Argentina La Plata)\n")
    country, city = entrada.split(' ', 1)
    print(f"Vives en {country}, {city}")
except ValueError:
    print("Error: Debes ingresar un país y una ciudad separados por un espacio.")
