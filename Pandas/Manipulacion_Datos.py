
import pandas as pd
import numpy as np

DF = pd.DataFrame({

	'Numeros': [1, 2, 3, 4], 
	'Letras': ['a', 'b', 'c', 'd']
})

# Manipulando valores

DF['Numeros'][:2] = np.nan

# Sustituyendo valores

print(DF['Numeros'].fillna(0))
print(DF.head())  