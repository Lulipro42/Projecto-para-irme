###
# 02- boleeanos
# Valores logicos: True y False
# Fundamentos para el control de flujo y la logica de programacion
###

# Los booleanos representan valores de verdad: true (verdadero) y false (falso)
print("Valores booleanos basicos")
print(True)
print(False)

# Operadores de comparacion
print("\n Operadores de comparacion")
print("5 > 3", 5 > 3)      # True
print("5 < 3", 5 < 3)      # False
print("5 >= 3", 5 >= 3)     # True
print("5 <= 3", 5 <= 3)     # False

print("\n Comparacion de cadenas")
print("banana < pera", "banana" < "pera")
print("'Hola' == 'hola'", "Hola" == "hola")

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False
print("not False:", not False)            # True

# tablas de verdad (para referencia)
print("\nTabla de verdad para AND:")
print("A\tB\tA and B")
print("True\tTrue\t", True and True)
print("True\tFalse\t", True and False)
print("False\tTrue\t", False and True)
print("False\tFalse\t", False and False)

# tabla de OR
print("\nTabla de verdad para OR:")
print("A\tB\tA or B")
print("True\tTrue\t", True or True)
print("True\tFalse\t", True or False)
print("False\tTrue\t", False or True)
print("False\tFalse\t", False or False)
print("\nTabla de verdad para NOT:")

# tabla de NOT
print("A\tnot A")
print("True\t", not True)
print("False\t", not False)
