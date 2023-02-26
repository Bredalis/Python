
import tkinter as tk

Window = tk.Tk()
Window.title("¡Saludo!")
Window.resizable(0,0)

tk.Label(Window, text = "Hola Mundo de la programacion", fg = 'blue', font = (25), bg = 'pink').pack()

Window.mainloop()