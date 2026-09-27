from datetime import datetime
import locale

now: datetime = datetime.now()
print(f"La fecha actual es: {now}")

date_time: datetime = datetime(2026,9,27,13,5,21)
print(date_time)
print(date_time.year)
print(date_time.month)
print(date_time.day)
print(date_time.hour)
print(date_time.minute)
print(date_time.second)

date_format: str = date_time.strftime("%d/%m/%Y %H:%M:%S")
print(date_format)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
date_format: str = date_time.strftime("%d de %B del %Y")
print(date_format)