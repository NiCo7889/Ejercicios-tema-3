import csv
import config
import unittest
from Ejercicios import Ejercicio1 as ej1
from Ejercicios.Ejercicio_2 import Iterativo as it
from Ejercicios.Ejercicio_2 import Recursivo as re
from Ejercicios.Ejercicio_3 import Ejercicio3 as ej3
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
        self.assertEqual(re.determinante_manera_recursiva(matriz), 0)

    def test_determinante_manera_iterativa(self):
        matriz = [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]
        ]
        self.assertEqual(it.determinante_manera_iterativa(matriz), 0)


    def setUp(self):

        # Se ejecuta antes de cada prueba
        ej3.naves.lista = [
            ej3.Nave("Halcón Milenario", 34.37, 4, 6),
            ej3.Nave("Estrella de la Muerte", 160000, 342, 843342),
            ej3.Nave("AT-AT Walker", 20.0, 5, 40),
            ej3.Nave("AT-ST Walker", 8.6, 2, 0),
            ej3.Nave("Naboo Royal Starship", 76.0, 8, 100),
            ej3.Nave("Slave I", 21.5, 1, 6),
        ]

    def test_nave_AT(self):
        lista = ej3.Nave.nave_AT()
        self.assertEqual(ej3.nave_AT(lista), True)

    def test_puede_llevar_pasajeros(self):
        lista = ej3.Nave.puede_llevar_pasajeros()
        self.assertEqual(ej3.puede_llevar_pasajeros(lista), True)
    def test_ordenar(self):
        lista = ej3.naves.ordenar()
        self.assertEqual(ej3.ordenar(lista), True)

    def test_mostar_naves(self):
        lista = ej3.naves.mostrar_naves()
        self.assertEqual(ej3.mostrar_naves(lista), True)

    def test_naves_mayor_pasajeros(self):
        lista = ej3.naves.naves_mayor_pasajeros()
        self.assertEqual(ej3.naves_mayor_pasajeros(lista), True)

    def test_nave_mayor_tripulacion(self):
        lista = ej3.naves.nave_mayor_tripulacion()
        self.assertEqual(ej3.nave_mayor_tripulacion(lista), True)

    def test_naves_AT(self):
        lista = ej3.naves.naves_AT()
        self.assertEqual(ej3.naves_AT(lista), True)

    def test_naves_mas_pasajeros(self):
        lista = ej3.naves.naves_mas_pasajeros()
        self.assertEqual(ej3.naves_mas_pasajeros(lista), True)

    def test_nave_mas_pequena(self):
        lista = ej3.naves.nave_mas_pequena()
        self.assertEqual(ej3.nave_mas_pequena(lista), True)

    def test_nave_mas_grande(self):
        lista = ej3.naves.nave_mas_grande()
        self.assertEqual(ej3.nave_mas_grande(lista), True)


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