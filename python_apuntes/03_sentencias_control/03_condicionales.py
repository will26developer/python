string: str = input("Edad:")

try:
    edad: int = int(string)
    if edad > 0 and edad < 18:
        print("Eres menor de edad")
    elif edad > 18 and edad < 35:
        print("Eres adulto")
    elif edad > 35 and edad <= 50:
        print("Eres un adulto de mediana edad")
    elif edad > 50 and edad <= 70:
        print("Esta en la mitad de tu vida")
    elif edad > 70:
        print("Estas en la vejez")
    else:
        print("Aun no has nacido")
except ValueError as e:
    print(f"Error: {e}")
