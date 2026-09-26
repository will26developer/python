# Bucle for

# Iterando con bucles for utilizando range
for i in range(1, 11):
    print(f"Numero: {i}")

for i in range(1, 11, 2):
    print(f"Numero en saltos de dos: {i}")

for x in range(10, 0, -1):
    print(f"Numero en orden inverso: {x}")


# Iterando sobre un array
nombres: list[str] = ["Pedro", "Alberto", "Jose"]
for nombre in nombres:
    print(f"Nombre: {nombre}")

# Iterando una cadena y multiplicado cada  letra por su indice con ayuda de enumerate
nueva_cadena: str = ""
cadena: str = "RxyUpqv"

for indice, letra in enumerate(cadena):
    if indice != 0:
        nueva_cadena += letra * indice
    else:
        nueva_cadena += letra

print(f"Nueva cadena: {nueva_cadena}")

# Iterando dos arrays a la vez con zip
from random import randint
from string import ascii_uppercase

numeros_aleatorios: list[int] = [randint(1, 100) for _ in range(1, 10)]
letras: list[str] = [ascii_uppercase[i] for i in range(10)]

for k, v in zip(letras, numeros_aleatorios):
    print(f"{k}: {v}")

# Bucle while
# Iterando dos arrays utilizando un bucle while
index1: int = 0
index2: int = 0
print("Iterando clave valor con un while")
while index1 < len(letras) - 1 and index2 < len(numeros_aleatorios) - 1:
    print(f"{letras[index1]} : {numeros_aleatorios[index2]}")
    index1 += 1
    index2 += 1
