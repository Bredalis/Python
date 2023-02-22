
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({

	'Columna1': [1, 2, 3, 4], 
	'Columna2': ['a', 'b', 'c', 'd']
})

df['Columna1'].plot()

plt.show()