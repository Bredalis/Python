
import matplotlib.pyplot as plt
import numpy as np

eje_x = np.linspace(0, 20, 10)
eje_y = eje_x ** 2

eje_x_2 = np.linspace(21, 30, 10)
eje_y_2 = eje_x * 2

fig, grafico = plt.subplots()

grafico.plot(eje_x, eje_y, 'rd-', eje_x_2, eje_y_2, 'ko:')

ticks_1 = np.arange(0, 450, 100)
ticks_2 = np.arange(0, 450, 50)

grafico.grid(axis = 'y', which = 'major', color = 'b', alpha = 0.5)
grafico.grid(axis = 'y', which = 'minor', color = 'b', alpha = 0.2, linestyle = '--')

grafico.tick_params(axis = 'y', which = 'minor', labelsize = 7)

grafico.legend(["Curva 1", "Curva 2"])

plt.show() 