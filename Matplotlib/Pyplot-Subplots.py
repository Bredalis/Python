
import matplotlib.pyplot as plt
import numpy as np

eje_x = np.linspace(0, 2, 100)

plt.figure(figsize = (5, 2.7), layout = 'constrained')

plt.plot(eje_x, eje_x, label = 'linear')
plt.plot(eje_x, eje_x**2, label = 'quadratic')
plt.plot(eje_x, eje_x**3, label = 'cubic')

plt.title('Simple Plot')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.legend()

plt.show()