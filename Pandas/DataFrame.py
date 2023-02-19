
import pandas as pd

DF = pd.DataFrame({

	'Columna1': [1, 2, 3, 4], 
	'Columna2': ['a', 'b', 'c', 'd']
})

Nombres = ['Numeros', "Letras"]

DF.columns = Nombres

# Tamaño del dataframe y encabezados
# Descriccion 

print(DF.shape, DF.head())
print(DF.describe())

print(DF)