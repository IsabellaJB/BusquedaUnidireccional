import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def funcion_objetivo(x):
    x1 = x[0]
    x2 = x[1]
    resultado = ((x1 - 10)**2) + ((x2 - 10)**2)
    return resultado




def primera_derivada(x, funcion):
    delta = 0.0001
    return (funcion(x + delta) - funcion(x - delta)) / (2 * delta)

def segunda_derivada(x, funcion):
    delta = 0.0001
    return (funcion(x + delta) - 2 * funcion(x) + funcion(x - delta))/(delta**2)

def newton_raphson(x, funcion, e):
    k = 0
    while True:
        x_derivada1 = primera_derivada(x, funcion)
        x_derivada2 = segunda_derivada(x, funcion)
        x_siguiente = x - (x_derivada1 / x_derivada2)
        if abs(x_siguiente - x) < e:
            return x_siguiente
        x = x_siguiente
        k += 1
        if k > 1000:
            return None



def busqueda_unidireccional(x, s, funcion, e):
    def objetivo(alpha):
        return funcion(x + alpha * s)
    alpha_optimo = newton_raphson(0, objetivo, e)
    return alpha_optimo

def optimizador_unidireccional(x_t, s_t, funcion, e):
    alpha_optimo = busqueda_unidireccional(x_t, s_t, funcion, e)
    x_alpha_optimo = x_t + alpha_optimo * s_t
    return x_alpha_optimo




x_t = np.array([2, 1])
s_t = np.array([2, 5])





punto_optimo = optimizador_unidireccional(x_t, s_t, funcion_objetivo, 0.0001)
print("Punto óptimo:", punto_optimo)

print(funcion_objetivo(x_t))
print(funcion_objetivo(punto_optimo))