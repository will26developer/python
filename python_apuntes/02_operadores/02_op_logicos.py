# Operadores logicos y de pertenencia

booleano_verdadero: bool = True
booleano_falso: bool = False

print(
    f"{booleano_verdadero} and {booleano_falso} = {booleano_verdadero and booleano_falso}"
)
print(
    f"{booleano_verdadero} or {booleano_falso} = {booleano_verdadero or booleano_falso}"
)
print(f"not {booleano_verdadero} = {not booleano_verdadero}")

# Operador de pertenencia
num1: int = 23

numeros: list[int] = [21, 23, 25, 27]
print(f"{num1} esta en {numeros} = {num1 in numeros}")

# Operador ternario
respuesta: str = (
    f"{num1} esta en el conjunto"
    if num1 in numeros
    else f"{num1} no esta en el conjunto"
)
print(respuesta)
