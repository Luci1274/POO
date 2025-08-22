#Clases
# Inventario
#Pseudocodigo
#   Agregar productos al inventario
#   Buscar producto
#   Calcular el total del precio en el inventario
#   Mostrar todos los productos

import os

def clear():
    """Esta funcion limpia la pantalla y imprime una linea de guiones"""
    try:
        os.system("clear"), os.system("cls")
        print("-" * 75)
    except:
        pass

class Inventario:
    """La clase recibe hasta un maximo de 10 productos con su stock y precio unitario, la añade a las listas y diccionario, 
    además la clase permite buscar un podructo y mostrar su informacion junto a mostrar el inventario completo y el valor de este"""
    
    def __init__ (self):
        self.datos_productos = {}
        self.productos = []
        self.stock = []
        self.precio_unitario = []

    def agregar_producto(self, producto, cantidad, precio):
        if not producto in self.productos:
            self.datos_productos[producto] = [cantidad, precio]
            self.productos.append(producto)
            self.stock.append(cantidad)
            self.precio_unitario.append(precio)
            self.calcular_valor_inventario(cantidad, precio)
        else:
            print("Producto ya ingresado")

    def mostrar_inventario(self):
        print(f"Los productos en el inventario son:")
        for producto, (cantidad, precio) in self.datos_productos.items():
            print(f"Producto: {producto}, Cantidad: {cantidad}, Precio unitario: {precio}")
    
    def calcular_valor_inventario(self, cantidad, precio):
        self.valor_inventario =+ cantidad * precio
        

    def buscar_producto(self, producto):
        if producto in self.datos_productos:
            cantidad, precio = self.datos_productos[producto]
            print(f"Producto: {producto}\nCantidad: {cantidad}\nPrecio unitario: {precio}")
        else:
            print("El producto no está en el inventario")

            
def elegir(inventario):
    """"La funcion permite elegir una opcion del menu, y llama a las funciones correspondientes"""
    while True:
        clear()
        print("Ingrese el numero de la opcion a elegir\n 1: Ingresar producto\n 2 Buscar producto\n 3: Calcular valor total del inventario\n 4: Mostrar inventario\n 5: Salir\n")
        elegir = input("")
        if elegir == "1":
            ingresar_producto(inventario)
            continue
                
        elif elegir == "2":
            for producto in inventario.productos:
                print(producto)
            buscar_producto(inventario)
            continue
                
        elif elegir == "3":
            try:
                print(f"El valor total del inventario es: {inventario.valor_inventario}")
                input("Ingrese enter para continuar")
                continue
            except:
                print("Añada un producto antes de continuar")
                input("Ingrese enter para continuar")
                
        elif elegir == "4":
            inventario.mostrar_inventario()
            input("Ingrese enter para continuar")
            continue
        
        elif elegir == "5":
            exit()
        else:
            print("Error pro favor elija la opcion correcta")
            continue

def ingresar_producto(inventario):
    """"La funcion permite ingresar productos al inventario, con un maximo de 10 productos"""
    for i in range(11):
        producto = input("Ingrese el nombre del producto: ").lower().strip()
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad a añadir a stock: "))
                precio  = float(input("Ingrese el precio unitario del producto: "))
                if cantidad >= 0 and precio >= 0:
                    inventario.agregar_producto(producto, cantidad, precio)
                    i += 1
                    break
                            
                else:
                    print("La el valor del stock o del precio unitario debe ser mayor o igual a 0")
                    continue
            except:
                print("Debe de ingresar valores numericos")
                continue
        print("Desea continuar? S/N")
        continuar = input("").lower().strip()
        if continuar != "s":
            return
        else:
            pass
    return
          
def buscar_producto(inventario):
    """La funcion busca un producto en el inventario y muestra su informacion"""
    producto = input("Ingrese el producto a buscar:")
    if producto in inventario.productos:
        inventario.buscar_producto(producto)
        input("Precione enter para continuar")
    else:
        print("El producto no está en el sistema. por favor agreguelo")
        return
    
inventario = Inventario()
elegir(inventario)
clear()
