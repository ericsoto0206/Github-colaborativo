"""
Pruebas unitarias para el módulo cuento.
Ejecutar con: python -m unittest tests/test_cuento.py
"""

import unittest
from modulos import cuento


class TestCuento(unittest.TestCase):

    def test_titulo_no_vacio(self):
        self.assertTrue(len(cuento.TITULO) > 0)

    def test_cuento_tiene_parrafos(self):
        self.assertGreater(len(cuento.CUENTO), 0)

    def test_contar_palabras(self):
        total = cuento.contar_palabras()
        self.assertIsInstance(total, int)
        self.assertGreater(total, 0)


if __name__ == "__main__":
    unittest.main()
