# gauss.py

def crear_matriz_aumentada(matriz_a, vector_b):
    matriz_aumentada = []
    for i in range(len(matriz_a)):
        fila = matriz_a[i][:] + [vector_b[i]]
        matriz_aumentada.append(fila)
    return matriz_aumentada


def resolver_sistema_gauss(matriz_a, vector_b, tol=1e-12):
    n = len(matriz_a)
    ab = crear_matriz_aumentada(matriz_a, vector_b)
    ab_inicial = [fila[:] for fila in ab]

    for i in range(n):
        max_fila = i
        for k in range(i + 1, n):
            if abs(ab[k][i]) > abs(ab[max_fila][i]):
                max_fila = k

        if max_fila != i:
            ab[i], ab[max_fila] = ab[max_fila], ab[i]

        if abs(ab[i][i]) < tol:
            raise ValueError("El sistema no tiene solución única (matriz singular).")

        for k in range(i + 1, n):
            factor = ab[k][i] / ab[i][i]
            for j in range(i, n + 1):
                ab[k][j] -= factor * ab[i][j]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(ab[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (ab[i][n] - suma) / ab[i][i]

    return x, ab_inicial