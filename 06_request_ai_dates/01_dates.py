# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Configurar la localización a español
# esto es para obtener la fecha y hora actuales
now = datetime.now()
print("Fecha y hora actuales:", now)
print("Año:", now.year)

# 2. crear una fecha y hora específica
specific_date = datetime(2026, 11, 12, 7, 30, 53)
print ("Fecha y hora específica:", specific_date)


# formartear fechas y horas
# metodo starftime() se usa para formatear fechas y horas
# pasar el objeto datetime y el formato deseado como una cadena
# formato:
format_date = now.strftime("%d/%m/%y %H:%M:%S")
print("Fecha formateada (dd/mm/yy):", format_date)

# 4. operaciones con fechas y horas (sumar/restar dias, horas, etc.)
yesterday = datetime.now() - timedelta(days=1, hours=2, minutes=30)
print("Ayer fue:", yesterday)
# tiedelta es para quitarle la fecha a la fecha actual
one_hour_after = datetime.now() + timedelta(hours=1)
print("Dentro de una hora será:", one_hour_after)

# 5. obtener compoonnetes individuales de una fecha
año = now.year
print("Año actual:", año)

mes = now.month
print("Mes actual:", mes)

# 6. calcular la diferencia entre dos fechas
future_date = datetime(2024, 12, 25)
difference = future_date - now
print("Días hasta Navidad 2024:", difference.days)

# 7.