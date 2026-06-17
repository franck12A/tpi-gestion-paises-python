from validaciones import validar_texto

def buscar_pais(paises):
    nombre_buscado = validar_texto("Ingrese el nombre del país a buscar: ").lower()

    encontrado = False
    for pais in paises:
        if nombre_buscado in pais["nombre"].lower():    
            print("\nPaís encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")
            encontrado = True
    if not encontrado:
        print("País no encontrado.")
    return None
