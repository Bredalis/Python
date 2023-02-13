
import matplotlib.pyplot as plt

fig, Grafico = plt.subplots(figsize = (6, 6))

Grafico.plot(

	[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 
	
	marker = 'D', markerfacecolor = '#ffff00', 
	markersize = 20, markeredgecolor = 'k', 
	fillstyle = 'top', markerfacecoloralt = 'green'

)

plt.show()