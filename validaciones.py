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
            if numero > 0:
                return numero
            else:
                print("Error: ingrese un número entero positivo.")
        except ValueError:
            print("Error: ingrese un número entero válido.")
        

def validar_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones:
            return opcion
        else:
            print(f"Error: opción inválida. Elija entre {', '.join(opciones)}.")
def validar_continente(mensaje):
    while True:
        origen = input(mensaje).strip().capitalize()
        if origen in ["America", "Europa", "Asia", "Africa", "Oceania", "Antartida"]:
                return origen
        else:
            print("Error: continente inválido. Elija entre América, Europa, Asia, África u Oceanía.")
