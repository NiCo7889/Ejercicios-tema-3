"""
Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, tripulación y cantidad de pasajeros, 
desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:
- realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
- mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
- determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
- indicar cuál es la nave que requiere mayor cantidad de tripulación;
- mostrar todas las naves que comienzan con AT;
- listar todas las naves que pueden llevar seis o más pasajeros;
- mostrar toda la información de la nave más pequeña y la más grande.
"""


import csv
import config


class Nave:

    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
    
    def __str__(self):
        return "Nombre: {}, Longutud: {} m, Tripulación: {}, Pasajeros: {}".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)
        
    def __repr__(self): # Para mostrar la información de la nave en la lista de naves
        return str(self)
    
    def __eq__(self, other): # Para comparar dos naves por nombre y largo 
        return self.nombre == other.nombre
    
    def __lt__(self, other): # Para ordenar las naves por nombre y largo de manera ascendente y descendente respectivamente 
        if self.nombre == other.nombre:
            return self.largo > other.largo
        return self.nombre < other.nombre
    
    def nave_AT(self): # Para determinar si la nave comienza con AT 
        return self.nombre.startswith("AT")
    
    def puede_llevar_pasajeros(self, num_pasajeros): # Para determinar si la nave puede llevar una cantidad de pasajeros 
        return self.pasajeros >= num_pasajeros


class naves:

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for nombre, largo, tripulacion, pasajeros in reader:
            nave = Nave(nombre, largo, tripulacion, pasajeros)
            lista.append(nave)

    @staticmethod
    def ordenar():
        return sorted(naves.lista)
    
    @staticmethod
    def mostrar_naves(nombre1, nombre2):
        for nave in naves.lista:
            if nave.nombre == nombre1 or nave.nombre == nombre2:
                return nave
            
    @staticmethod
    def naves_mayor_pasajeros():
        return sorted(naves.lista, key=lambda nave: nave.pasajeros, reverse=True)[:5]
    
    @staticmethod
    def nave_mayor_tripulacion():
        return max(naves.lista, key=lambda nave: nave.tripulacion)
    
    @staticmethod
    def naves_AT():
        return list(filter(lambda nave: nave.nave_AT(), naves.lista))
    
    # @staticmethod
    # def naves_mas_pasajeros():
    #     naves_pueden_llevar_pasajeros = [nave for nave in naves.lista if Nave.puede_llevar_pasajeros(6)]
    #     return naves_pueden_llevar_pasajeros    

    @staticmethod
    def nave_mas_pequena():
        return min(naves.lista, key=lambda nave: nave.largo)
    
    @staticmethod
    def nave_mas_grande():
        return max(naves.lista, key=lambda nave: nave.largo)
    


if __name__ == "__main__":

#     # Ordenar las naves por nombre de manera ascendente y por largo de manera descendente
    print("\n Naves ordenadas por nombre de manera ascendente y por largo de manera descendente: \n")
    print(naves.ordenar())

#     # Mostrar la información del Halcón Milenario y la Estrella de la Muerte
    print("\n Información del Halcón Milenario y la Estrella de la Muerte: \n")
    print(naves.mostrar_naves("Halcón Milenario", "Estrella de la Muerte"))

#     # # Determinar las cinco naves con mayor cantidad de pasajeros
    print("\n Naves con mayor cantidad de pasajeros: \n")
    print(naves.naves_mayor_pasajeros())

#     # Indicar cuál es la nave que requiere mayor cantidad de tripulación
    print("\n Nave que requiere mayor cantidad de tripulación: \n")
    print(naves.nave_mayor_tripulacion())

#     # Mostrar todas las naves que comienzan con AT
    print("\n Naves que comienzan con AT: \n")
    print(naves.naves_AT())

# #     # Listar todas las naves que pueden llevar seis o más pasajeros
#     print("\n Naves que pueden llevar seis o más pasajeros: \n")
#     print(naves.naves_mas_pasajeros(6))

#     # Mostrar toda la información de la nave más pequeña y la más grande
    print("\n Información de la nave más pequeña y la más grande: \n")
    print("Nave más pequeña: ", naves.nave_mas_pequena())
    print("Nave más grande: ", naves.nave_mas_grande())

















# # Cuestiones
# if __name__ == "__main__":
    
#     # Ordenar las naves por nombre de manera ascendente y por largo de manera descendente
#     naves_ordenadas = sorted(naves) # sorted() devuelve una lista ordenada sin modificar la lista original
#     print("\n Naves ordenadas por nombre de manera ascendente y por largo de manera descendente: \n")
#     print(naves_ordenadas)

#     # Mostrar la información del Halcón Milenario y la Estrella de la Muerte
#     halcon_milenario = next(nave for nave in naves if nave == Nave("Halcón Milenario", 0, 0, 0)) # next() devuelve el primer elemento de la lista que cumpla con la condición
#     estrella_muerte = next(nave for nave in naves if nave == Nave("Estrella de la Muerte", 0, 0, 0)) # next() devuelve el primer elemento de la lista que cumpla con la condición
#     print("\n Información del Halcón Milenario y la Estrella de la Muerte: \n")
#     print(halcon_milenario)
#     print(estrella_muerte)

#     # # Determinar las cinco naves con mayor cantidad de pasajeros
#     naves_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
#     print("\n Naves con mayor cantidad de pasajeros: \n")
#     print(naves_pasajeros)

#     # Indicar cuál es la nave que requiere mayor cantidad de tripulación
#     nave_tripulacion_maxima = max(naves, key=lambda x: x.tripulacion)
#     print("\n Nave que requiere mayor cantidad de tripulación: \n")
#     print(nave_tripulacion_maxima)

#     # Mostrar todas las naves que comienzan con AT
#     naves_AT = [nave for nave in naves if nave.nave_AT()]
#     print("\n Naves que comienzan con AT: \n")
#     print(naves_AT)

#     # Listar todas las naves que pueden llevar seis o más pasajeros
#     naves_pueden_llevar_pasajeros = [nave for nave in naves if nave.puede_llevar_pasajeros(6)]
#     print("\n Naves que pueden llevar seis o más pasajeros: \n")
#     print(naves_pueden_llevar_pasajeros)

#     # Mostrar toda la información de la nave más pequeña y la más grande
#     nave_mas_pequena = min(naves, key=lambda x: x.largo)
#     nave_mas_grande = max(naves, key=lambda x: x.largo)
#     print("\n Nave más pequeña y la más grande: \n")
#     print("La nave más pequeña: ", nave_mas_pequena)
#     print(" La nave más grande: ", nave_mas_grande)