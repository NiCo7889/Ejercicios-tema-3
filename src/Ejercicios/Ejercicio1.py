"""
En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una plataforma de bronce sobre la cual había tres agujas de diamante. 
En la primera aguja estaban apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo. A los sacerdotes se les encomendó la tarea 
de pasarlos todos desde la primera aguja a la tercera, con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse en- cima de otro más pequeño. 
Se dijo a los sacerdotes que, cuando hubieran terminado de mover los discos, llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.
"""
# hay que hacer uso de las colas para resolverlo


class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()


def torre_hanoi_pila(n):
    A = Pila()
    B = Pila()
    C = Pila()

    # Llenar pila A con los n discos
    for i in range(n, 0, -1):
        A.apilar(i)

    if n % 2 == 0:
        while not C.esta_vacia() or not B.esta_vacia():
            if not C.esta_vacia() and (B.esta_vacia() or C.items[-1] < B.items[-1]):
                mover_disco(C, B)
            else:
                mover_disco(B, C)
    else:
        while not C.esta_vacia() or not A.esta_vacia():
            if not C.esta_vacia() and (A.esta_vacia() or C.items[-1] < A.items[-1]):
                mover_disco(C, A)
            else:
                mover_disco(A, C)


def mover_disco(desde, hacia):
    disco = desde.desapilar()
    hacia.apilar(disco)
    print(f"Mover disco de {desde} a {hacia}")

print(torre_hanoi_pila(4))


# class Pila:
#     def __init__(self):
#         self.items = []

#     def esta_vacia(self):
#         return self.items == []

#     def agregar(self, item):
#         self.items.append(item)

#     def quitar(self):
#         return self.items.pop()

# def torre_hanoi_pila(n):
#     pila_origen = Pila()
#     pila_auxiliar = Pila()
#     pila_destino = Pila()

#     # Llenar la pila de origen con los discos
#     for i in range(n, 0, -1):
#         pila_origen.agregar(i)

#     # Definir la dirección de los movimientos
#     if n % 2 == 0:
#         direccion = ["A", "C", "B"]
#     else:
#         direccion = ["A", "B", "C"]

#     # Realizar los movimientos
#     movimiento = 0
#     while len(pila_destino.items) != n:
#         movimiento += 1
#         if movimiento % 3 == 1:
#             mover_disco(pila_origen, pila_destino, direccion[0], direccion[1])
#         elif movimiento % 3 == 2:
#             mover_disco(pila_origen, pila_auxiliar, direccion[0], direccion[2])
#         else:
#             mover_disco(pila_auxiliar, pila_destino, direccion[2], direccion[1])

# def mover_disco(pila_origen, pila_destino, origen, destino):
#     if not pila_origen.esta_vacia() and (pila_destino.esta_vacia() or pila_origen.items[-1] < pila_destino.items[-1]):
#         disco = pila_origen.quitar()
#         pila_destino.agregar(disco)
#         print(f"Mover disco de {origen} a {destino}")

# # Ejemplo de uso para el problema planteado en el ejercicio:
# print(torre_hanoi_pila(2))
