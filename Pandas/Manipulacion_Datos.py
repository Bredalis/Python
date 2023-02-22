
import pandas as pd
import numpy as np

df = pd.DataFrame({

	'Columna1': [1, 2, 3, 4], 
	'Columna2': ['a', 'b', 'c', 'd']
})

# Manipulando valores

df['Columna1'][:2] = np.nan

# Sustituyendo valores

print(df['Columna1'].fillna(4))
print(df.head())  