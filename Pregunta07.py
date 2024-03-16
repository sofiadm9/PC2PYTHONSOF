def test_prime(n):
    """
    Comprobar si un número 'n' es un número primo.
    """
    if n == 1:
        # 1 no es numero primo
        return False
    elif n == 2:
        # 2 es numero primo
        return True
    else:
        # Repetirr a través de números del 2 al (n-1)
        for x in range(2, n):
            # Comprueba si 'n' es divisible por 'x' sin resto
            if n % x == 0:
                # Si 'n' es divisible por 'x', no es un número primo
                return False
        # Si 'n' no es divisible por ningún número entre 2 y (n-1), es un número primo
        return True

# Comprueba si el 7 es un número primo.
print("Es 7 un numero primo?", test_prime(7))
