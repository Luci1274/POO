import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Inventario:

    def ver_inventario(self):
        # Este método debería mostrar el inventario actual
        # El cual deberia de estar en una base de datos o en un archivo
        # Por simplicidad, aquí se muestra un inventario ficticio
        # El cual sera solo un mensaje
        print("Inventario actual:")
        productos = {"helado": 10, "gaseosa": 20, "agua": 30, "cerveza": 0, "vino": 5, "whisky": 0}
        return productos
    
    def filtrar_productos(self, productos):
        # Este método debería filtrar los productos según su cantidad
        # Por simplicidad, aquí se muestra un inventario ficticio
        print("Filtrando productos:")
        productos_sin_stock = []
        for producto, cantidad in productos.items():
            if cantidad == 0:
                print(f"{producto}: sin stock")
                productos_sin_stock.append(producto)
        return productos_sin_stock
    
    def agregar_producto(self, productos_sin_stock, cantidad):
        # Este método debería agregar un producto al inventario
        # Por simplicidad, aquí se muestra un inventario ficticio
        print(f"Agregando {cantidad} unidades de {productos_sin_stock} al inventario")
        return True

class Repositor(Inventario):
    
    def realizar_pedido_repocision(self):
        productos = self.ver_inventario()
        productos_sin_stock = self.filtrar_productos(productos)
        if len(productos_sin_stock) == 0:
            print("No hay productos sin stock")
            exit()
        else:
            print(f"El producto: {productos_sin_stock} está sin stock")
            while True:
                print("Desea realizar un pedido de reposición? si/no")
                respuesta = input().lower()
                if respuesta == "si" or respuesta == "sí" or respuesta == "s":
                    print("Realizando pedido de reposición")
                    cantidad = int(input("Ingrese la cantidad a reponer: "))
                    self.agregar_producto(productos_sin_stock, cantidad)
                    break
                elif respuesta == "no" or respuesta == "n":
                    print("No se realizará el pedido de reposición")
                    break
                else:
                    print("Respuesta no válida, por favor ingrese 'si' o 'no'")

repositor = Repositor()
repositor.realizar_pedido_repocision()