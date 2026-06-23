usuario = ("Escribi tu nombre:")
clave = ("Escribi tu clave:")

# El len(clave) te dice cuantaas letras tiene 

if len(clave) > 8 and clave != usuario:
    print("Acceso creado con exito")
else:
    print("Error: La clave es corta o igual al nombre")
    
compras = []

while true:
    item = input("¿Que queres comprar? (o esciribi 'salir'):")
    
    if item == 'salir':
        break
    
    if item in compras:
        print("!Ese ya lo puimos!")
    else:
        compras.append(item)
        print(f"{item} agregado.")