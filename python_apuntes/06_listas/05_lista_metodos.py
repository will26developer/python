#Metodos de listas

numeros: list[int] = list(range(1,20))
print(numeros)

#Añadir elementos
numeros.append(20)
print(numeros)

numeros.extend([21, 22, 23])
print(numeros)

numeros.insert(0, 0)
print(numeros)

#Quitar elementos
numeros.remove(0)
print(numeros)

ultimo = numeros.pop()
print(ultimo, numeros)

penultimo = numeros.pop(-2)
print(penultimo, numeros)

#Buscar / contar
print(numeros.index(10))
print(numeros.count(10))

#Ordenar / invertir (in-place)
numeros.sort(reverse=True)
print(numeros)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

#len() - cuenta elementos
print(len(numeros))

#Copiar
copia: list[int] = numeros.copy()
copia.append(999)
print(numeros, copia)  # numeros no se ve afectada

#Concatenar y repetir
extra: list[int] = numeros + [100, 200]
print(extra)

repetida: list[int] = [0] * 5
print(repetida)

#Clear - vacia la lista
copia.clear()
print(copia)

#EL ERROR CLASICO: append/sort/reverse devuelven None
resultado = numeros.append(999)
print(resultado)  # None, no la lista