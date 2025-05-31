# ejemplo_uso.py
from cliente_compras import Cliente
from cliente_compras.utils import *


# Crear un cliente
cliente1 = Cliente("Ivan Graneros", "ivan@gmail.com", "123456789", "Calle Falsa 123")

# Agregar productos
cliente1.agregar_producto("Teclado")
cliente1.agregar_producto("Mouse")

# Mostrar carrito
cliente1.mostrar_carrito()

# Imprimir el cliente
print(cliente1)

