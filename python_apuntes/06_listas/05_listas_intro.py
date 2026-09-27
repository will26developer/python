#Listas introduccion

#Inicializando listas de dos maneras
nombres: list[str] = ['William', 'George', 'Pedro', 'Alberto','Jose','Pablo']
numeros: list[int] = list(range(1,20))
print(nombres,numeros)

#Accediendo a los elementos de la lista por indice
print(nombres[1],numeros[4])

#Indices negativos en listas
print(nombres[-2],numeros[-3])

#Slicing de listas
print(nombres[0:3],numeros[2:6])
print(nombres[::2],numeros[::2])
print(nombres[1::2],numeros[1::2])
print(nombres[::-1],numeros[::-1])

#Modificando listas accediendo a su posicion
nombres[1] = "Fernando"
numeros[4] = 42
print(nombres,numeros)