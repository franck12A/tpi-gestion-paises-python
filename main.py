#from datos import *
#from busquedas import *
#from filtros import *
#from ordenamientos import *
#from estadisticas import *


def mostrar_menu():
    print("===== MENU =====")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("7. Salir")
paises = []
def agregar_pais(paises):
    nombre = input("Nombre del país: ")
    poblacion = int(input("Población: "))
    superficie = int(input("Superficie: "))
    continente = input("Continente: ")

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    print("País agregado correctamente.")

def actualizar_pais(paises):
    nombre_buscado = input("Ingrese el nombre del país a actualizar: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre_buscado.lower():
            print("País encontrado. Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")

            nueva_poblacion = input(f"Población actual ({pais['poblacion']}): ")
            nueva_superficie = input(f"Superficie actual ({pais['superficie']}): ")

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            print("País actualizado correctamente.")
            return
    print("País no encontrado.")
            

def buscar_pais(paises, nombre):
    nombre_buscado = input("Ingrese el nombre del país a buscar: ")

    encontrado = False
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("\nPaís encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            encontrado = True
    if not encontrado:
        print("País no encontrado.")
    return None

def filtrar_paises(paises):
    poblacion_min = int(input("Ingrese la población mínima: "))
    poblacion_max = int(input("Ingrese la población máxima: "))
    superficie_min = int(input("Ingrese la superficie mínima: "))
    superficie_max = int(input("Ingrese la superficie máxima: "))

    print("1. Continente")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Seleccione el criterio de filtrado: ")

    if opcion == "1":
        continente = input("Ingrese el continente: ")
        for pais in paises:
            if pais["continente"].lower() == continente.lower():
                print(f"País: {pais['nombre']} - Continente: {pais['continente']}")

    elif opcion == "2":
        for pais in paises:
            if poblacion_min <= int(pais["poblacion"]) <= poblacion_max:
                print(f"País: {pais['nombre']} - Población: {pais['poblacion']}")

    elif opcion == "3":
        for pais in paises:
            if superficie_min <= int(pais["superficie"]) <= superficie_max:
                print(f"País: {pais['nombre']} - Superficie: {pais['superficie']}")

    else:
        print("Opción inválida.")


while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pais(paises)
    elif opcion == "2":
        actualizar_pais(paises)
    elif opcion == "3":
        nombre = input("Nombre del país a buscar: ")
        pais = buscar_pais(paises, nombre)
        if pais:
            print(f"País encontrado: {pais['nombre']}")
        else:
            print("País no encontrado.")

    elif opcion == "4":
        filtrar_paises(paises)

    elif opcion == "5":
        print("Ordenar países")

    elif opcion == "6":
        print("Mostrar estadísticas")

    elif opcion == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")