
import matplotlib.pyplot as plt
import pandas as pd

fig, Grafica = plt.subplots()

Datos = {

	"Lenguajes": ["Keras", "TensorFlow", "Pytorch", "SQL", "Notion", "Patrones Diseño", "Neural Network"],
	"Ubicacion": [3, 4, 5, 6, 7, 8, 9]

}

Lenguajes = pd.DataFrame(Datos)

Grafica.bar(Lenguajes.Lenguajes, Lenguajes.Ubicacion, color = '#00ACC1')

Grafica.set_yticks(range(3, 10, 1))

plt.title("Lenguajes Para Aprender")
plt.ylabel("Meses")
plt.xlabel("Lenguajes")

plt.show()