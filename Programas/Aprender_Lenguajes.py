
import matplotlib.pyplot as plt
import pandas as pd

fig, Grafica = plt.subplots()

Datos = {

	"Lenguajes": ["Keras", "TensorFlow", "Pytorch", "SQL", "Patrones Diseño", "Neural Network"],
	"Colores": ["#F44336","#29B6F6", "#4CAF50", "#757575", "pink", "#FFF59D"],
	"Ubicacion": [3, 4, 5, 6, 8, 9]

}

Lenguajes = pd.DataFrame(Datos)

Grafica.bar(Lenguajes.Lenguajes, Lenguajes.Ubicacion, color = Lenguajes.Colores)

Grafica.set_yticks(range(3, 10, 1))

plt.title("Lenguajes Para Aprender")
plt.ylabel("Meses")
plt.xlabel("Lenguajes")

plt.show()