import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def funcion_objetivo(x, y):
    resultado = ((x - 10)**2) + ((y - 10)**2)
    return resultado

x = np.linspace(-15, 15, 100)
y = np.linspace(-15, 15, 100)
X, Y = np.meshgrid(x, y)
Z = funcion_objetivo(X, Y)

punto_optimo = [ 6.20689655, 11.51724138]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.scatter(*punto_optimo, color='red', label='Punto óptimo')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
plt.title('Gráfica de la función objetivo y punto óptimo')
plt.legend()
plt.show()
