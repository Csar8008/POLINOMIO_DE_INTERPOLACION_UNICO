# Interpolación Polinomial Única con Tkinter

Aplicación de escritorio en **Python** para encontrar y evaluar el polinomio de interpolación único que pasa por un conjunto de puntos dado $(X_i, Y_i)$.

## Características
* **Construcción del Polinomio**: Generación de la matriz de Vandermonde a partir de los puntos ingresados.
* **Resolución del Sistema**: Resolución de $AX = B$ mediante **Eliminación Gaussiana con Pivoteo Parcial**.
* **Evaluación Eficiente**: Evaluación del polinomio obtenido $P(x)$ mediante la **Regla de Horner**.
* **Interfaz Gráfica Interactiva**: Diseñada en **Tkinter** con tabla dinámica, atajos de teclado para navegación y formato claro del polinomio resultante.
* **Validaciones**: Detección de puntos duplicados en $X$ y sistemas singulares.

## Estructura del Proyecto
* `polinomio.py`: Funciones puras para evaluar y dar formato de texto a los coeficientes.
* `gauss.py`: Algoritmo de eliminación de Gauss con pivoteo parcial de filas.
* `interpolacion.py`: Módulo de validación y construcción de la matriz de Vandermonde.
* `interfaz.py`: Clase `InterfazApp` encargada del control y pintado de la GUI en Tkinter.
* `main.py`: Punto de entrada para ejecutar la aplicación.

## Requisitos e Instalación
* Python 3.x
* Módulo `tkinter` (incluido por defecto en la mayoría de las instalaciones de Python)

Para ejecutar la aplicación:
```bash
python main.py
