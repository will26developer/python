#Funciones

#Definicion basica con type hints
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

print(saludar("William"))

#Parametros con valor por defecto
def presentar(nombre: str, edad: int = 18) -> str:
    return f"{nombre} tiene {edad} años"

print(presentar("William"))
print(presentar("William", 30))

#Args posicionales variables
def sumar_todos(*numeros: int) -> int:
    return sum(numeros)

print(sumar_todos(1, 2, 3, 4, 5))

#Kwargs - argumentos nombrados variables
def crear_perfil(**datos: str) -> dict[str, str]:
    return datos

print(crear_perfil(nombre="William", ciudad="España", lenguaje="Python"))

#Combinando todo - orden obligatorio: normales, *args, con-default, **kwargs
def funcion_completa(a: int, b: int, *args: int, c: int = 10, **kwargs: str) -> None:
    print(a, b, args, c, kwargs)

funcion_completa(1, 2, 3, 4, 5, c=99, extra="dato")

#Parametros solo-posicionales (/) y solo-nombrados (*)
def dividir(a: int, b: int, /, *, redondear: bool = False) -> float:
    resultado = a / b
    return round(resultado) if redondear else resultado

print(dividir(10, 3))
print(dividir(10, 3, redondear=True))
#dividir(a=10, b=3)  # esto daria error, a y b son solo-posicionales

#Scope - local vs global
contador: int = 0

def incrementar() -> None:
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)

#Nonlocal - para closures
def contador_externo():
    cuenta: int = 0
    def incrementar_interno() -> int:
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return incrementar_interno

mi_contador = contador_externo()
print(mi_contador())
print(mi_contador())
print(mi_contador())

#Funciones como ciudadanos de primera clase
def cuadrado(n: int) -> int:
    return n ** 2

def aplicar_funcion(funcion, valor: int) -> int:
    return funcion(valor)

print(aplicar_funcion(cuadrado, 5))

#Recursion
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


#Lambdas

#Lambda basica - equivalente a la funcion cuadrado de antes
cuadrado_lambda = lambda n: n ** 2
print(cuadrado_lambda(5))

#Con varios parametros
sumar = lambda a, b: a + b
print(sumar(3, 4))

#Donde de verdad se usan - como argumento inline de otras funciones
numeros: list[int] = [5, 2, 8, 1, 9, 3]

#sorted con key
print(sorted(numeros, key=lambda n: -n))  # orden descendente

personas: list[dict[str, int]] = [
    {"nombre": "William", "edad": 30},
    {"nombre": "George", "edad": 25},
]
print(sorted(personas, key=lambda p: p["edad"]))

#map - aplica la lambda a cada elemento
print(list(map(lambda n: n ** 2, numeros)))

#filter - se queda con los que cumplen la condicion
print(list(filter(lambda n: n % 2 == 0, numeros)))

#reduce - necesita import, no es builtin
from functools import reduce
print(reduce(lambda acc, n: acc + n, numeros))