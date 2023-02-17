
import tkinter as tk 

class Juegos():

    def __init__(self):
        
        self.Cursor = 'hand2'
        self.Lados = 'center'
        self.Color = 'pink'
        
        self.Valor_Introduce = tk.StringVar()
        self.Valor_Invierte = tk.StringVar()
        
    def Elaboracion_Etiquetas(self):     
        
        self.Texto = tk.Label(Ventana, text = "Invierte Letras \n Introduce", cursor = self.Cursor, bg = self.Color).place(x = 90, y = 15)
            
    def Elaboracion_Entrys(self):
            
        self.Introduce = tk.Entry(Ventana, textvariable = self.Valor_Introduce, justify = self.Lados).place(x = 70, y = 52)
        self.Invierte = tk.Entry(Ventana, textvariable = self.Valor_Invierte, justify = self.Lados, fg = "grey").place(x = 70, y = 95)
        
    def Elaboracion_Boton(self):
            
        self.Resultado = tk.Button(Ventana, text = "Resultado", command = lambda: self.Invertir_Cosas(), cursor = self.Cursor, bg = self.Color).place(x = 100, y = 70)
        
    def Invertir_Cosas(self):
    
        Cosa = self.Valor_Invierte.set(self.Valor_Introduce.get()[::-1].upper())
    
        self.Limpiar()
        
    def Limpiar(self):
    
        self.Valor_Introduce.set("")

if __name__ == "__main__":
    
    Ventana = tk.Tk()
    Ventana.title("Mini - Juegos")
    Ventana.resizable(0,0)
    Ventana.geometry('260x130')
    Ventana.config(bg = '#AA00FF')
    Ventana.iconbitmap('C:\\Users\\Angelica Gerrero\\Desktop\\LenguajesDeProgramacion\\Icon\\ImagenesPython\\Toy.ico')
    
    Clase_Objeto = Juegos()
    Clase_Objeto.Elaboracion_Etiquetas()
    Clase_Objeto.Elaboracion_Entrys()
    Clase_Objeto.Elaboracion_Boton()
    
    Ventana.mainloop()