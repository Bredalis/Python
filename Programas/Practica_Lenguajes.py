
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.pyplot as plt
import pandas as pd

fig, Grafica = plt.subplots()

Datos = {

	"Lenguajes": ["Git", "Numpy", "Pandas", "Python", "Matplotlib", "Keras", "OS", "EDITORES", "SQL", "Tkinter"],
	"Colores": ["#F4511E","#29B6F6", "#E0E0E0", "#4CAF50", "pink", "#E53935", "#FFF59D", "#424242", "#BDBDBD", "#F48FB1"],
	"Ubicacion": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

Lenguajes = pd.DataFrame(Datos)

Grafica.bar(Lenguajes.Lenguajes, Lenguajes.Ubicacion, color = Lenguajes.Colores)

Grafica.yaxis.set_major_locator(MultipleLocator(1))

Grafica.tick_params(axis = 'y', which = 'minor', labelsize = 12)
Grafica.tick_params(axis = 'x', which = 'minor', labelsize = 12)

plt.title("Lenguajes a Practicar")
plt.ylabel("Meses")
plt.xlabel("Lenguajes")

plt.show()