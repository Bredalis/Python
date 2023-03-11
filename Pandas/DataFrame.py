
import pandas as pd

DF = pd.DataFrame({

	'Numeros': [1, 2, 3, 4], 
	'Letras': ['a', 'b', 'c', 'd']
})

Nombres = ['Numeros', "Letras"]

DF.columns = Nombres

# Tamaño del dataframe y encabezados
# Descriccion 

print(DF.shape)
print(DF.head())
print(DF.describe())

print(DF)