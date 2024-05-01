import numpy as np

def funcion_objetivo(x):
    x1 = x[0]
    x2 = x[1]
    resultado = ((x1 - 10)**2) + ((x2 - 10)**2)
    return resultado

def busqueda_unidireccional(punto_inicial, direccion_busqueda, funcion_objetivo, paso_alpha=0.01):
    def evaluar_objetivo_en_alpha(alpha):
        x_alpha = punto_inicial + alpha * direccion_busqueda
        return funcion_objetivo(x_alpha)
    
    valor_minimo = float('inf')
    punto_minimo = None
    alpha = 0.0
    while alpha <= 1.0:
        valor_actual = evaluar_objetivo_en_alpha(alpha)
        if valor_actual < valor_minimo:
            valor_minimo = valor_actual
            punto_minimo = punto_inicial + alpha * direccion_busqueda
        alpha += paso_alpha
    return punto_minimo, valor_minimo


punto_inicial = np.array([0, 0])
direccion_busqueda = np.array([1, 1])

punto_minimo, valor_minimo = busqueda_unidireccional(punto_inicial, direccion_busqueda, funcion_objetivo)

print("Punto mínimo:", punto_minimo)
print("Valor mínimo:", valor_minimo)
