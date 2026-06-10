# PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
# Este principio dice que si "B" es una subclase de "A", entonces deberíamos 
# poder usar objetos de la clase "B" en cualquier lugar donde se use "A" 
# sin que el programa se rompa o se comporte de forma inesperada.

class Ave:
    def volar(self):
        return "Estoy volando"

class Gorrion(Ave):
    def volar(self):
        return "El gorrión vuela alto"

class Pinguino(Ave):
    # ¡PROBLEMA! Un pingüino es un ave, pero NO vuela.
    # Si forzamos a que herede 'volar', estamos rompiendo el principio LSP
    # porque el programa esperará que todas las aves vuelen.
    def volar(self):
        return "No puedo volar"

# --- FORMA CORRECTA SIGUIENDO LSP ---

class AveCorrecta:
    pass

class AveVoladora(AveCorrecta):
    def volar(self):
        return "Estoy volando"

class AveNoVoladora(AveCorrecta):
    def caminar(self):
        return "Estoy caminando"

def hacer_volar(ave: AveVoladora):
    print(ave.volar())

# Ahora el sistema es seguro. Solo pasamos aves que realmente vuelan.
piolin = Gorrion()
print(piolin.volar())

# Nota: LSP nos obliga a diseñar jerarquías donde las subclases realmente 
# cumplan con el contrato de la clase padre.


class Ave2:
    pass


class AveVoladora2:
    def volar2(self):
        return "Estoy volando"
    
class AveNoVoladora1:
    pass