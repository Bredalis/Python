
import pandas as pd
import matplotlib.pyplot as plt

DF = pd.DataFrame({

	'Coordenadas': [1, 2, 3, 4], 
	'Letras': ['a', 'b', 'c', 'd']
})

DF['Coordenadas'].plot()

plt.suptitle("Coordenadas")
plt.show()