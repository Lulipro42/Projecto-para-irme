# EL PRINCIPIO DE ABIERTO/CERRADO (OCP)
# Las clases deben estar abiertas para la extensión (podemos agregar nuevas funcionalidades)
# pero cerradas para la modificación (no debemos cambiar el código que ya funciona).

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        # raise NotImplementedError sirve para obligar a las clases hijas a implementar este método.
        # Es una forma de crear una "interfaz" o contrato.
        raise NotImplementedError




class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")


class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"ENviando SMS a: {self.usuario.sms}")


class NotificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje a: {self.usuario.whatsapp}")



# EXTENSIÓN: Si queremos notificar por Email, creamos una nueva clase.
# No modificamos la clase 'Notificador' original.
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando EMAIL a {self.usuario.email}: {self.mensaje}")

# EXTENSIÓN: Si mañana queremos notificar por SMS, solo agregamos esta clase.
class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.telefono}: {self.mensaje}")

# ¿Por qué es útil? 
# Porque si agregamos 10 formas nuevas de notificar, el código original de 'Notificador' 
# se mantiene intacto y sin errores, evitando romper lo que ya funcionaba.

# Nota: Este concepto se complementa con las "Clases Abstractas" que viste en otro archivo.