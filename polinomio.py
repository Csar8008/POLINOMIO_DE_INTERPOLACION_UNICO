
def limpiar_coeficientes(coeficientes, tol=1e-9):
    """Limpia coeficientes extremadamente cercanos a cero."""
    return [0.0 if abs(c) < tol else c for c in coeficientes]


def evaluar_polinomio_normal(coeficientes, x):
    resultado = 0.0
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** i)
    return resultado


def formatear_polinomio(coeficientes, decimales=4):
    terminos = []
    for i, c in enumerate(coeficientes):
        if c == 0.0 and len(coeficientes) > 1:
            continue

        valor_abs = round(abs(c), decimales)

        if i == 0:
            str_termino = f"{valor_abs}"
        elif i == 1:
            str_termino = f"{valor_abs}x" if valor_abs != 1 else "x"
        else:
            str_termino = f"{valor_abs}x^{i}" if valor_abs != 1 else f"x^{i}"

        if not terminos:
            signo = "-" if c < 0 else ""
        else:
            signo = " - " if c < 0 else " + "

        terminos.append(f"{signo}{str_termino}")

    if not terminos:
        return "P(x) = 0"

    return "P(x) = " + "".join(terminos)