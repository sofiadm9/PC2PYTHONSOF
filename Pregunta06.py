def fibonacci_secuencia(limit):
    """
    Generar la secuencia de Fibonacci hasta un límite dado.

    Args:
    limit (int): El límite de la secuencia de Fibonacci.

    Yields:
    int: El siguiente número en la secuencia de Fibonacci.
    """
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Generar la Fibonacci secuencia entre 0 y 50
fibonacci_secuencia_gen = fibonacci_secuencia(50)
fibonacci_secuencia = [next(fibonacci_secuencia_gen) for _ in range(10)]

# Print la Fibonacci secuencia
print(fibonacci_secuencia)