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


# Crear la lista de naves
naves = [
    Nave("Halcón Milenario", 34.37, 4, 6),
    Nave("Estrella de la Muerte", 160000, 342, 843342),
    Nave("AT-AT Walker", 20.0, 5, 40),
    Nave("AT-ST Walker", 8.6, 2, 0),
    Nave("Naboo Royal Starship", 76.0, 8, 100),
    Nave("Slave I", 21.5, 1, 6),
    Nave("TIE Fighter", 6.4, 1, 0),
    Nave("X-wing", 12.5, 1, 0),
    Nave("Imperial Star Destroyer", 1600.0, 47060, 0),
    Nave("Millennium Falcon", 34.37, 4, 6)
]

# Cuestiones
if __name__ == "__main__":
    # Ordenar las naves por nombre de manera ascendente y por largo de manera descendente
    naves_ordenadas = sorted(naves) # sorted() devuelve una lista ordenada sin modificar la lista original
    print("\n Naves ordenadas por nombre de manera ascendente y por largo de manera descendente: \n")
    print(naves_ordenadas)

    # Mostrar la información del Halcón Milenario y la Estrella de la Muerte
    halcon_milenario = next(nave for nave in naves if nave == Nave("Halcón Milenario", 0, 0, 0)) # next() devuelve el primer elemento de la lista que cumpla con la condición
    estrella_muerte = next(nave for nave in naves if nave == Nave("Estrella de la Muerte", 0, 0, 0)) # next() devuelve el primer elemento de la lista que cumpla con la condición
    print("\n Información del Halcón Milenario y la Estrella de la Muerte: \n")
    print(halcon_milenario)
    print(estrella_muerte)

    # # Determinar las cinco naves con mayor cantidad de pasajeros
    naves_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
    print("\n Naves con mayor cantidad de pasajeros: \n")
    print(naves_pasajeros)

    # Indicar cuál es la nave que requiere mayor cantidad de tripulación
    nave_tripulacion_maxima = max(naves, key=lambda x: x.tripulacion)
    print("\n Nave que requiere mayor cantidad de tripulación: \n")
    print(nave_tripulacion_maxima)

    # Mostrar todas las naves que comienzan con AT
    naves_AT = [nave for nave in naves if nave.nave_AT()]
    print("\n Naves que comienzan con AT: \n")
    print(naves_AT)

    # Listar todas las naves que pueden llevar seis o más pasajeros
    naves_pueden_llevar_pasajeros = [nave for nave in naves if nave.puede_llevar_pasajeros(6)]
    print("\n Naves que pueden llevar seis o más pasajeros: \n")
    print(naves_pueden_llevar_pasajeros)

    # Mostrar toda la información de la nave más pequeña y la más grande
    nave_mas_pequena = min(naves, key=lambda x: x.largo)
    nave_mas_grande = max(naves, key=lambda x: x.largo)
    print("\n Nave más pequeña y la más grande: \n")
    print("La nave más pequeña: ", nave_mas_pequena)
    print(" La nave más grande: ", nave_mas_grande)