
import matplotlib.pyplot as plt
import pandas as pd

fig, Grafica = plt.subplots()

Datos = {
	
	"Habitos": ["Leer", "Programar", "Ejercicio", "Desarrollo Personal", "Ingles", "Journalist", "Practicar", "Afirmaciones"],
	"Ubicacion": [2, 4, 1, 3, 2, 1, 3, 5]
}

Habitos = pd.DataFrame(Datos)

Grafica.bar(Habitos.Habitos, Habitos.Ubicacion, color = '#EC407A')

Grafica.set_yticks(range(1, 6, 1))

plt.title("Productividad")
plt.xlabel("Habitos")

plt.show()