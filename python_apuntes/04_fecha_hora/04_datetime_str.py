import locale
from datetime import datetime

text: str = "17/04/2025 13:11"
date_time: datetime = datetime.strptime(text, "%d/%m/%Y %H:%M")
print(date_time)
print(date_time.year)
print(date_time.month)

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
date_str: str = "18 de agosto, 2026"
format: str = "%d de %B, %Y"
date_obj: datetime = datetime.strptime(date_str, format)
print(date_obj)

try:
    date_str: str = "15 de septiembre, 2026 - 02:30 PM"
    format: str = "%d de %B, %Y - %I:%M %p"
    date_obj: datetime = datetime.strptime(date_str, format)
    print(datetime.strftime(date_obj, "%d de %B, %Y - %I:%M %p"))
except ValueError as err:
    print("Error en el formato de fecha", err)