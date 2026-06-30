"""
Pruebas unitarias para el módulo conversor_unidades.
Ejecutar con: python -m unittest tests/test_conversor_unidades.py
"""

import unittest
from modulos import conversor_unidades as cu


class TestConversorUnidades(unittest.TestCase):

    def test_metros_a_pies(self):
        self.assertAlmostEqual(cu.metros_a_pies(1), 3.28084, places=4)

    def test_pies_a_metros(self):
        self.assertAlmostEqual(cu.pies_a_metros(3.28084), 1, places=4)

    def test_km_a_millas(self):
        self.assertAlmostEqual(cu.km_a_millas(1), 0.621371, places=4)

    def test_kg_a_libras(self):
        self.assertAlmostEqual(cu.kg_a_libras(1), 2.20462, places=4)

    def test_celsius_a_fahrenheit(self):
        self.assertEqual(cu.celsius_a_fahrenheit(0), 32)
        self.assertEqual(cu.celsius_a_fahrenheit(100), 212)

    def test_fahrenheit_a_celsius(self):
        self.assertEqual(cu.fahrenheit_a_celsius(32), 0)

    def test_celsius_a_kelvin(self):
        self.assertEqual(cu.celsius_a_kelvin(0), 273.15)

    def test_celsius_a_kelvin_invalido(self):
        with self.assertRaises(ValueError):
            cu.celsius_a_kelvin(-300)


if __name__ == "__main__":
    unittest.main()
