def filtrar_continente():
    ...

def filtrar_poblacion():
    ...

def filtrar_superficie():
    ...
def filtrar_paises(paises):
    print("1. Filtrar por continente")
    print("2. Filtrar por población")
    print("3. Filtrar por superficie")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        filtrar_continente(paises)
    elif opcion == "2":
        filtrar_poblacion(paises)
    elif opcion == "3":
        filtrar_superficie(paises)
    else:
        print("Opción inválida.")