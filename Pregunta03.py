def pares_impares():
    """
    Solicita al usuario que ingrese números y realiza un seguimiento del número de números pares e impares.
    """
    cuenta_pares = 0
    cuenta_impares = 0

    while True:
        x = input("Ingresa un numero (o 'Hecho' para finalizar): ")
        if x == "Hecho":
            break
        try:
            y = float(x)
            if y % 2 == 0:
                cuenta_pares += 1
            else:
                cuenta_impares += 1
        except:
            print("Invalid input.")

    print("Numero de pares:", cuenta_pares)
    print("Numero de impares:", cuenta_impares)

pares_impares()