
import pandas as pd

Datos = {

	"Desarrollo Personal": ["Ajedrez", "Piense y hagase rico", "Las 48 leyes del poder",
	"Como ganar amigos e influir sobre las personas", "Filosofia", "Psicologia", "Habla menos actua mas", "Mente de crecimiento"],

 	"Programacion": ["SQL","Libro negro del programador", "Keras", "Pytorch", "Patrones de diseño", "Python", "Linux", "Mejor Programador"],

 	"Inteligencia Finaciera": ["Publicidad", "Probabilidad", "Inversiones", "Mercadotegnia", 
 	"Leyes de liderasgo", "Marketing Digital", "Estadistica", "El inversion Inteligente"],
}

Tabla_Libros = pd.DataFrame(Datos)

print(Tabla_Libros)