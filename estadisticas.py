def mostrar_estadisticas(paises):
    if not paises:
            print("No hay paises cargados.")
            return
    print("1. Mayor y menor población")
    print("2. Promedio de población")
    print("3. Promedio superficie")
    print("4. Cantidad por continente")
    print("5. Mostrar todos los paises")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        mayor = paises[0]
        menor = paises[0]
        for pais in paises:
            if  pais["poblacion"] > mayor["poblacion"]:
                mayor = pais
            if pais["poblacion"] < menor["poblacion"]:
                menor = pais

        print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
        print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    elif opcion == "2":
        total_poblacion = 0
        for pais in paises:
            total_poblacion += pais["poblacion"]

        promedio = total_poblacion / len(paises)
        print(f"Promedio de población: {promedio}")

    elif opcion == "3":
        total_superficie = 0
        for pais in paises:
            total_superficie += pais["superficie"]

        promedio = total_superficie / len(paises)
        print(f"Promedio de superficie: {promedio}")
    elif opcion == "4":
        continentes = {}
        for pais in paises:
            if pais["continente"] not in continentes:
                continentes[pais["continente"]] = 1
            else:
                continentes[pais["continente"]] += 1
        for continente in continentes:
            print(f"{continente}: {continentes[continente]} países")
    elif opcion == "5":
        for pais in paises:
            for continente, cantidad in continentes.items():
                print(f"{continente}: {cantidad} países")
    else:
        print("Opción inválida.")