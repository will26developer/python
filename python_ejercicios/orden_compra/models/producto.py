from select import select


class Producto:
    def __init__(self, nombre: str, fabricante: str, precio: float) -> None:
        self.__nombre: str = nombre
        self.__fabricante: str = fabricante
        self.__precio: float = precio

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def fabricante(self) -> str:
        return self.__fabricante

    @property
    def precio(self) -> float:
        return self.__precio

    def __str__(self) -> str:
        return f"Producto(nombre={self.__nombre}, fabricante={self.__fabricante}, precio={self.precio})"