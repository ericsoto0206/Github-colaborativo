"""
Pruebas unitarias para el módulo operaciones_matematicas.
Ejecutar con: python -m unittest tests/test_operaciones_matematicas.py
"""

import unittest
from modulos import operaciones_matematicas as om


class TestOperacionesMatematicas(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(om.sumar(2, 3), 5)
        self.assertEqual(om.sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(om.restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(om.multiplicar(4, 3), 12)

    def test_dividir(self):
        self.assertEqual(om.dividir(10, 2), 5)

    def test_dividir_entre_cero(self):
        with self.assertRaises(ValueError):
            om.dividir(10, 0)

    def test_potencia(self):
        self.assertEqual(om.potencia(2, 3), 8)

    def test_raiz_cuadrada(self):
        self.assertEqual(om.raiz_cuadrada(9), 3)

    def test_raiz_cuadrada_negativo(self):
        with self.assertRaises(ValueError):
            om.raiz_cuadrada(-4)

    def test_factorial(self):
        self.assertEqual(om.factorial(5), 120)
        self.assertEqual(om.factorial(0), 1)

    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            om.factorial(-3)

    def test_promedio(self):
        self.assertEqual(om.promedio([2, 4, 6]), 4)

    def test_promedio_lista_vacia(self):
        with self.assertRaises(ValueError):
            om.promedio([])


if __name__ == "__main__":
    unittest.main()
