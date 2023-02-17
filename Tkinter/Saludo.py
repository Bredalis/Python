
import tkinter as tk

roof = tk.Tk()
roof.title("¡Saludo!")
roof.resizable(0,0)

My_Frame = tk.Frame(roof, width = 500, height = 500, bg = 'pink')
My_Frame.pack()

Imagen = tk.PhotoImage()

tk.Label(My_Frame, text = "Hola Mundo de la programacion", fg = 'blue', font = (18), bg = 'pink').pack()

roof.mainloop()