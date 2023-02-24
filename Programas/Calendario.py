
import calendar

# Funciones que validan los diferentes inputs

def Numero(Numero):

    try:
        Numero = int(Numero)

    except:
        Numero = Numero(input("Caracter no valido: "))
    
    return Numero

def Opciones(Opciones):

    while Opciones != ("Si") and Opciones != ("No"):

        print(chr(7)); Opciones = input("Escribe solo \'Si\' o \'No\' según su opción: ")

    return(Opciones)

def OPCION_A_B(Opcion_Entrada):

    while Opcion_Entrada != ("A") and Opcion_Entrada != ("B"):

        Opcion_Entrada = input("Escriba solo \'A\' o \'B\' segun su opción: ")

    return Opcion_Entrada

def Year(Year_Entrada):

    while Year_Entrada < 1 or Year_Entrada > 9999:

        Year_Entrada = Numero(input("Introduzca un año valido: "))

    return Year_Entrada

def MES(Mes_Entrada):

     while Mes_Entrada < 1 or Mes_Entrada > 12:

        Mes_Entrada = Numero(input("Introduzca un mes valido: "))

     return Mes_Entrada

while True:

    print("\n------------------------------CALENDARIOS------------------------------\n")
    
    print("""Escoja una opción:
        A)Ver los calendarios correspondientes a un determinado año.
        B)Ver el calendario correspondiente a un año y mes determinados.
        """)
    
    Opcion = OPCION_A_B(input("Introduzca su opción(A/B): "))

    if Opcion == ("A"):

        Year = Year(Numero(input("Introduce el año cuyos calendarios desea ver: ")))
        
        Calendario_Texto = calendar.TextCalendar()

        Calendario = Calendario_Texto.formatyear(Year)

    else:

        Year = Year(Numero(input("Introduzca el año: ")))
        Mes = MES(Numero(input("Introduzca mes: ")))

        Calendario_Texto = calendar.TextCalendar()

        Calendario = Calendario_Texto.formatmonth(Year , Mes)

    print("\n" + Calendario)
        
    Opcion_Continuar = Opciones(input("¿Desea continuar?(Si/No): "))

    if Opcion_Continuar == ("No"):
            
        break