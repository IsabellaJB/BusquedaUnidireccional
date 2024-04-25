import numpy as np

def funcion_objetivo(x):
    return x**2

def busqueda_unidireccional(x_inicial, direccion, paso_maximo, tolerancia):
    x_actual = x_inicial
    while True:
        valor_actual = funcion_objetivo(x_actual)
        x_siguiente = x_actual + paso_maximo * direccion
        valor_siguiente = funcion_objetivo(x_siguiente)
        if np.abs(valor_siguiente - valor_actual) < tolerancia:
            break
        x_actual = x_siguiente
    return x_actual, funcion_objetivo(x_actual)

x_inicial = 3.0
direccion = 1.0
paso_maximo = 0.1
tolerancia = 1e-6

resultado, valor_minimo = busqueda_unidireccional(x_inicial, direccion, paso_maximo, tolerancia)

print("El mínimo de la función se encuentra en x =", resultado)
print("El valor mínimo de la función es f(x) =", valor_minimo)
