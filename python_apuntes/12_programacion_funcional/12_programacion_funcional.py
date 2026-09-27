#Programacion funcional

#Funcion pura vs impura - el contraste que hay que interiorizar
total: int = 0

def sumar_impura(n: int) -> int:
    global total
    total += n  # efecto secundario - modifica algo fuera de la funcion
    return total

def sumar_pura(a: int, b: int) -> int:
    return a + b  # mismo input, siempre mismo output, sin tocar nada externo

print(sumar_pura(3, 4))
print(sumar_pura(3, 4))  # siempre 7, garantizado


#Funciones de orden superior - map, filter, reduce formalizados

from functools import reduce

numeros: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#map - transforma cada elemento
dobles: list[int] = list(map(lambda n: n * 2, numeros))
print(dobles)

#filter - selecciona elementos segun condicion
pares: list[int] = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)

#reduce - reduce toda la secuencia a un unico valor
suma_total: int = reduce(lambda acc, n: acc + n, numeros)
print(suma_total)

#reduce con valor inicial
producto_total: int = reduce(lambda acc, n: acc * n, numeros, 1)
print(producto_total)


#Composicion de funciones - encadenar funciones simples

def duplicar(n: int) -> int:
    return n * 2

def incrementar(n: int) -> int:
    return n + 1

def componer(f, g):
    return lambda x: f(g(x))

duplicar_e_incrementar = componer(incrementar, duplicar)
print(duplicar_e_incrementar(5))  # duplicar(5)=10, incrementar(10)=11


#functools.partial - fija argumentos, crea version "precargada"
from functools import partial

def potencia(base: int, exponente: int) -> int:
    return base ** exponente

cuadrado = partial(potencia, exponente=2)
cubo = partial(potencia, exponente=3)
print(cuadrado(5))
print(cubo(5))


#functools.lru_cache - memoizacion automatica
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))  # rapido gracias a la cache, sin ella seria muy lento


#itertools - modulo pensado para FP
import itertools

#chain - concatena varios iterables sin crear una lista intermedia
letras: list[str] = ['a', 'b', 'c']
combinado = itertools.chain(numeros, letras)
print(list(combinado))

#accumulate - como reduce pero devuelve TODOS los pasos intermedios
acumulados: list[int] = list(itertools.accumulate(numeros))
print(acumulados)

#islice - "slicing" para iteradores/generadores (que no admiten [0:5])
primeros_cinco = list(itertools.islice(numeros, 5))
print(primeros_cinco)

#starmap - como map, pero desempaqueta tuplas como argumentos
pares_numeros: list[tuple[int, int]] = [(2, 3), (4, 5), (6, 7)]
sumas: list[int] = list(itertools.starmap(lambda a, b: a + b, pares_numeros))
print(sumas)