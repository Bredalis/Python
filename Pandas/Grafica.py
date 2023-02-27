
import pandas as pd
import matplotlib.pyplot as plt

DF = pd.DataFrame({

	'Coordenadas': [1, 2, 3, 4], 
})

DF.plot()

plt.suptitle("Grafica")
plt.show()