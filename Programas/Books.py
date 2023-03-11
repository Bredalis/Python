
import pandas as pd
import time

Datos = {

	"Desarrollo Personal": ["Piense y Hagase Rico", "Las 48 Leyes del Poder",
	"Como Ganar Amigos e Influir Sobre las Personas", "Filosofia", "Psicologia", "Habla Menos, Actua Mas", "Mente en Crecimiento"],

 	"Programacion": ["SQL", 1, "Pytorch", "Patrones de Diseño", 1, "Linux", "Mejor Programador"],

 	"Inteligencia Finaciera": ["Probabilidad", "Inversiones", "Mercadotegnia", 
 	"Leyes de Liderasgo", "Marketing Digital", "Estadistica", "El Inversor Inteligente"],
}

pd.options.display.max_columns = None

Tabla_Libros = pd.DataFrame(Datos)

print(time.strftime('%t'), "Libros")
print(Tabla_Libros)