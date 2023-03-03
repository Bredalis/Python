
import tkinter as tk

Window = tk.Tk()
Window.title("¡Saludo!")
Window.resizable(0,0)

tk.Label(Window, text = "Hola Mundo De La Programacion", fg = "#884EA0", font = (25), bg = 'pink', padx = 10, pady = 10).pack()

Window.mainloop()