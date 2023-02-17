
import tkinter as tk
import random

Ventana = tk.Tk()
Ventana.title("Interfaces Calculator")
Ventana.geometry('700x420')
Ventana.resizable(0,0)
Ventana.config(bg = '#ffcdd2', cursor = 'cross')

Ventana.iconbitmap('C:\\Users\\Angelica Gerrero\\Desktop\\LenguajesDeProgramacion\\Icon\\ImagenesPython\\CalculadoraInterfas.ico')

Resultado = ""

Valor = tk.IntVar()

Numero = tk.StringVar()
Numero1 = tk.StringVar()
Numero2 = tk.IntVar()
Numero3 = tk.StringVar()
Numero4 = tk.StringVar()
Numero5 = tk.IntVar()
Numero6 = tk.StringVar()
Numero7 = tk.StringVar()
Numero8 = tk.IntVar()
Numero9 = tk.StringVar()
Numero10 = tk.StringVar()
Numero11 = tk.IntVar()

def Limpiar():

	Numero.set("")
	Numero1.set("")
	Numero2.set("")

	Numero3.set("")
	Numero4.set("")
	Numero5.set("")

	Numero6.set("")
	Numero7.set("")
	Numero8.set("")

	Numero9.set("")
	Numero10.set("")
	Numero11.set("")

	Etiqueta.config(text = "")

def Suma():

	Numero2.set(float(Numero.get()) + float(Numero1.get()))

def Resta():

	Numero5.set(float(Numero3.get()) - float(Numero4.get()))

def Multiplicacion():

	Numero8.set(float(Numero6.get()) * float(Numero7.get()))

def Division():

	try:

		Numero11.set(float(Numero9.get()) / float(Numero10.get()))

	except ZeroDivisionError:

		Numero11.set("Error")
	
def Comentario():

	if Valor.get() == 0:

		Etiqueta.config(text = "¡Gracias!")

	elif Valor.get() == 1:

		Etiqueta.config(text = "¡Gracias \n por comentar!")

	else:

		Etiqueta.config(text = "¡Vamos a mejor nuestra \n interfas!")

def Background_Color() :

	Colores = [

	"#ffebee", "#ffcdd2", "#ef9a9a", "#e57373", "#ef5350", "#f44336", "#e53935", "#d32f2f", "#c62828", "#b71c1c", "#ff8a80", "#ff5252",
	"#ff1744", "#d50000", "#fce4ec", "#f8bbd0", "#f48fb1", "#f06292", "#ec407a", "#e91e63", "#d81b60", "#c2185b", "#ad1457", "#880e4f",
	"#ff80ab", "#ff4081", "#f50057", "#c51162", "#f3e5f5", "#e1bee7", "#ce93d8", "#ba68c8", "#ab47bc", "#9c27b0", "#8e24aa", "#7b1fa2", 
	"#6a1b9a", "#4a148c", "#ea80fc", "#e040fb", "#d500f9", "#aa00ff", "#ede7f6", "#d1c4e9", "#b39ddb", "#9575cd", "#7e57c2", "#673ab7", 
	"#5e35b1", "#512da8", "#4527a0", "#311b92", "#b388ff", "#7c4dff", "#651fff", "#6200ea", "#e8eaf6", "#c5cae9", "#9fa8da", "#7986cb", 
	"#5c6bc0", "#3f51b5", "#3949ab", "#303f9f", "#283593", "#1a237e", "#8c9eff", "#536dfe", "#3d5afe", "#304ffe", "#e3f2fd", "#bbdefb", 
	"#90caf9", "#64b5f6", "#42a5f5", "#2196f3", "#1e88e5", "#1976d2", "#1565c0", "#0d47a1", "#82b1ff", "#448aff", "#2979ff", "#2962ff", 
	"#e1f5fe", "#b3e5fc", "#81d4fa", "#4fc3f7", "#29b6f6", "#03a9f4", "#039be5", "#0288d1", "#0277bd", "#01579b", "#80d8ff", "#40c4ff", 
	"#00b0ff", "#0091ea", "#e0f7fa", "#b2ebf2", "#80deea", "#4dd0e1", "#26c6da", "#00bcd4", "#00acc1", "#0097a7", "#00838f", "#006064", 
	"#84ffff", "#18ffff", "#00e5ff", "#00b8d4", "#e0f2f1", "#b2dfdb", "#80cbc4", "#4db6ac", "#26a69a", "#009688", "#00897b", "#00796b", 
	]

	Ventana.config(bg = random.choice(Colores))

