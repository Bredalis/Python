
import matplotlib.pyplot as plt

fig, grafico = plt.subplots()

grafico.plot([1, 2, 3, 4], [1, 2, 4, 3], label = "dataset_1")
grafico.plot([1, 2, 3, 4], [4, 5, 6, 4], label = "dataset_2")

grafico.scatter([1, 2, 3, 4], [1.5, 5, 4.5, 5.6], label = "dataset_3")
grafico.text(

	x = 2.5, y = 2.5, s = "Elaboracion de Grafica", 
	fontsize = 15, color = 'green', 
	bbox = dict(facecolor = 'coral', edgecolor = '#003430', alpha = 0.8, boxstyle = 'larrow')

)

grafico.annotate(

	"Dinamicas", (2,2), xytext = (1, 2), fontsize = 15, 
	arrowprops = dict(arrowstyle = 'simple', facecolor = 'yellow', edgecolor = 'k'))

grafico.legend(loc = 'upper center', shadow = True, fontsize = 'x-large', facecolor = 'yellow')

plt.show()