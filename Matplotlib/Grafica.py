
import matplotlib.pyplot as plt
import numpy as np

Fig, Grafica = plt.subplots()

X = np.arange(4)

Grafica.plot(X, [1, 2, 4, 3])

plt.title('Primera Grafica')

plt.show()