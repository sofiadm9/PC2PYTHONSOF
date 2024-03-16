# Definir una función llamada 'factorial' que calcule el factorial de un número 'n'
def factorial(n):
    # Comprobar si el número 'n' es 0
    if n == 0:
        # Si 'n' es 0, devuelve 1 (el factorial de 0 es 1)
        return 1
    else:
        # Si 'n' no es 0, llama recursivamente a la función 'factorial' con (n-1) y multiplícala por 'n'
        return n * factorial(n - 1)

# Solicite al usuario que ingrese un número para calcular su factorial y almacenarlo en la variable 'n'
n = int(input("Ingrese un número para calcular el factorial: "))

# Imprime el factorial del número ingresado por el usuario llamando a la función 'factorial'
print(factorial(n))
