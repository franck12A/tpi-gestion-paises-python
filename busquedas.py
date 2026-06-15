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
