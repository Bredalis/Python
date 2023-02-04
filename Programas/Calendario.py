
import calendar

def Validacion_Numero(Numero):

    try:

        Numero = int(Numero)

    except:

        Numero = Validacion_Numero(input("Caracter no valido: "))
    
    return Numero

def Validacion_Opciones(Opciones):

    while Opciones != ("Si") and Opciones != ("No"):

        print(chr(7)); Opciones = input("Escribe solo \'Si\' o \'No\' según su opción: ")

    return(Opciones)

def VALIDAR_OPCION_A_B(Opcion_Entrada):

    while Opcion_Entrada != ("A") and Opcion_Entrada != ("B"):

        Opcion_Entrada = input("Escriba solo \'A\' o \'B\' segun su opción: ")

    return Opcion_Entrada

def VALIDAR_Year(Year_Entrada):

    while Year_Entrada < 1 or Year_Entrada > 9999:

        Year_Entrada = Validacion_Numero(input("Introduzca un año valido: "))

    return Year_Entrada

def VALIDAR_MES(Mes_Entrada):

     while Mes_Entrada < 1 or Mes_Entrada > 12:

        Mes_Entrada = Validacion_Numero(input("Introduzca un mes valido: "))

     return Mes_Entrada

while True:

    print("\n------------------------------CALENDARIOS------------------------------\n")
    
    print("""Escoja una opción:
        A)Ver los calendarios correspondientes a un determinado año.
        B)Ver el calendario correspondiente a un año y mes determinados.
        """)
    
    Opcion = VALIDAR_OPCION_A_B(input("Introduzca su opción(A/B): "))

    if Opcion == ("A"):

        Year = VALIDAR_Year(Validacion_Numero(input("Introduce el año cuyos calendarios desea ver: ")))
        
        Calendario_Texto = calendar.TextCalendar()

        Calendario = Calendario_Texto.formatyear(Year)

    else:

        Year = VALIDAR_Year(Validacion_Numero(input("Introduzca el año: ")))
        Mes = VALIDAR_MES(Validacion_Numero(input("Introduzca mes: ")))

        Calendario_Texto = calendar.TextCalendar()

        Calendario = Calendario_Texto.formatmonth(Year , Mes)

    print("\n" + Calendario)
        
    Opcion_Continuar = Validacion_Opciones(input("¿Desea continuar?(Si/No): "))

    if Opcion_Continuar == ("No"):
        
        break