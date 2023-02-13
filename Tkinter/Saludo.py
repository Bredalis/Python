
import tkinter as tk

root = tk.Tk()
root.title("¡Saludo!")
root.resizable(0,0)

My_Frame = tk.Frame(root, width = 500, height = 500, bg = 'pink')
My_Frame.pack()

Imagen = tk.PhotoImage()

tk.Label(My_Frame, text = "Hola Mundo de la programacion", fg = 'blue', font = (18), bg = 'pink').pack()

root.mainloop()