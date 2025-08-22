import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Producto:
    
    def __init__ (self):
        self.precio = 0
        self.stock = 0
        self.productos = []

    def obtener_precio(self):
        pass

    def verificar_stock(self):
        pass

class Zapato(Producto):
    def __init__ (self, marca, precio, stock):
        self.marca = marca
        self.precio = precio
        self.stock = stock
    
    def obtener_precio(self):
        return self.precio
    
    def stock_disponible(self):
        if self.stock > 0:
            print(f"Hay un stock de {self.stock} unidades")
            return True
        else:
            print(f"No hay stock de {self.marca}")
            return False


class Zapatilla(Producto):
    def __init__ (self, marca, precio, stock):
        self.marca = marca
        self.precio = precio
        self.stock = stock
    
    def obtener_precio(self):
        return self.precio
    
    def stock_disponible(self):
        if self.stock > 0:
            print("Hay stock")
            return True
        else:
            print("No hay stock")
            return False

class Metodo_pago:
    def __init__ (self, metodo, saldo):
        self.metodo = metodo
        self.saldo = saldo

    def obtener_metodo(self):
        return self.metodo
    
    def obtener_saldo(self):
        return self.saldo

def mostrar_precio(objeto):
    print(objeto.obtener_precio())

def verificar_stock(objeto):
    print(objeto.stock_disponible())

def validar_pago(pago):
    if pago.obtener_saldo() > 0:
        print("Pago aceptado")
    else:
        print("Pago rechazado")

def confirmar_venta(objeto,pago):
    if objeto.stock_disponible() and pago.obtener_saldo() >= objeto.obtener_precio():
        print("Venta confirmada")
    else:
        print("Venta rechazada")

objeto = Zapato("nike", 100, 2)
pago = Metodo_pago("UALA", 1000)

mostrar_precio(objeto)
verificar_stock(objeto)
validar_pago(pago)
confirmar_venta(objeto, pago)