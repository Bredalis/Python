
import pandas as pd

DF = pd.DataFrame({

	'Numeros': [1, 2, 3, 4], 
	'Letras': ['a', 'b', 'c', 'd']
})

# Seleccion de filas
# Posicion

print(DF.iloc[:3])

print(DF.sort_values('Numeros', ascending = False))

# Develve los numeros de esa columna en negativo

print(DF['Numeros'].apply(lambda X: -X))