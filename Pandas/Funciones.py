
import pandas as pd

df = pd.DataFrame({

	'Columna1': [1, 2, 3, 4], 
	'Columna2': ['a', 'b', 'c', 'd']
})

# Seleccion de filas
# Posicion

print(df.iloc[:3])

print(df.sort_values('Columna1', ascending = False))

# Develve los numeros de esa columna en negativo

print(df['Columna1'].apply(lambda X: -X))