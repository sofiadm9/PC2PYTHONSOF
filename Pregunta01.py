# Un programa para encontrar números que son divisibles por 7 y múltiplos de 5, en el rango de 1500 a 2700 (inclusive)

# Inicializa los valores de inicio y fin del rango
inicio = 1500
fin = 2700

# Recorre el rango
for num in range(inicio, fin + 1):
    # Verifica si el número es divisible por 7 y múltiplo de 5
    if num % 7 == 0 and num % 5 == 0:
        # Imprime el número
        print(num)
