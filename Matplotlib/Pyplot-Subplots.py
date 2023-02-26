
import matplotlib.pyplot as plt
import numpy as np

Eje_X = np.linspace(0, 2, 100)

plt.figure(figsize = (5, 2.7), layout = 'constrained')

plt.plot(Eje_X, Eje_X, label = 'linear')
plt.plot(Eje_X, Eje_X**2, label = 'quadratic')
plt.plot(Eje_X, Eje_X**3, label = 'cubic')

plt.title('Simple Plot')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.legend()

plt.show()