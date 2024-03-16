def contar_digitos(numero, digito):
    # Convertir el número a una cadena para repetir sobre cada dígito
    numero_str = str(numero)
    
    # Iniciar222 el contador de ocurrencias del dígito
    contador = 0
    
    # Repetir sobre cada dígito en el número y contar las ocurrencias del dígito dado
    for d in numero_str:
        if d == str(digito):
            contador += 1
    
    # Devolver la cantidad de veces que aparece el dígito en el número
    return contador

# Pedir al usuario que ingrese el número y el dígito
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese un dígito: "))

# Calcular la cantidad de veces que aparece el dígito en el número
cantidad = contar_digitos(numero, digito)

# Mostrar el resultado
print(f"La cantidad de veces que el dígito {digito} aparece en el número {numero} es: {cantidad}")
