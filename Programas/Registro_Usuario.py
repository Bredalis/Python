
import tkinter as tk

Ventana = tk.Tk()
Ventana.title("Registro De Usuario")
Ventana.config(bg = 'pink')
Ventana.geometry('500x500')
Ventana.resizable(0,0)
Ventana.iconbitmap('C:\\Users\\Angelica Gerrero\\Desktop\\LenguajesDeProgramacion\\Icon\\ImagenesPython\\Registro_2.ico')

tk.Button(Ventana, text = "Registro", font = (15), fg = '#1F618D', bg = '#D0D3D4', width = 40, command = lambda: Data_cleansing()).place(x = 60, y = 400)

Titulo = tk.Label(Ventana, text = "Registro De Usuario", pady = 30, font = (10), bg = 'pink').pack()
Mi_Frame = tk.Frame(Ventana, height = 300, width = 400, bg = 'aqua').pack()

Resultado = ""
Valor_Usuario = tk.StringVar()
Valor_Caracter = tk.StringVar()
Valor_Caracter.set(".com")
Valor_Contraseña = tk.StringVar()
Valor_Numero = tk.IntVar()
Valor_Texto = tk.StringVar()

Registro = tk.Label(Mi_Frame, text = "Registrarme :", font = (15), bg = 'aqua').place(x = 60, y = 100)

Usuario = tk.Label(Mi_Frame, text = "Nombre De Usuario", bg = 'aqua').place(x = 70, y = 140)
Usuario = tk.Entry(Mi_Frame, width = 40, justify = 'center', textvariable = Valor_Usuario).place(x = 180, y = 140)

Email = tk.Label(Mi_Frame, text = "E-mail", bg = 'aqua').place(x = 70, y = 170)
Email = tk.Entry(Mi_Frame, width = 40, justify = 'center', textvariable = Valor_Caracter).place(x = 180, y = 170)

Contraseña = tk.Label(Mi_Frame, text = "Contraseña", bg = 'aqua').place(x = 70, y = 200)
Contraseña = tk.Entry(Mi_Frame, width = 40, justify = 'center', show = "*", textvariable = Valor_Contraseña).place(x = 180, y = 200)

Numero_Celular = tk.Label(Mi_Frame, text = "Telefono", bg = 'aqua').place(x = 70, y = 230)
Numero_Celular = tk.Entry(Mi_Frame, width = 40, justify = 'center', textvariable = Valor_Numero).place(x = 180, y = 240)

Registrado = tk.Label(Mi_Frame, bg = 'aqua', textvariable = Valor_Texto).place(x = 210, y = 340)

def Uploaded_log():

	global Resultado

	if(Valor_Caracter.get()):

		Resultado = Valor_Texto.set("Registrado y Guardado")

		Folden_Registrado = open("Registro_De_Usuario.txt", 'a')

		Folden_Registrado.write(Valor_Usuario.get())
		Folden_Registrado.write("\n")
		Folden_Registrado.write(Valor_Caracter.get())
		Folden_Registrado.write("\n")
		Folden_Registrado.write(Valor_Contraseña.get())
		Folden_Registrado.write("\n")
		Folden_Registrado.write(str(Valor_Numero.get()))
		Folden_Registrado.close()

	elif(Valor_Caracter.get() != ".com" and Valor_Caracter.get() == ""):
		Resultado = Valor_Texto.set("No Se Pudo Registrar")

def Data_cleansing():

	global Resultado

	Resultado = [Valor_Usuario.set(""), Valor_Caracter.set(".com"), Valor_Contraseña.set(""), Valor_Numero.set(""), Valor_Texto.set("")]

Texto_Final = tk.Button(Mi_Frame, width = 40, text = "Registrado", command = lambda: Uploaded_log()).place(x = 60, y = 300)

Ventana.mainloop()