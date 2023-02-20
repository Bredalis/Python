
import pandas as pd

DF = pd.DataFrame({

	'Columna1': [1, 2, 3, 4], 
	'Columna2': ['a', 'b', 'c', 'd']
})

# Seleccion de filas
# Posicion

print(DF.iloc[:3])

print(DF.sort_values('Columna1', ascending = False))

# Develve los numeros de esa columna en negativo

print(DF['Columna1'].apply(lambda X: -X))