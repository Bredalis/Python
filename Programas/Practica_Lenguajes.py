
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.pyplot as plt
import pandas as pd

fig, Grafica = plt.subplots()

Datos = {

	"Lenguajes": ["Git", "Numpy", "Pandas", "Python", "Matplotlib", "Keras", "OS", "EDITORES", "SQL"],
	"Ubicacion": [1, 2, 3, 4, 5, 6, 7, 8, 9]

}

Lenguajes = pd.DataFrame(Datos)

Grafica.bar(Lenguajes.Lenguajes, Lenguajes.Ubicacion, color = '#8C9EFF')

Grafica.yaxis.set_major_locator(MultipleLocator(1))

Grafica.tick_params(axis = 'y', which = 'minor', labelsize = 12)
Grafica.tick_params(axis = 'x', which = 'minor', labelsize = 12)

plt.title("Lenguajes a Practicar")
plt.ylabel("Meses")
plt.xlabel("Lenguajes")

plt.show()