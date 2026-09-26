# Tipos de variables en python

# Datos simples


cadenas: str = "Hola mundo desde python"
numero_int: int = 98
numero_float: float = 13.21
booleano: bool = True
nulo = None

print("================================")
print(f"Cadenas: {cadenas} {type(cadenas)}")
print(f"Numero entero: {numero_int} {type(numero_int)}")
print(f"Numero float: {numero_float} {type(numero_float)}")
print(f"Booleano: {booleano} {type(booleano)}")
print(f"Nulo: {nulo} {type(nulo)}")


# Datos compuestos
nombres: list[str] = ["William", "Pedro", "Alberto", "Juan"]
numeros: set[int] = {1, 3, 5, 7, 9, 11, 13}
datos_varios: tuple[str, int, float] = "William", 30, 1.80
coordenadas: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


class Persona:
    def __init__(self, nombre: str, apellido: str, dni: str) -> None:
        self.__nombre: str = nombre
        self.__apellido: str = apellido
        self.__dni: str = dni

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value:
            raise ValueError("Valor invalido")
        else:
            self.__nombre = value

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, value: str) -> None:
        if not value:
            raise ValueError("Valor invalido")
        else:
            self.__apellido = value

    @property
    def dni(self) -> str:
        return self.__dni

    @dni.setter
    def dni(self, value: str) -> None:
        if not value:
            raise ValueError("Valor invalido")
        else:
            self.__dni = value

    def __str__(self) -> str:
        return f"Persona(nombre={self.__nombre}, apellido={self.__apellido}, dni={self.__dni})"


print("==============================")
print(f"Listas: {nombres} {type(nombres)}")
print(f"Sets: {numeros} {type(numeros)}")
print(f"Tuplas: {datos_varios} {type(datos_varios)}")
print(f"Diccionarios: {coordenadas} {type(coordenadas)}")

persona = Persona("William", "Martinez", "X9323314B")
print(f"Objetos: {persona} {type(persona)}")
