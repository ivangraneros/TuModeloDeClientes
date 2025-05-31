    #metodo para agregar producto al carrito
def agregar_producto(self, producto):
    self.carrito.append(producto)
    print(f"Producto '{producto}' agregado al carrito de {self.nombre}.")
    
    
    #metodo para mostrar carrito    
def mostrar_carrito(self):
    if not self.carrito:
        print(f"El carrito de {self.nombre} está vacío.")
    else:
        print(f"Carrito de {self.nombre}:")
        for producto in self.carrito:
            print(f"- {producto}")