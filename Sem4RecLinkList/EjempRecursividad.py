# Triangulo de Pascal recursivamente
def imprimir_piramide(n, nivel=1):
    if n < 1:
        return
    imprimir_piramide(n - 1, nivel + 1)
    print(' ' * (nivel - 1) + '*' * (2 * n - 1))

# Ejemplo de uso:
altura = 5
imprimir_piramide(altura)