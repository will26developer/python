import datetime
from readline import get_completer

from models.producto import Producto
from models.orden_compra import OrdenCompra
from models.cliente import Cliente

cliente = Cliente("William","Martinez")
fecha = datetime.datetime.now()
orden_compra = OrdenCompra("Ticket de compra")

orden_compra.fecha = fecha
orden_compra.cliente = cliente

producto1 = Producto("Laptop", "Dell", 850.99)
producto2 = Producto("Mouse", "Logitech", 25.50)
producto3 = Producto("Teclado", "Razer", 120.00)
producto4 = Producto("Monitor", "Samsung", 310.75)

orden_compra.add_producto(producto1)
orden_compra.add_producto(producto2)
orden_compra.add_producto(producto3)
orden_compra.add_producto(producto4)

print(orden_compra)
print(orden_compra.total())
