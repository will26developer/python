from datetime import date, timedelta
from datetime import datetime

today: date = date.today()
birth_date: date = date(1996,4,3)
#birth_str: str = input("Ingresa tu fecha de cumple, %d-%m-%Y:")
#birth_date: date = datetime.strptime(birth_str, "%d-%m-%Y")

if (today == birth_date):
    print(f"Las fechas {today} y {birth_date} son iguales")
elif today > birth_date:
    print(f"La fecha de cumple {birth_date} es mas antigua que {today}")
elif today < birth_date:
    print(f"La fecha de cumple {birth_date} es mas reciente {today}")

event: datetime = datetime(2026,9,27,13,20)
event2: datetime = datetime(2026,9,27,13,45)

print(event < event2)
print(event > event2)
print(event == event2)

new_date: timedelta = event2 - event
new_date2: datetime = event2 + timedelta(weeks=1, days=3)
print(new_date)
print(new_date2)
