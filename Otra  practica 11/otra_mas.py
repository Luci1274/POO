import os

def clear():
    try:
        os.system("cls")
        os.system("clear")
        print("-" * 75)
    except:
        pass

class Sistema:
    
    def __init__(self, item, cantidad):
        self.productos = {}
        self.item = item
        self.cantidad = cantidad
    
    def agregar_nuevo_producto(self, producto, item, cantidad):
        if not producto in self.productos and not item in self.item:
            self.productos[item] = [producto, cantidad]
        else:
            print(f"El producto: {producto} ya está registrado o el item ya está en uso {item}")
    
    def verificar_stok(self):
        for item, producto, cantidad in self.productos.items():
            print(f"{item}: {producto, cantidad}")
    
    def sumar_stock(self, item, sumar):
        if item in self.productos:
            self.productos[item[1]] =+ sumar
    
    def restar_stock(self, item, restar):
        if item in self.productos:
            self.productos[item[1]] =- restar
    
clear()