import calendar
from datetime import datetime

current_date: datetime = datetime.now()
print(f"Current date: {current_date}")

days: list[str] = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
day_index = current_date.weekday()
week_name: str = days[day_index]
print(f"Hoy es: {week_name}")

if calendar.isleap(current_date.year):
    print(f"{current_date.year} is a leap year")
else:
    print(f"{current_date.year} is not a leap year")

print("Calendario mes actual")
print(calendar.month(current_date.year, current_date.month))

first_weekday,days_in_month = calendar.monthrange(current_date.year, current_date.month)
print(first_weekday)
print(days_in_month)

modified_date = current_date.replace(year=1996,month=4,day=3,hour=7,minute=45,second=18)
print(modified_date)