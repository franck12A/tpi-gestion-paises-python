def mostrar_estadisticas(paises):
    if not paises:
            print("No hay países cargados para mostrar estadísticas.")
            return
    print("\n===== MENÚ DE ESTADÍSTICAS =====")
    print("1. País con mayor y menor población")
    print("2. Promedio de población")
    print("3. Promedio de superficie")
    print("4. Cantidad de países por continente")
    print("===============================\n")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        mayor = paises[0]
        menor = paises[0]
        for pais in paises:
            if  pais["poblacion"] > mayor["poblacion"]:
                mayor = pais
            if pais["poblacion"] < menor["poblacion"]:
                menor = pais

        print("\n===== MAYOR Y MENOR POBLACIÓN =====")
        print(f"País con mayor población: {mayor['nombre']}")
        print(f"Habitantes: {mayor['poblacion']}")

        print()

        print(f"País con menor población: {menor['nombre']}")
        print(f"Habitantes: {menor['poblacion']}")
    elif opcion == "2":
        total_poblacion = 0
        for pais in paises:
            total_poblacion += pais["poblacion"]

        promedio = total_poblacion / len(paises)
        print("\n===== PROMEDIO DE POBLACIÓN =====")
        print(f"Población promedio: {promedio}")
    elif opcion == "3":
        total_superficie = 0
        for pais in paises:
            total_superficie += pais["superficie"]
        
        promedio = total_superficie / len(paises)
        print("\n===== PROMEDIO DE SUPERFICIE =====")
        print(f"Superficie promedio: {promedio}")
    elif opcion == "4":
        continentes = {}
        for pais in paises:
            if pais["continente"] not in continentes:
                continentes[pais["continente"]] = 1
            else:
                continentes[pais["continente"]] += 1
        print("\n===== CANTIDAD DE PAÍSES POR CONTINENTE =====")
        for continente in continentes:
            print(f"{continente}: {continentes[continente]} países")

    else:
        print("Opción inválida.")