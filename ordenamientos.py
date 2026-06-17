from validaciones import validar_opcion
def ordenar_paises(paises):
    print()
    print("Ordenamiento de paises".center(70,"."))
    print("\nDatos que definen el orden: ")
    print("  1) Ordenar por nombre")
    print("  2) Ordenar por población")
    print("  3) Ordenar por superficie")
    segun_dato = validar_opcion("\nSeleccione una opción: ", ["1", "2", "3"])
    segun_dato = int(segun_dato)

    print("\nTipos de ordenamiento: ")
    print("  1) Ascendente")
    print("  2) Descendente")
    orden = validar_opcion("\nSeleccione el orden: ", ["1", "2"])
    orden = int(orden)
    orden_inverso = (orden == 2)
    orden_str = ("ascendente" if orden == 1 else "descendente")
    
    # Valores vacios para que esten definidos
    paises_ordenados = []
    criterio = ""

    # Estructura principal de ordenamiento
    if segun_dato == 1:
        paises_ordenados = sorted(paises, key=lambda x: x["nombre"].lower(), reverse=orden_inverso)
        criterio = "nombre"
    elif segun_dato == 2:
        paises_ordenados = sorted(paises, key=lambda x: x["poblacion"], reverse=orden_inverso)
        criterio = "población"
    else:
        paises_ordenados = sorted(paises, key=lambda x: x["superficie"], reverse=orden_inverso)
        criterio = "superficie"

    # El print en pantalla 
    print()
    print("RESULTADO DE ORDENAMIENTO DE PAISES".center(70,"."))
    print(f" - Datos ordenados según su {criterio}")
    print(f" - Presentados en forma {orden_str}")
    print()
    
    for p in paises_ordenados:
        print(f"País: {p['nombre']:<15} | Población: {p['poblacion']:<12} | Superficie: {p['superficie']:<10} | Continente: {p['continente']}")

    print()
    return paises_ordenados


if __name__ == "__main__":

    #Esto solo representa una prueba para verificar el codigo de esta parte
    ejemplo_paises = [{"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400,"continente": "America"},
                      {"nombre": "Japon", "poblacion": 125800000, "superficie": 377975,"continente": "Asia"},
                      {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767,"continente": "America"},
                      {"nombre": "Alemania", "poblacion": 83149300, "superficie": 357022,"continente": "Europa"}
                      ]
    
    lista_para_usar = ordenar_paises(ejemplo_paises)
