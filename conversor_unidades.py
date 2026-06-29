"""
Módulo: conversor_temperatura.py
Descripción: Convierte temperaturas entre Celsius y Fahrenheit.
"""


def mostrar_conversiones():
    temperatura_celsius = 25
    temperatura_fahrenheit = 77

    fahrenheit = (temperatura_celsius * 9 / 5) + 32
    celsius = (temperatura_fahrenheit - 32) * 5 / 9

    print("\n--- Conversor de Temperatura ---")
    print("25 grados Celsius equivalen a", fahrenheit, "grados Fahrenheit")
    print("77 grados Fahrenheit equivalen a", celsius, "grados Celsius")