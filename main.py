"""
Archivo principal del proyecto.
Desde aquí se ejecutan los tres módulos del repositorio colaborativo.
"""

from operaciones_matematicas import mostrar_operaciones
from cuento import imprimir_cuento
from conversor_unidades import mostrar_conversiones


def mostrar_menu():
    print("\n==============================")
    print(" Proyecto colaborativo Python")
    print("==============================")
    print("1. Operaciones matemáticas")
    print("2. Imprimir cuento")
    print("3. Conversor de temperatura")
    print("4. Ejecutar todo")
    print("5. Salir")


def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_operaciones()

        elif opcion == "2":
            imprimir_cuento()

        elif opcion == "3":
            mostrar_conversiones()

        elif opcion == "4":
            mostrar_operaciones()
            imprimir_cuento()
            mostrar_conversiones()

        elif opcion == "5":
            print("Programa finalizado. ¡Gracias por usar el proyecto!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()