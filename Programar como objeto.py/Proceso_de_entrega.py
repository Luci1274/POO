import random
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Pedido:

    def mostrar_comidas(self):
        print("Comidas disponibles:")
        comidas = ["pizza", "hamburguesa", "ensalada", "sopa", "tacos"]
        for comida in comidas:
            print(f"- {comida}")
        return comidas
    
    def realizar_pedido(self,comidas):
        print("Por favor, elige una comida de la lista anterior.")
        while True:
            comida = input("Ingresa el nombre de la comida: ")
            if comida in comidas:
                print(f"Has elegido: {comida}")
                break
            else:
                print("Comida no disponible. Por favor, elige una comida de la lista anterior.")
                for comida in comidas:
                    print(f"- {comida}")
                input("Presiona Enter para continuar...")
                continue
        stock = random.choice([0, 1, 2, 3, 4])
        while True:
            if stock == 0:
                print(f"Lo siento, {comida} no está disponible en este momento.")
                for comida in comidas:
                    print(f"- {comida}")
                input("Presiona Enter para continuar...")
                continue
            else:
                print(f"Has elegido: {comida}")
                return comida
    
    def mostrar_pedido(self, comida):
        clear()
        print(f"Tu pedido es: {comida}")
        input("Presiona Enter para continuar...")
        return comida
    

class Entrega(Pedido):
    
    def __init__(self):
        self.comidas = self.mostrar_comidas()
        self.comida = self.realizar_pedido(self.comidas)
        self.mostrar_pedido(self.comida)
        self.dirección = input("Ingresa tu dirección de entrega: ")
        self.nombre_pedido = input("Ingresa tu nombre: ")

    def preparar_comida(self):
        clear()
        print(f"Preparando {self.comida}...")
        tiempo_preparacion = random.randint(5, 25)
        print(f"Tu {self.comida} estará lista en {tiempo_preparacion} minutos.")
        input("Presiona Enter para continuar...")
    
    def entregar_pedido_repartidor(self):
        clear()
        print(f"Repartidor recogiendo {self.comida}...")
        tiempo_entrega = random.randint(10, 15)
        print(f"Tu {self.comida} llegará en {tiempo_entrega} minutos.")
        input("Presiona Enter para continuar...")

    def llevar_pedido(self):
        clear()
        print(f"Entregando {self.comida} a {self.dirección}...")
        tiempo_entrega = random.randint(10, 35)
        print(f"Tu {self.comida} llegará en {tiempo_entrega} minutos.")
        input("Presiona Enter para continuar...")
    
    def pedido_en_puerta(self):
        clear()
        print(f"Tu {self.comida} ha llegado a la puerta.")
        print(f"Muchas gracias por utilizar nuestros servicios, {self.nombre_pedido}.")
        print("Esperamos que disfrutes tu comida.")
        input("Presiona Enter para finalizar...")
    
claide = Entrega()
claide.preparar_comida()
claide.entregar_pedido_repartidor()
claide.llevar_pedido()
claide.pedido_en_puerta()
    
