"""
En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una plataforma de bronce sobre la cual había tres agujas de diamante. 
En la primera aguja estaban apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo. A los sacerdotes se les encomendó la tarea 
de pasarlos todos desde la primera aguja a la tercera, con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse en- cima de otro más pequeño. 
Se dijo a los sacerdotes que, cuando hubieran terminado de mover los discos, llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.
"""


class Disco:
    def __init__(self, nombre):
        self.nombre = nombre
       
class Torre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.discos = []

    def agregar_disco(self, disco):
        if not self.discos or disco.nombre < self.discos[-1].nombre:
            self.discos.append(disco)
            return True
        else:
            return False
        
def mover_torres(n, torre1, torre3, torre2):
    if n == 0:
        print("No hay discos que mover.")
    elif n == 1:
        print(f"Mover disco {torre1.discos[-1].nombre} de torre {torre1.nombre} a torre {torre3.nombre}")
        torre3.agregar_disco(torre1.discos.pop())
    else:
        mover_torres(n - 1, torre1, torre2, torre3)
        print(f"Mover disco {torre1.discos[-1].nombre} de torre {torre1.nombre} a torre {torre3.nombre}")
        torre3.agregar_disco(torre1.discos.pop())
        mover_torres(n - 1, torre2, torre3, torre1)
        return True
    
if __name__ == "__main__":

    torre1 = Torre("1")
    torre2 = Torre("2")
    torre3 = Torre("3")
    n = 3

    for i in range(n, 0, -1): # sirve para agregar los discos a la torre 1 en orden de mayor a menor (de 3 a 1) 
        torre1.agregar_disco(Disco(str(i))) # str(i) es para convertir el numero a string y poder agregarlo a la torre como nombre del disco 

    mover_torres(n, torre1, torre3, torre2)