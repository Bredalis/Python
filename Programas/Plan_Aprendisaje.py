
import pandas as pd
import time

Plan = pd.Series([

	"Plan",

	"Se Autodidacta", "Ten Fundamentos", "Une Puntos", 
	"Reta la Mente", "Práctica", "Aplica", 
	"Experimenta", "Ten Mentores"
])

print(time.strftime('%t'), "Pasos para aprender lo que sea")
print(time.strftime('%n'), Plan)