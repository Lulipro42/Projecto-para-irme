# EL DECORADOR TOMA UNA FUNCIJON COMO ENTRADA Y LA MODIFICA UN POCO NO MUCHO, ES SOLO PARA AGRGARLE FUNCIONALIDAD Y LA DEVULEVE MEJOR 
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
    return funcion_modificada

#def saludo():
    #print("Hola luli, como ")
    
#saludo_modificado = decorador(saludo)
#saludo_modificado()
@decorador # EL DECORADOR SIRVE PARA HACER VALIDACIONES POR EJ: A LAS 9 ABRE LA PANADERIA 
def saludo(): 
    print("Hola dalto como estas")

saludo()