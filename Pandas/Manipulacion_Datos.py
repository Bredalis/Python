
import pandas as pd
import numpy as np

DF = pd.DataFrame({

	'Columna1': [1, 2, 3, 4], 
	'Columna2': ['a', 'b', 'c', 'd']
})

# Manipulando valores

DF['Columna1'][:2] = np.nan

# Sustituyendo valores

print(DF['Columna1'].fillna(4))
print(DF.head())  