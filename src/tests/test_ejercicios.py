import unittest
# from Ejercicios import Ejercicio1 as ej1
# from Ejercicios import Ejercicio2 as ej2
# from Ejercicios import Ejercicio3 as ej3
from Ejercicios import Ejercicio4 as ej4

class TestEjercicios(unittest.TestCase):

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