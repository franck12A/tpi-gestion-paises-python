from datos import agregar_pais, actualizar_pais
from busquedas import buscar_pais
from filtros import filtrar_paises
from ordenamientos import ordenar_paises
from estadisticas import mostrar_estadisticas
from datos import cargar_csv

def mostrar_menu():
    print("===== MENU =====")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("7. Salir")
paises = cargar_csv("paises.csv")



while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pais(paises)
    elif opcion == "2":
        actualizar_pais(paises)
    elif opcion == "3":
        buscar_pais(paises)

    elif opcion == "4":
        filtrar_paises(paises)
    elif opcion == "5":
        ordenar_paises(paises)

    elif opcion == "6":
        mostrar_estadisticas(paises)

    elif opcion == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")