# Suma

tk.Label(Ventana, text = "First Number", bg = 'pink').place(x = 120, y = 30)
tk.Label(Ventana, text = "Second Number", bg = 'pink').place(x = 120, y = 80)
tk.Label(Ventana, text = "Result", bg = 'pink').place(x = 120, y = 130)

tk.Entry(Ventana, justify = 'center', textvariable = Numero).place(x = 120, y = 50)
tk.Entry(Ventana, justify = 'center', textvariable = Numero1).place(x = 120, y = 100)
tk.Entry(Ventana, justify = 'center', textvariable = Numero2).place(x = 120, y = 150)

tk.Button(Ventana, text = "Sum!", bg = 'pink', activebackground = '#8D6E63', command = lambda: Suma()).place(x = 120, y = 169)

# Resta

tk.Label(Ventana, text = "First Number", bg = 'pink').place(x = 120, y = 220)
tk.Label(Ventana, text = "Second Number", bg = 'pink').place(x = 120, y = 270)
tk.Label(Ventana, text = "Result", bg = 'pink').place(x = 120, y = 330)

tk.Entry(Ventana, justify = 'center', textvariable = Numero3).place(x = 120, y = 240)
tk.Entry(Ventana, justify = 'center', textvariable = Numero4).place(x = 120, y = 290)
tk.Entry(Ventana, justify = 'center', textvariable = Numero5).place(x = 120, y = 350)

tk.Button(Ventana, text = "Rest!", bg = 'pink', activebackground = '#8D6E63', command = lambda : Resta()).place(x = 120, y = 369)

# Multiplicacion

tk.Label(Ventana, text = "First Number", bg = 'pink').place(x = 370, y = 30)
tk.Label(Ventana, text = "Second Number", bg = 'pink').place(x = 370, y = 80)
tk.Label(Ventana, text = "Result", bg = 'pink').place(x = 370, y = 130)

tk.Entry(Ventana , justify = 'center', textvariable = Numero6).place(x = 370, y = 50)
tk.Entry(Ventana , justify = 'center', textvariable = Numero7).place(x = 370, y = 100)
tk.Entry(Ventana, justify = 'center', textvariable = Numero8).place(x = 370, y = 150)

tk.Button(Ventana, text = "Multiplicaction!", bg = 'pink', activebackground = '#8D6E63', command = lambda : Multiplicacion()).place(x = 370, y = 169)

# Division

tk.Label(Ventana , text = "First Number", bg = 'pink').place(x = 370, y = 220)
tk.Label(Ventana , text = "Second Number", bg = 'pink').place(x = 370, y = 270)
tk.Label(Ventana , text = "Result", bg = 'pink').place(x = 370, y = 330)

tk.Entry(Ventana, justify = 'center', textvariable = Numero9).place(x = 370, y = 240)
tk.Entry(Ventana , justify = 'center', textvariable = Numero10).place(x = 370, y = 290)
tk.Entry(Ventana, justify = 'center', textvariable = Numero11).place(x = 370, y = 350)

tk.Button(Ventana,  text = "Division!", bg = 'pink', activebackground = '#8D6E63', command = lambda : Division()).place(x = 370, y = 369)

# Valoracion del Programa

tk.Label(Ventana, text = "Elige como te parecio : ", bg = 'pink', cursor = 'hand2').place(x = 530, y = 130)

tk.Radiobutton(Ventana, text = "Good"  , variable = Valor, value = 0, command = lambda: Comentario(), bg = 'pink', cursor = 'hand2').place(x = 530, y = 160)
tk.Radiobutton(Ventana, text = "Regular", variable = Valor, value = 1, command = lambda: Comentario(), bg = 'pink', cursor = 'hand2').place(x = 530, y = 180)
tk.Radiobutton(Ventana, text = "Bad", variable = Valor, value = 2, command = lambda: Comentario(), bg = 'pink', cursor = 'hand2').place(x = 530, y = 200)

Etiqueta = tk.Label(Ventana, bg = 'pink', cursor = 'hand2')
Etiqueta.place(x = 530, y = 250)

tk.Button(Ventana, text = "Put your favorite color", activebackground = '#8D6E63', command = lambda : Background_Color(), bg = 'pink', cursor = 'hand2').place(x = 572, y = 20)
tk.Button(Ventana, text = "Restart", activebackground = '#8D6E63', bg = "pink", command = lambda: Limpiar()).place(x = 30, y = 20)

Ventana.mainloop()