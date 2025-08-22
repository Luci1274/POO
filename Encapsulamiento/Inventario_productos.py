class Productos:
    
    def nombrar_producto(self):
        self.__nombre = input("Ingrese el nombre del producto: ") 
        
    def modificar_nombre(self):
        while True:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            if self.__nombre != nuevo_nombre:
                self.__nombre = nuevo_nombre
                print(f"Nombre modificado a: {self.__nombre}")
                break
                
            else:
                print("El nombre ingresado es el mismo que el actual. Intente nuevamente.")
                continue
    
    def ingresar_precio(self):
        while True:
            self.__precio = float(input("Ingrese el precio del producto: "))
            if self.__precio > 0:
                print(f"Precio ingresado: {self.__precio}")
                break
            else:
                print("El precio debe ser mayor a 0. Intente nuevamente.")
                continue
    
    def ingresar_stock(self):
        while True:
            self.__stock = int(input("Ingrese el stock del producto: "))
            if self.__stock >= 0:
                print(f"Stock ingresado: {self.__stock}")
                break
            else:
                print("El stock no puede ser negativo. Intente nuevamente.")
                continue

    def retirar_stock(self):
        while True:
            retirar = int(input("Ingrese la cantidad de productos a retirar: "))
            if self.__stock > 0 and retirar > 0:
                self.__stock -= retirar
                print(f"Stock retirado: {retirar}, stock restante {self.__stock}")
                break
            else:
                print("La cantidad a retirar debe ser mayor a 0. Intente nuevamente.")
                continue
    
    def agregar_stock(self):
        while True:
            agregar = int(input("Ingrese la cantidad de productos a agregar: "))
            if agregar > 0:
                self.__stock += agregar
                print(f"Stock agregado: {agregar}, stock restante {self.__stock}")
                break
            else:
                print("La cantidad a agregar debe ser mayor a 0. Intente nuevamente.")
                continue
    
    def agregar_informacion(self):
        self.nombrar_producto()
        self.ingresar_precio()
        self.ingresar_stock()

    def mostrar_informacion(self):
        print(f"Nombre del producto: {self.__nombre}")
        print(f"Precio del producto: {self.__precio}")
        print(f"Stock del producto: {self.__stock}")

producto = Productos()

print("Informacion basica del producto")
producto.agregar_informacion()
producto.mostrar_informacion()
input("Presione Enter para continuar...")
print(f"{50 * "-"} \n modificar informacion del producto \n ")
producto.modificar_nombre()
producto.retirar_stock()
producto.mostrar_informacion()
input("Presione Enter para continuar...")
print(f"{50 * "-"} \n agregar stock del producto \n ")
producto.agregar_stock()
producto.mostrar_informacion()