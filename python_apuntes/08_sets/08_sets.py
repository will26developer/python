#Sets

numeros: set[int] = {1, 2, 3, 4, 5}
otros: set[int] = {4, 5, 6, 7, 8}
print(numeros, otros)

#Añadir/quitar
numeros.add(10)
print(numeros)

numeros.update([11, 12, 13])
print(numeros)

numeros.discard(100)  # no existe, pero no da error
print(numeros)

#Los duplicados se ignoran automaticamente
duplicados: set[int] = {1, 1, 2, 2, 3}
print(duplicados)

#Operaciones de conjuntos
print(numeros.union(otros))
print(numeros.intersection(otros))
print(numeros.difference(otros))
print(numeros.symmetric_difference(otros))
print(numeros & otros)  # equivalente a intersection
print(numeros | otros)  # equivalente a union

print({1, 2}.issubset(numeros))
print(numeros.isdisjoint({999, 1000}))