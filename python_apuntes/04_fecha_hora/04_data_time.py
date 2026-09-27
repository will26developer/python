from datetime import date

today: date = date.today()
print(f"Today: {today}")
print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")

birthday: date = date(1996,4,3)
print(f"Birthday: {birthday}")