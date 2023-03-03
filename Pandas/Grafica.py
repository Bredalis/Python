
import pandas as pd
import matplotlib.pyplot as plt

DF = pd.DataFrame({

	'Coordenadas': [1, 6, 3, 8]
})

DF.plot()

plt.suptitle("Grafica")
plt.show()