


class Cliente:
    def __init__(self,nombre: str, apellido: str) -> None:
        self.__nombre: str = nombre
        self.__apellido: str = apellido

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    def __str__(self) -> str:
        return f"Cliente(nombre={self.__nombre}, apellido={self.__apellido})"