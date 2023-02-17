
import tkinter as tk

Ventana = tk.Tk()
Ventana.title("Registro")
Ventana.config(bg = 'pink')
Ventana.geometry('300x300')
Ventana.resizable(0,0)
Ventana.iconbitmap('C:\\Users\\Angelica Gerrero\\Desktop\\LenguajesDeProgramacion\\Icon\\ImagenesPython\\Registro_2.ico')

tk.Label(Ventana, text = "Grupo Informatico", pady = 30, font = (10), bg = 'pink').pack()

Mi_Frame = tk.Frame(Ventana, height = 190, width = 260, bg = 'aqua').pack()

Opcion = tk.IntVar()

Integrantes = tk.StringVar()
Lenguajes = tk.StringVar()
Informacion = tk.StringVar()
Texto = tk.StringVar()

tk.Label(Mi_Frame, text = "Registro Formulario", font = (15), bg = 'aqua').place(x = 60, y = 100)
tk.Label(Mi_Frame, text = "Integrantes", bg = 'aqua').place(x = 40, y = 140)
tk.Label(Mi_Frame, text = "Lenguajes", bg = 'aqua').place(x = 40, y = 170)
tk.Label(Mi_Frame, text = "Informacion Educativa", bg = 'aqua').place(x = 40, y = 200)
tk.Label(Mi_Frame, bg = 'aqua', textvariable = Texto).place(x = 150, y = 240)

tk.Entry(Mi_Frame, width = 15, justify = 'center', textvariable = Integrantes).place(x = 180, y = 140)
tk.Entry(Mi_Frame, width = 15, justify = 'center', textvariable = Lenguajes).place(x = 180, y = 170)
tk.Entry(Mi_Frame, width = 15, justify = 'center', show = "*", textvariable = Informacion).place(x = 180, y = 200)

def Uploaded_log():
    
    Archivo_Registrado = open("Datos_De_Grupo.txt", 'a')
    
    Archivo_Registrado.write(Integrantes.get())
    Archivo_Registrado.write("\n")
    Archivo_Registrado.write(Lenguajes.get())
    Archivo_Registrado.write("\n")
    Archivo_Registrado.write(Informacion.get())
    Archivo_Registrado.write("\n\n")
    Archivo_Registrado.close()

    [Integrantes.set(""), Lenguajes.set(""), Informacion.set(""), Texto.set("")]

    Texto.set("Registrado y Guardado")

def Reinicio():

	if Opcion.get() == 1:

		Texto.set("")

tk.Button(Mi_Frame, width = 10, text = "Registrado", activebackground = 'aqua', command = lambda: Uploaded_log()).place(x = 60, y = 255)

tk.Checkbutton(Mi_Frame, text = "Reinicio", variable = Opcion, onvalue = 1, offvalue = 0, bg = 'pink', command = lambda: Reinicio()).place(x = 10, y = 10)

Ventana.mainloop()