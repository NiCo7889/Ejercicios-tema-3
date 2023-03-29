import unittest
# import csv
# import config
from Ejercicios import Ejercicio1 as ej1
from Ejercicios import Ejercicio2 as ej2
# from Ejercicios.Ejercicio3 import Ejercicio3 as ej3
from Ejercicios import Ejercicio4 as ej4

class TestEjercicios(unittest.TestCase):

    def test_agregar_disco(self):
        torre1 = ej1.Torre("1")
        self.assertEqual(torre1.agregar_disco(ej1.Disco(str(3))), True)

    def test_mover_torres(self): # Test hecho para 3 discos
        torre1 = ej1.Torre("1")
        torre2 = ej1.Torre("2")
        torre3 = ej1.Torre("3")
        n = 3

        for i in range(n, 0, -1):
            torre1.agregar_disco(ej1.Disco(str(i)))

        self.assertEqual(ej1.mover_torres(n, torre1, torre3, torre2), True)

    def test_determinante_manera_recursiva(self):
        matriz = [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]
        ]
        self.assertEqual(ej2.determinante_manera_recursiva(matriz), 0)

    def test_determinante_manera_iterativa(self):
        matriz = [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]
        ]
        self.assertEqual(ej2.determinante_manera_iterativa(matriz), 0)





#     def setUp(self):
#         self.naves = [
#             ej3.Nave("Halcón Milenario", 34.37, 4, 6),
#             ej3.Nave("Estrella de la Muerte", 160000, 342, 843342),
#             ej3.Nave("AT-AT Walker", 20.0, 5, 40),
#             ej3.Nave("AT-ST Walker", 8.6, 2, 0),
#             ej3.Nave("Naboo Royal Starship", 76.0, 8, 100),
#             ej3.Nave("Slave I", 21.5, 1, 6),
#             ej3.Nave("TIE Fighter", 6.4, 1, 0),
#             ej3.Nave("X-wing", 12.5, 1, 0),
#             ej3.Nave("Imperial Star Destroyer", 1600.0, 47060, 0),
#             ej3.Nave("Millennium Falcon", 34.37, 4, 6)
#         ]

#         self.naves_AT = [nave for nave in self.naves if nave.nave_AT()]

# # naves_AT = [nave for nave in naves if nave.nave_AT()]
#     # print("\n Naves que comienzan con AT: \n")
#     # print(naves_AT)

#     def test_nave_AT(self):
#         self.assertEqual(self.naves_AT, "[Nombre: AT-AT Walker, Longutud: 20.0 m, Tripulación: 5, Pasajeros: 40, Nombre: AT-ST Walker, Longutud: 8.6 m, Tripulación: 2, Pasajeros: 0]")

#     # def test_nave_AT(self):
#     #     self.assertEqual(ej3.Nave.nave_AT(), "[Nombre: AT-AT Walker, Longutud: 20.0 m, Tripulación: 5, Pasajeros: 40, Nombre: AT-ST Walker, Longutud: 8.6 m, Tripulación: 2, Pasajeros: 0]")

#     # def test_puede_llevar_pasajeros(self):
#     #     self.assertEqual(ej3.Nave.puede_llevar_pasajeros(6), "[Nombre: Halcón Milenario, Longutud: 34.37 m, Tripulación: 4, Pasajeros: 6, Nombre: Estrella de la Muerte, Longutud: 160000 m, Tripulación: 342, Pasajeros: 843342, Nombre: AT-AT Walker, Longutud: 20.0 m, Tripulación: 5, Pasajeros: 40, Nombre: Naboo Royal Starship, Longutud: 76.0 m, Tripulación: 8, Pasajeros: 100, Nombre: Slave I, Longutud: 21.5 m, Tripulación: 1, Pasajeros: 6, Nombre: Millennium Falcon, Longutud: 34.37 m, Tripulación: 4, Pasajeros: 6]")





    def setUp(self):
        self.p1 = ej4.Polinomio()
        ej4.Polinomio.agregar_termino(self.p1, 1, 5)
        ej4.Polinomio.agregar_termino(self.p1, 2, 2)
        self.p2 = ej4.Polinomio()
        ej4.Polinomio.agregar_termino(self.p2, 1, 4)
        ej4.Polinomio.agregar_termino(self.p2, 3, 6)
        self.p3 = ej4.Polinomio()
   
    def test_agregar_termino(self):
        ej4.Polinomio.agregar_termino(self.p3, 3, -1)
        ej4.Polinomio.agregar_termino(self.p3, 2, 2)
        ej4.Polinomio.agregar_termino(self.p3, 1, 4)
        self.assertEqual(ej4.Polinomio.mostrar(self.p3), "-1x^3+2x^2+4x^1")

    def test_modificar_termino(self):
        ej4.Polinomio.modificar_termino(self.p1, 1, 7)
        self.assertEqual(ej4.Polinomio.mostrar(self.p1), "+2x^2+7x^1")

    def test_obtener_valor(self):
        self.assertEqual(ej4.Polinomio.obtener_valor(self.p2, 1), 4)
        self.assertEqual(ej4.Polinomio.obtener_valor(self.p2, 3), 6)

    def test_eliminar_termino(self):
        ej4.Polinomio.eliminar_termino(self.p1, 1)
        self.assertEqual(ej4.Polinomio.mostrar(self.p1), "+2x^2")

    def test_existe_termino(self):
        self.assertTrue(ej4.Polinomio.existe_termino(self.p1, 1))
        self.assertFalse(ej4.Polinomio.existe_termino(self.p2, 2))

    def test_restar(self):
        p5 = ej4.Polinomio.restar(self.p1, self.p2)
        self.assertEqual(ej4.Polinomio.mostrar(p5), "-6x^3+2x^2+1x^1")

if __name__ == '__main__':
    unittest.main()