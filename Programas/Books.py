
import pandas as pd

Datos = {

	"Desarrollo Personal": ["Piense y Hagase Rico", "Las 48 Leyes del Poder",
	"Como Ganar Amigos e Influir Sobre las Personas", "Filosofia", "Psicologia", "Habla Menos, Actua Mas", "Mente en Crecimiento"],

 	"Programacion": ["SQL", "Keras", "Pytorch", "Patrones de Diseño", "Python", "Linux", "Mejor Programador"],

 	"Inteligencia Finaciera": ["Probabilidad", "Inversiones", "Mercadotegnia", 
 	"Leyes de Liderasgo", "Marketing Digital", "Estadistica", "El Inversor Inteligente"],
}

pd.options.display.max_columns = None

Tabla_Libros = pd.DataFrame(Datos)

print(f"Libros \n {Tabla_Libros}")