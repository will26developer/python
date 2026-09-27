#Tuplas

coordenadas: tuple[int, int] = (3, 7)
nombres: tuple[str, ...] = ('William', 'George', 'Pedro', 'William')
print(coordenadas, nombres)

#Tupla de un solo elemento - coma obligatoria
un_elemento: tuple[int] = (5,)
print(un_elemento, type(un_elemento))

#Indexado y slicing (igual que listas)
print(nombres[0], nombres[1:3], nombres[::-1])

#Metodos (solo 2, por ser inmutable)
print(nombres.count('William'))
print(nombres.index('Pedro'))

#Las tuplas son inmutables - esto lanzaria TypeError:
#nombres[0] = "Otro"

#Desempaquetado, muy tipico en tuplas
x, y = coordenadas
print(x, y)