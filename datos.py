import csv
from validaciones import validar_texto, validar_entero, validar_opcion, validar_continente

def agregar_pais(paises):
    nombre = validar_texto("Nombre del país: ")
    poblacion = validar_entero("Población: ")
    superficie = validar_entero("Superficie: ")
    continente = validar_continente("Continente: ")

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    print("País agregado correctamente.")

def actualizar_pais(paises):
    nombre_buscado = validar_texto("Ingrese el nombre del país a actualizar: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre_buscado.lower():
            print("País encontrado. Ingrese los nuevos datos: ")

            nueva_poblacion = validar_entero(f"Población actual ({pais['poblacion']}): ")
            nueva_superficie = validar_entero(f"Superficie actual ({pais['superficie']}): ")

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

def guardar_csv(nombre_archivo, paises):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")

        for pais in paises:
            linea = ",".join([pais["nombre"], str(pais["poblacion"]), str(pais["superficie"]), pais["continente"]]) + "\n"
            archivo.write(linea + "\n")