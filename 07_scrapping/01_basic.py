import requests  # Importa la librería para hacer peticiones a internet (como si fueras un navegador)
import re        # Importa 'Regular Expressions', una herramienta para buscar patrones de texto específicos

# La URL de la página que queremos "espiar" o analizar
url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'

# Enviamos una petición GET a la URL. El servidor de Apple responde y guardamos todo en 'response'
response = requests.get(url)
def    
# El status_code 200 significa "OK". Si es 200, la web nos dio permiso y cargó bien.
if response.status_code == 200:
    print('La petición fue exitosa')

    # Guardamos todo el código fuente de la página (el HTML) en esta variable
    html = response.text
    
    # Imprimimos el código (ojo, esto va a llenar la consola de texto porque el HTML es gigante)
    print(html)

    # --- BUSCANDO EL PRECIO ---
    # Definimos un patrón: buscamos el texto que esté adentro de las etiquetas <span> con esa clase
    # El (.*?) es un "comodín" que dice: "atrapá todo lo que encuentres aquí adentro"
    price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'
    
    # re.search busca ese patrón en todo el código HTML que bajamos
    match = re.search(price_pattern, html)

    if match:
        # .group(1) nos da solo el contenido que atrapó el comodín (.*?), o sea, el precio
        print(f"El precio del producto es: {match.group(1)}")

    # --- BUSCANDO EL TÍTULO ---
    # Las webs guardan su nombre entre las etiquetas <title>...</title>
    title_pattern = r'<title>(.*?)</title>'
    match = re.search(title_pattern, html)

    if match:
        # Esto imprimirá algo como "Comprar MacBook Air - Apple (ES)"
        print(f"El título de la web es: {match.group(1)}")

else:
    # Si el servidor nos bloquea o la URL no existe (ej: error 404), entraría acá
    print(f"Error al acceder a la web. Código: {response.status_code}")