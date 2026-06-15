import csv

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

def cargar_csv(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")

    return paises