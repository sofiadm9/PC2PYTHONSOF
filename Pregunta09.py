def eliminar_vocales(text):
    """
    Devuelve una cadena con todas las vocales (A, E, I, O y U) eliminadas, independientemente de si son
     ingresado en mayúsculas o minúsculas.
    """
    vocales = set("aeiouAEIOU")
    return "".join(c for c in text if c not in vocales)

# Solicitar a la usuario una cadena de texto
text = input("Introduzca una cadena de texto: ")

# Quitar las vocales de la cuerda.
resultado = eliminar_vocales(text)

# Imprime la cadena resultante
print("Result:", resultado)