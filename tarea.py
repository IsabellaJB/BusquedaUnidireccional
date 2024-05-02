import numpy as np

def funcion_objetivo(x):
    x1 = x[0]
    x2 = x[1]
    resultado = ((x1 - 10)**2) + ((x2 - 10)**2)
    return resultado

def gradiente(x):
    x1 = x[0]
    x2 = x[1]
    grad = np.array([2*(x1 - 10), 2*(x2 - 10)], dtype=np.float64)
    return grad

def hessiana(x):
    return np.array([[2, 0], [0, 2]], dtype=np.float64)

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

def newton_raphson_along_direction(funcion_objetivo, gradiente, hessiana, x0, direccion, tol=1e-6, max_iter=100):
    x = x0.astype(np.float64) 
    for i in range(max_iter):
        grad = gradiente(x)
        hess = hessiana(x)
        if np.linalg.norm(grad) < tol:
            break
        direction_grad = np.dot(grad, direccion)
        if abs(direction_grad) < tol:
            break
        delta_x = - direction_grad / np.dot(np.dot(direccion, hess), direccion) * direccion
        x += delta_x
    return x

x_t = np.array([2, 1], dtype=np.float64)
s_t = np.array([2, 5], dtype=np.float64)
punto_inicial = x_t


direccion_busqueda, _ = busqueda_unidireccional(punto_inicial, s_t, funcion_objetivo)
solucion = newton_raphson_along_direction(funcion_objetivo, gradiente, hessiana, punto_inicial, direccion_busqueda)

print("Solución encontrada:", solucion)
print("Valor mínimo de la función objetivo:", funcion_objetivo(solucion))
