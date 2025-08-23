import os
def clear():
    try:
        clear = os.system("cls")
        clear_linux = os.system("clear")
        print("-" * 50)
    except:
        print("No se a podido limpiar la pantalla")
        pass