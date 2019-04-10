import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
n = 2 ** 6  # Número de intervalos
f = 400.0  # Hz
dt = 1 / (f * 16)  # Espaciado, 16 puntos por período
t = np.linspace(0, (n - 1) * dt, n)  # Intervalo de tiempo en segundos
y = np.sin(2 * pi * f * t) - 0.5 * np.sin(2 * pi * 2 * f * t)  # Señal
plt.plot(t, y)
plt.plot(t, y, 'ko')
plt.xlabel('Tiempo (s)')
plt.ylabel('$y(t)$')