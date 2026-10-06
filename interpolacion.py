from gauss import resolver_sistema_gauss


def validar_puntos(puntos_x):
    if len(puntos_x) != len(set(puntos_x)):
        raise ValueError("Existen valores de 'X' duplicados. Cada X_i debe ser único.")


def construir_matriz(puntos_x):
    n = len(puntos_x)
    matriz_a = []
    for x in puntos_x:
        fila = [x ** i for i in range(n)]
        matriz_a.append(fila)
    return matriz_a


def calcular_interpolacion(puntos_x, puntos_y):
    if len(puntos_x) < 2:
        raise ValueError("Se requieren al menos 2 puntos para interpolar.")

    if len(puntos_x) != len(puntos_y):
        raise ValueError("La cantidad de valores en X y Y debe ser igual.")

    validar_puntos(puntos_x)

    matriz_a = construir_matriz(puntos_x)
    vector_b = list(puntos_y)

    coeficientes, matriz_aumentada = resolver_sistema_gauss(matriz_a, vector_b)
    return coeficientes, matriz_aumentada