# PRINCIPIO DE INVERSIÓN DE DEPENDENCIA (DIP)
# Este principio establece dos cosas fundamentales:
# 1. Los módulos de alto nivel no deben depender de módulos de bajo nivel. 
#    Ambos deben depender de abstracciones.
# 2. Las abstracciones no deben depender de los detalles. 
#    Los detalles deben depender de las abstracciones.

from abc import ABC, abstractmethod

# --- PROBLEMA (Violando DIP) ---
# Aquí la clase 'Usuario' (Alto nivel) depende directamente de 'MySQLDatabase' (Bajo nivel).
# Si queremos cambiar a MongoDB, tenemos que modificar la clase Usuario.

class MySQLDatabase:
    def guardar(self, datos):
        print(f"Guardando {datos} en MySQL...")

class UsuarioService_Error:
    def __init__(self):
        self.db = MySQLDatabase() # Dependencia rígida

    def crear_usuario(self, nombre):
        self.db.guardar(nombre)

# --- SOLUCIÓN (Siguiendo DIP) ---
# Creamos una interfaz (abstracción) para que ambos dependan de ella.

class InterfaceBaseDeDatos(ABC):
    @abstractmethod
    def guardar(self, datos):
        pass

class MySQL(InterfaceBaseDeDatos):
    def guardar(self, datos):
        print(f"Guardando {datos} en MySQL de forma segura")

class MongoDB(InterfaceBaseDeDatos):
    def guardar(self, datos):
        print(f"Guardando {datos} en MongoDB (NoSQL)")

class UsuarioService:
    def __init__(self, base_de_datos: InterfaceBaseDeDatos):
        # Ahora no depende de una clase específica, sino de la interfaz
        self.db = base_de_datos

    def crear_usuario(self, nombre):
        self.db.guardar(nombre)

# Uso: Podemos intercambiar la base de datos sin tocar el código de UsuarioService
db_mysql = MySQL()
db_mongo = MongoDB()

servicio = UsuarioService(db_mongo) # Inyectamos la dependencia
servicio.crear_usuario("Ulises")

# Esto hace que el código sea mucho más fácil de mantener y testear.


class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Dicconario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        pass

class CorrectorOrtografioc:
    def __init__(self, verificador):
        self.verificador = verificador
    
    def corregir_texto(self, texto)
    # USAMOS EL VERIFCIADO
    