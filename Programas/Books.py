
import pandas as pd

Datos = {

	"Desarrollo Personal": ["Ajedrez", "Piense y Hagase Rico", "Las 48 Leyes del Poder",
	"Como Ganar Amigos e Influir Sobre las Personas", "Filosofia", "Psicologia", "Habla Menos, Actua Mas", "Mente en Crecimiento"],

 	"Programacion": ["SQL","Libro Negro del Programador", "Keras", "Pytorch", "Patrones de Diseño", "Python", "Linux", "Mejor Programador"],

 	"Inteligencia Finaciera": ["Publicidad", "Probabilidad", "Inversiones", "Mercadotegnia", 
 	"Leyes de Liderasgo", "Marketing Digital", "Estadistica", "El Inversor Inteligente"],
}

Tabla_Libros = pd.DataFrame(Datos)

print(Tabla_Libros)