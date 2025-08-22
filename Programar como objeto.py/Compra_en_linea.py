import random
import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Tienda_en_linea:
    
    def ver_productos(self):
        print("Lista de productos disponibles:")
        indice = 1
        productos = ["Laptop", "Celular", "Tablet", "Audífonos"]
        productos_disponibles = {}
        for producto in productos:
            productos_disponibles[indice] = producto
            indice += 1
        print(f"- {productos_disponibles}")
        return productos_disponibles
    
    def seleccionar_producto(self, productos_disponibles):    
        print("¿Qué producto deseas comprar? Seleccione el número del producto.")
        while True: 
            producto = input()
            producto = int(producto)  
            if not producto in productos_disponibles:
                print("Producto no disponible. Seleccione un producto de la lista.")
            else:
                print(f"Has seleccionado {productos_disponibles[producto]}.")
                return producto
    
    def seleccionar_cantidad(self, productos_disponibles, producto):
        while True:
                print("Cuantas unidades deseas comprar?")
                unidades = input()
                unidades = int(unidades)
                while unidades <= 0:
                    print("Cantidad no válida. Por favor, ingrese una cantidad positiva.")
                    unidades = input()
                    unidades = int(unidades)
                print(f"Has seleccionado {unidades} unidades de {productos_disponibles[producto]}.")
                comprado_hasta_ahora = [productos_disponibles[producto], unidades]
                return comprado_hasta_ahora
    
    def carrito_de_compras(self, comprado_hasta_ahora):
        print("Carrito de compras:")
        print(f"Producto: {comprado_hasta_ahora[0]}, Unidades: {comprado_hasta_ahora[1]}")
        return comprado_hasta_ahora
    
    def realizar_pago(self, comprado_hasta_ahora):
        print("Realizando pago...")
        print(f"Producto: {comprado_hasta_ahora[0]}, Unidades: {comprado_hasta_ahora[1]}")
        realizar_pago = input("¿Deseas realizar el pago? (si/no): ")
        if realizar_pago.lower() != "si":
            print("Pago cancelado.")
            return False
        else:
            print("Procesando pago...")
            durante_el_pago = random.choice([True, False])
            # Simulando un pago exitoso o fallido
            # En un caso real, aquí iría la lógica para procesar el pago
            # y verificar si fue exitoso o no.
            if durante_el_pago == False:
                print("Error en el pago. ¿Desea intenta nuevamente?")
                while True:
                    nuevo_pago = input("¿Deseas intentar nuevamente? (si/no): ")
                    if nuevo_pago.lower() == "si":
                        print("Reintentando pago...")
                        return True
                    elif nuevo_pago.lower() == "no":
                        print("Pago cancelado.")
                        return False
                    else:
                        print("Opción no válida. Por favor, ingrese 'si' o 'no'.")
            if durante_el_pago == True:
                print("Pago procesado con éxito.")
                print(f"Producto: {comprado_hasta_ahora[0]}, Unidades: {comprado_hasta_ahora[1]}")
                print("Gracias por su compra.")
                return True

clear()

cliente = Tienda_en_linea()
productos_disponibles = cliente.ver_productos()
producto = cliente.seleccionar_producto(productos_disponibles)
comprado_hasta_ahora = cliente.seleccionar_cantidad(productos_disponibles, producto)
carrito = cliente.carrito_de_compras(comprado_hasta_ahora)
cliente.realizar_pago(comprado_hasta_ahora)