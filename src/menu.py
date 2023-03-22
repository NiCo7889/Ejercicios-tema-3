import helpers
from Ejercicios import Ejercicio1 as ej1
from Ejercicios import Ejercicio2 as ej2
from Ejercicios import Ejercicio3 as ej3
from Ejercicios import Ejercicio4 as ej4


def iniciar():
    while True:
        helpers.limpiar_pantalla() # cls en Windows

        print("========================")
        print("   Ejercicios tema 3  ")
        print("  ¿Cuál desea hacer? ")
        print("========================")
        print("[1]")
        print("[2]")
        print("[3]")
        print("[4]")
        print("[5]Salir")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla() # cls en Windows

        if opcion == '1':
            print("Ejercicio 1...\n")

        if opcion == '2':
            print("Ejercicio 2...\n")

        if opcion == '3':
            print("Ejercicio 3...\n")

        if opcion == '4':
            print("Ejercicio 4...\n")

        if opcion == '5':
            print("Saliendo...\n")
            break

        if opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' and opcion != '5':
            print("Opción no válida, escoja una opción del 1-5.\n")
        

        input("\nPresiona ENTER para continuar...")