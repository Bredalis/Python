
import tkinter as tk

Ventana = tk.Tk()
Ventana.title("Registro")
Ventana.config(bg = 'pink')
Ventana.geometry('300x300')
Ventana.resizable(0,0)
Ventana.iconbitmap('C:\\Users\\Angelica Gerrero\\Desktop\\LenguajesDeProgramacion\\Icon\\ImagenesPython\\Registro_2.ico')

Titulo = tk.Label(Ventana, text = "Grupo Informatico", pady = 30, font = (10), bg = 'pink').pack()
Mi_Frame = tk.Frame(Ventana, height = 190, width = 260, bg = 'aqua').pack()

Opcion = tk.IntVar()
Valor_Integrantes = tk.StringVar()
Valor_Lenguajes = tk.StringVar()
Valor_Informacion = tk.StringVar()
Valor_Texto = tk.StringVar()

Registro = tk.Label(Mi_Frame, text = "Registro Formulario", font = (15), bg = 'aqua').place(x = 60, y = 100)
Integrantes = tk.Label(Mi_Frame, text = "Integrantes", bg = 'aqua').place(x = 40, y = 140)
Lenguajes = tk.Label(Mi_Frame, text = "Lenguajes", bg = 'aqua').place(x = 40, y = 170)
Informacion = tk.Label(Mi_Frame, text = "Informacion Educativa", bg = 'aqua').place(x = 40, y = 200)
Registrado = tk.Label(Mi_Frame, bg = 'aqua', textvariable = Valor_Texto).place(x = 150, y = 240)

Integrantes = tk.Entry(Mi_Frame, width = 15, justify = 'center', textvariable = Valor_Integrantes).place(x = 180, y = 140)
Lenguajes = tk.Entry(Mi_Frame, width = 15, justify = 'center', textvariable = Valor_Lenguajes).place(x = 180, y = 170)
Informacion = tk.Entry(Mi_Frame, width = 15, justify = 'center', show = "*", textvariable = Valor_Informacion).place(x = 180, y = 200)

def Uploaded_log():
    
    Folden_Registrado = open("Datos_De_Grupo.txt", 'a')
    
    Folden_Registrado.write(Valor_Integrantes.get())
    Folden_Registrado.write("\n")
    Folden_Registrado.write(Valor_Lenguajes.get())
    Folden_Registrado.write("\n")
    Folden_Registrado.write(Valor_Informacion.get())
    Folden_Registrado.write("\n\n")
    Folden_Registrado.close()

    [Valor_Integrantes.set(""), Valor_Lenguajes.set(""), Valor_Informacion.set(""), Valor_Texto.set("")]

    Valor_Texto.set("Registrado y Guardado")

def Reinicio():

	if Opcion.get() == 1:

		Valor_Texto.set("")

Texto_Final = tk.Button(Mi_Frame, width = 10, text = "Registrado", activebackground = 'aqua', command = lambda: Uploaded_log()).place(x = 60, y = 255)

Boton_Reinicio = tk.Checkbutton(Mi_Frame, text = "Reinicio", variable = Opcion, onvalue = 1, offvalue = 0, bg = 'pink', command = lambda: Reinicio()).place(x = 10, y = 10)

Ventana.mainloop()