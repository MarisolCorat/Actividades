from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
from tkinter import messagebox

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("650x450") #tamaño de la ventana
ventana.title ("Adivinador de número") #título que se muestra en la parte superior de la ventana
ventana.config(bg="deep pink")
ventana.resizable(0,0)

radio = IntVar()
entryNum1 = StringVar()
entryNum2 = StringVar()
var = StringVar()
entryNum1.set("")
entryNum2.set("")

#FUNCIÓN PARA SELECCIONAR EL IDIOMA UTILIZANDO BOTÓN RADIO
def ElegirIdioma():
    opcionIdioma = int(radio.get())
    if opcionIdioma == 1:
        "Español"
    else:
        opcionIdioma == 2
        "Ingles"

#FUNCIÓN DEL CÁLCULO MATEMÁTICO PARA ADIVINAR EL NÚMERO QUE PIENSA EL USUARIO
def calculo():
    resultado_Resta = int(entryNum1.get())
    resultado_Suma = int(entryNum2.get())
    k = ((resultado_Resta)/9)
    a = ((resultado_Suma - k )/2) 
    b = ((resultado_Suma + k )/2)   
    var=int(a), int(b)
    return messagebox.showerror("Tu numero era", var) 

#CREACIÓN DE LOS FRAMES CONTENEDORES

#frame principal que contiene el juego
frameJuego = tkinter.Frame(ventana)
frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=550, height=350)

#Frame que aparece en primera instancia para seleccionar el idioma
frame1 = tkinter.Frame(ventana, bg="turquoise1", bd = 10, relief= "ridge")
frame1.place(relx= 0.5, rely=0.5, anchor=CENTER, width=550, height=350)

#Etiqueta del frame para seleccionar el idioma
etiquetaFrame1 = Label(frame1, text ="Bienvenido a Adivina Adivinador Numérico,\n\nel juego que va a adivinar el Número que pienses, \n\npero antes de comenzar por favor, \n\nSelecciona el idioma", font= ("Arial.",12),justify="center")
etiquetaFrame1.place(x = 100, y = 30)
#Nota: es solo decoración la opción de seleccionar el idioma porque la traducción no está hecha, solo está puesto
#porque era la consigna y que debían traducirlo los estudiantes de primer año. 

#Función del botón siguiente que cambia de frame
def boton_siguiente():
    frameJuego = tkinter.Frame(ventana, bg= "cyan", bd = 10, relief="ridge")
    frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=550, height=350)
    #NOTA: el frameJuego está creado 2 veces pero si no lo creo afuera no me lo toma en los botones cuando debo
    #llamar a la función y si no lo pongo dentro de la función no cambia de frame cuando pulso el botón siguiente
    #Por ese motivo lo puse dos veces, no sé si se puede hacer de otra manera.
    
    #CREACIÓN DE ETIQUETAS DENTRO DEL FRAME DEL JUEGO PRINCIPAL Y LOS RESPECTIVOS ENTRY DONDE SE COLOCAN LOS RESULTADOS CORRESPONDIENTES 
    etiqueta1 = Label(frameJuego, text ="Estás listo? Comencemos!", font= ("Arial.",12),justify="center")
    etiqueta1.place(x = 150, y = 15)

    etiqueta2 = Label(frameJuego, text="1) Piensa un número de dos cifras que no sean iguales", font= ("Arial",12),justify="center")
    etiqueta2.place(x = 40, y = 50)

    etiqueta3 = Label(frameJuego, text="2) Ahora invierte el número y coloca el resultado de la operación. \n*Si el nuevo n° es mayor, se resta el 1ro(el que pensaste) del 2do \n*Si el nuevo n° es menor, entonces restale a este el que pensaste", font= ("Arial",12),justify="center")
    etiqueta3.place(x = 40, y = 85)

    resultado1 = Entry(frameJuego, textvariable=entryNum1) #Resultado de la resta del primer número con el segundo
    resultado1.place(x = 40, y = 155)

    etiqueta4 = Label(frameJuego, text="3) Suma los dígitos del número que pensaste y coloca el resultado", font= ("Arial",12))
    etiqueta4.place(x = 40, y = 190)

    resultado2 = Entry(frameJuego,  textvariable=entryNum2) #Resultado de la suma de los dígitos del número pensado
    resultado2.place(x = 40, y = 225)
    
    resultadoBoton = Button (frameJuego, text="Resultado", command=calculo, bd= 5) #Botón para obtener el resultado
    resultadoBoton.place(x = 40, y = 260)
    
    etiqueta5= Label(frameJuego, text= "4) El número que pensaste es: ", font= ("Arial",12))
    etiqueta5.place(x = 40, y = 295)
    
    btn_Reset = Button (frameJuego, text="Clear", command=Resetear, bd = 3) #botón para limpiar los campos
    btn_Reset.place(x = 190, y = 260)
     
    
#FUNCIÓN PARA LIMPIAR LOS CAMPOS

def Resetear():
    entryNum1.set("")
    entryNum2.set("")


#CREACIÓN DE LOS BOTONES

#rBotones de radio para elegir el idioma (Español e inglés)
botonRadioIdioma1 = Radiobutton(frame1, text="Español", variable=radio, value=1,font=("Algerian",10))
botonRadioIdioma1.place(x = 230, y = 180)

botonRadioIdioma2 = Radiobutton(frame1, text="Inglés", variable=radio, value=2,font=("Algerian",10))
botonRadioIdioma2.place(x = 230, y = 210)

#Botón siguiente para pasar al frame del juego
btn_Siguiente = Button (ventana, text="Siguiente", command= boton_siguiente, bd= 7)
btn_Siguiente.place(x = 290, y = 320)

ventana.mainloop()