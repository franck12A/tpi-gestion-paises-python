def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("Error: no puede estar vacío.")

def validar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: ingrese un número entero válido.")

def validar_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones:
            return opcion
        else:
            print(f"Error: opción inválida. Elija entre {', '.join(opciones)}.")

