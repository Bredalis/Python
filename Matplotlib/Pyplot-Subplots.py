
import matplotlib.pyplot as plt
import numpy as np

Grafica = np.linspace(0, 2, 100)

plt.figure(figsize = (5, 2.7), layout = 'constrained')

plt.plot(Grafica, Grafica, label = 'linear')
plt.plot(Grafica, Grafica**2, label = 'quadratic')
plt.plot(Grafica, Grafica**3, label = 'cubic')

plt.title('Simple Plot')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.legend()

plt.show()