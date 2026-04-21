# 1. Introducción a las Clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

# ejemplo basico de una clase
class Coche:
  # atributo de clase (comparte todas las instancias)
  tipo = "vehículo de cuatro ruedas"
  ruedas = 4

  # método especial que es el que construye el objeto
  # se llama automáticamente este método cuando creas la instancia
  def __init__(self, marca, modelo, color):
    # atributos de la instancia
    self.marca = marca
    self.modelo = modelo
    self.color = color

  def arrancar(self):
    print(f"El coche {self.marca} {self.modelo} arrancó! 🚗")


mi_coche = Coche("Toyota", "Corolla", "rojo")
mi_coche.arrancar()

print(mi_coche.marca)
print(mi_coche.tipo)

coche_de_pheralb = Coche("Ford", "Fiesta", "azul")
coche_de_pheralb.arrancar()

print(coche_de_pheralb.marca)


# encapsulación: es ocultar los detalles internos de una clase y exponer solo lo necesario

# crear una clase para llaar a la IA de openai, deepseek O LO QUE SEA

import requests

class AI_API:
  def __init__(self, api_key, url, model):
    self.api_key = api_key
    self.url = url
    self.model = model

  def call(self, prompt):
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {self.api_key}"
    }
    data = {
      "model": self.model,
      "messages": [{"role": "user", "content": prompt}]
    }

    try:
      response = requests.post(self.url, json=data, headers=headers)
      res_json = response.json()

      if response.status_code == 200:
        print(res_json["choices"][0]["message"]["content"])
      else:
        print(f"Error {response.status_code}:", res_json)
    except requests.exceptions.RequestException as e:
      print(f"Error en la solicitud: {e}")
      return None

print("\nDEEPSEEK:")
DEEPSEEK_API_KEY = "sk-8b9a56ebeab0496d953f7b911e61afdf"
deepseek_api = AI_API(DEEPSEEK_API_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")

deepseek_api.call("Escribe un breve poema sobre la programación")