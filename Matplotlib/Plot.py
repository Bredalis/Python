
import matplotlib.pyplot as plt
import numpy as np

Eje_X = np.linspace(0, 20, 10)
Eje_Y = Eje_X ** 2

Eje_X_2 = np.linspace(21, 30, 10)
Eje_Y_2 = Eje_X * 2

fig, Grafica = plt.subplots()

Grafica.plot(Eje_X, Eje_Y, "rd-", Eje_X_2, Eje_Y_2, "ko:")

ticks_1 = np.arange(0, 450, 100)
ticks_2 = np.arange(0, 450, 50)

Grafica.grid(axis = "y", which = "major", color = "b", alpha = 0.5)
Grafica.grid(axis = "y", which = "minor", color = "b", alpha = 0.2, linestyle = "--")

Grafica.tick_params(axis = "y", which = "minor", labelsize = 7)

Grafica.legend(["Curva 1", "Curva 2"])

plt.show() 