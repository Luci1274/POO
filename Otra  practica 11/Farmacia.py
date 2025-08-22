class Usuario:
    pass
    def recibir_datos (self):
        while True:
            try:
                DNI = input("ingrese el DNI del cliente: ")
                if len(DNI) == 8 and DNI.isdigit():
                    return DNI
            except:
                print("el DNI no es correcto")
    
    def registrar(self):
        nombre = input("ingrese el nombre del cliente: ")
        apellido = input("ingrese el apellido del cliente: ")
        telefono = input("ingrese el telefono del cliente: ")
        direccion = input("ingrese la direccion del cliente: ")
        correo = input("ingrese el correo del cliente: ")
        return nombre, apellido, telefono, direccion, correo
    
class recibo(Usuario):
    pass
    def validar (self, DNI):
        base_dni = open("Practicas de POO/Otra  practica 11/dni.csv", "r")
        base_dni = base_dni.read().splitlines()
        if DNI in base_dni:
            print("el DNI se encuentra en la base de datos")
            return True
        else:
            guardar_dni = open("Practicas de POO/Otra  practica 11/dni.csv", "a")
            guardar_dni.write(DNI + "\n")
            print("el DNI no se encuentra en la base de datos")
            return False
    
    def imprimir_receta(self):
        print("recibo")
        print("nombre: .....")
        print("apellido: ......")
        print("telefono: ...........")
        print("direccion: ..........")
        print("correo: ............")
        print("medicamento.......")

operario = Usuario()
sistema = recibo()
if sistema.validar(operario.recibir_datos()) == True:
    sistema.imprimir_receta()
else:
    operario.registrar()
    sistema.imprimir_receta()
