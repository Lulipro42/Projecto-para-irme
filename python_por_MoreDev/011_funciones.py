### FUNCIONES ###

# Las funciones son para resolver problemas con ellas es decir una funcion va a resolver un problema en concreto

# Surge un error al poner mi_funcion() el entre parentesis junto y se escribiria corretamente separado osea asi mi_funcion ()
def mi_funcion ():
    print("Esto es una funcion")
    
mi_funcion ()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)
    
# Hay un error que al poner otro numero osea 3 sale un TypeError debido a que en el print solo esta el primer y segundo numero
sum_two_values (6,7)
sum_two_values (6242,7552)
sum_two_values (612,-21)
# En este caso solo se unen no se suman ya que son una cadena de texto
sum_two_values ("2", "4")

# SIGUIENTE FUNCION que ene vez de recibir tiene que retornarlos

def sum_two_values_with_retur (first_number, second_number):
    return first_number + second_number


mi_resultado = sum_two_values_with_retur (10,6)
print(mi_resultado)

mi_resultado = sum_two_values (1.4, 2.4)
print(mi_resultado)


def print_name (name, surname):
    print(f"{name} {surname}") # La f sirve para acceder a esos parametros osea el name y el surname
    
print_name(surname = "Ulises", name= "Solis") # con este metodo lo puedo modificar como yo quiera

def print_name_with_default (name, surname, alias="Sin alias"): # con esto al no ponerse un alias se desconoce el texto entonces suelta ese sin alias
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Ulises", "Solis", )

# el * sirve para cuando quiero poner mas de una palabra o los que se me de la gana
def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
        
print_upper_texts("Hola","Luli","Pro")