from validaciones import validar_opcion
def filtrar_continente(paises):
    lista_continentes = ["America", "Asia", "Africa", "Antartida", "Europa", "Oceania"]
    paises_continente_elegido = []
    print("Seleccione el continente: ")
    for i, c in enumerate(lista_continentes):
        print(f" {i+1}) {c}")
    opc= validar_opcion("\nSeleccione una opción: ", [str(i) for i in range(1, len(lista_continentes)+1)])
    opc = int(opc)
    continente_elegido = lista_continentes[opc-1]

    for pais in paises:
        if pais["continente"] == continente_elegido:
            paises_continente_elegido.append(pais)
        else:
            continue

    return paises_continente_elegido, continente_elegido


def filtrar_poblacion(paises):
    while True:
        minimo = False
        maximo = False
        print("Ingrese el valor mínimo para filtrar. En caso de no usar minimos, dejar vacio y presionar ENTER")
        poblacion_min = input("Población mínima: ")

        print("Ingrese el valor máximo para filtrar. En caso de no usar máximos, dejar vacio y presionar ENTER")
        poblacion_max = input("Población máxima: ")

        if poblacion_min.isdigit():
            poblacion_min = int(poblacion_min)
            minimo = True
        if poblacion_max.isdigit():
            poblacion_max = int(poblacion_max)
            maximo = True

        if maximo and minimo:
            if poblacion_min < poblacion_max:
                break
            else:
                continue
        elif maximo:
            poblacion_min = 0
            break
        elif minimo:
            poblacion_max = float('inf')
            break
        else:
            poblacion_min = 0
            poblacion_max = float('inf')
            break
    
    lista_fitrada = []
    for p in paises:
        if p["poblacion"] > poblacion_min and p["poblacion"] < poblacion_max:
            lista_fitrada.append(p)
        else:
            continue
    return lista_fitrada

    

def filtrar_superficie(paises):
    while True:
        minimo_s = False
        maximo_s = False
        print("Ingrese el valor mínimo para filtrar. En caso de no usar minimos, dejar vacio y presionar ENTER")
        superficie_min = input("Superficie mínima: ")

        print("Ingrese el valor máximo para filtrar. En caso de no usar máximos, dejar vacio y presionar ENTER")
        superficie_max = input("Superficie máxima: ")

        if superficie_min.isdigit():
            superficie_min = int(superficie_min)
            minimo_s = True
        if superficie_max.isdigit():
            superficie_max = int(superficie_max)
            maximo_s = True

        if maximo_s and minimo_s:
            if superficie_min < superficie_max:
                break
            else:
                continue
        elif maximo_s:
            superficie_min = 0
            break
        elif minimo_s:
            superficie_max = float('inf')
            break
        else:
            superficie_min = 0
            superficie_max = float('inf')
            break
    
    lista_fitrada = []
    for p in paises:
        if p["superficie"] > superficie_min and p["superficie"] < superficie_max:
            lista_fitrada.append(p)
        else:
            continue
    return lista_fitrada


def filtrar_paises(paises):
    print("Filtro de paises".center(70,"."))
    print("Filtrar por: ")
    print(" 1) Continente")
    print(" 2) Población")
    print(" 3) Superficie")
    opcion = validar_opcion("\nSeleccione una opción: ", ["1", "2", "3"])
    paises_filtro_aplicado = []
    criterio = ""

    if opcion == "1":
        paises_filtro_aplicado, continente_criterio = filtrar_continente(paises)
        criterio = "continente"
    elif opcion == "2":
        paises_filtro_aplicado = filtrar_poblacion(paises)
        criterio = "población"
    elif opcion == "3":
        paises_filtro_aplicado = filtrar_superficie(paises)
        criterio = "superficie"


    print()
    print("RESULTADO DE FILTRO DE PAISES".center(70,"."))
    print(f" - Datos filtrados por {criterio}")
    if criterio == "continente":
        print(f" - Continente elegido: {continente_criterio}")
    print()
    
    if paises_filtro_aplicado == []:
        print("No hay paises que coincidan con los criterios elegidos")
    else:
        for p in paises_filtro_aplicado:
            print(f"País: {p['nombre']:<15} | Población: {p['poblacion']:<12} | Superficie: {p['superficie']:<10} | Continente: {p['continente']}")
    print()

    return paises_filtro_aplicado



if __name__ == "__main__":
    #Esto solo representa una prueba para verificar el codigo de esta parte
    ejemplo_paises = [{"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400,"continente": "América"},
                      {"nombre": "Japon", "poblacion": 125800000, "superficie": 377975,"continente": "Asia"},
                      {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767,"continente": "América"},
                      {"nombre": "Alemania", "poblacion": 83149300, "superficie": 357022,"continente": "Europa"}
                      ]
    
    lista_para_usar = filtrar_paises(ejemplo_paises)