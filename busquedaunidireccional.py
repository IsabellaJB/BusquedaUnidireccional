import numpy as np

def funcion_objetivo(x):
    # Función objetivo: (x1 - 10)^2 + (x2 - 10)^2
    x1 = x[0]
    x2 = x[1]
    resultado = ((x1 - 10)**2) + ((x2 - 10)**2)
    return resultado

def busqueda_unidireccional(x_inicial, direccion, paso_maximo, tolerancia):
    x_actual = np.array(x_inicial) 
    direccion = np.array(direccion) 
    while True:
        valor_actual = funcion_objetivo(x_actual)
        x_siguiente = x_actual + paso_maximo * direccion
        valor_siguiente = funcion_objetivo(x_siguiente)
        if np.abs(valor_siguiente - valor_actual) < tolerancia:
            break
        x_actual = x_siguiente
    return x_actual, funcion_objetivo(x_actual)


x_inicial = [3.0, 3.0]
direccion = [1.0, 1.0]
paso_maximo = 0.1
tolerancia = 1e-6
resultado, valor_minimo = busqueda_unidireccional(x_inicial, direccion, paso_maximo, tolerancia)

print("El mínimo de la función se encuentra en x =", resultado)
print("El valor mínimo de la función es f(x) =", valor_minimo)
