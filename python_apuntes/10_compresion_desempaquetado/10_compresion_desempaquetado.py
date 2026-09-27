#Comprehensions

numeros: list[int] = list(range(1, 11))
print(numeros)

#List comprehension basica
cuadrados: list[int] = [n**2 for n in numeros]
print(cuadrados)

#Con condicion (filtro)
pares: list[int] = [n for n in numeros if n % 2 == 0]
print(pares)

#Con if/else en la propia expresion (distinto del filtro)
etiquetas: list[str] = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(etiquetas)

#Set comprehension
cuadrados_unicos: set[int] = {n**2 % 10 for n in numeros}
print(cuadrados_unicos)

#Dict comprehension
cuadrados_dict: dict[int, int] = {n: n**2 for n in numeros}
print(cuadrados_dict)

#Generator expression - fijate que no imprime valores, imprime el objeto generador
generador = (n**2 for n in numeros)
print(generador)
print(list(generador))  # aqui si se consume y se ven los valores

#Comprehension anidada
matriz: list[list[int]] = [[f * c for c in range(3)] for f in range(3)]
print(matriz)


#Desempaquetado

coordenadas: tuple[int, int, int] = (10, 20, 30)
x, y, z = coordenadas
print(x, y, z)

#Con asterisco - recoge "el resto"
primero, *resto = numeros
print(primero, resto)

*inicio, ultimo = numeros
print(inicio, ultimo)

primero, *medio, ultimo = numeros
print(primero, medio, ultimo)

#Intercambio sin variable temporal
a, b = 1, 2
a, b = b, a
print(a, b)

#Fusionar listas y diccionarios con desempaquetado
lista1: list[int] = [1, 2, 3]
lista2: list[int] = [4, 5, 6]
fusion: list[int] = [*lista1, *lista2]
print(fusion)

dict1: dict[str, int] = {"a": 1, "b": 2}
dict2: dict[str, int] = {"b": 99, "c": 3}
fusion_dict: dict[str, int] = {**dict1, **dict2}
print(fusion_dict)  # dict2 sobrescribe la clave repetida "b"

#Desempaquetado al llamar funciones
def sumar_tres(a: int, b: int, c: int) -> int:
    return a + b + c

valores: list[int] = [10, 20, 30]
print(sumar_tres(*valores))