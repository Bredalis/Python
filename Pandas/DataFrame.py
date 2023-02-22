
import pandas as pd

df = pd.DataFrame({

	'Columna1': [1, 2, 3, 4], 
	'Columna2': ['a', 'b', 'c', 'd']
})

nombres = ['Numeros', "Letras"]

df.columns = nombres

# Tamaño del dataframe y encabezados
# Descriccion 

print(df.shape, df.head())
print(df.describe())

print(df)