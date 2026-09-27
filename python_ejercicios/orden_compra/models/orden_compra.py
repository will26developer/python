from datetime import datetime

from models.cliente import Cliente
from models.producto import Producto


class OrdenCompra:
    def __init__(self, descripcion: str) -> None:
        self.__descripcion: str = descripcion
        self.__fecha: datetime | None = None
        self.__cliente: Cliente | None = None
        self.__productos: list[Producto] = []

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @property
    def fecha(self) -> datetime | None:
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha: datetime | None) -> None:
        if not fecha:
            raise ValueError("Fecha incorrecto")
        else:
            self.__fecha = fecha

    @property
    def cliente(self) -> Cliente | None:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente | None) -> None:
        if not cliente:
            raise ValueError("Cliente incorrecto")
        else:
            self.__cliente = cliente

    @property
    def productos(self) -> list[Producto]:
        return self.__productos

    def add_producto(self, producto: Producto) -> None:
        if isinstance(producto,Producto) and (len(self.__productos) < 4):
            self.__productos.append(producto)
        else:
            print("Carrito de la compra lleno")
            print(len(self.__productos))

    def total(self) -> float:
        return sum(producto.precio for producto in self.__productos)

    def __str__(self) -> str:
        return f"OrdenCompra(descripcion={self.__descripcion}, fecha={self.__fecha}, cliente={self.__cliente}, productos={self.__productos})"