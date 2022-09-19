#Actividad 1.3 FACTORIAL 

from tkinter import *
from tkinter import ttk
import tkinter as tk
import math

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("550x200") #Tamaño de la ventana
ventana.title ("FACTORIAL") #Título que se muestra en a parte superior de la ventana
ventana.config(bg="brown1") #Color de fondo de a ventana

#CREACIÓN DE LA FUNCIÓN DEL CÁLCULO DEL FACTORIAL
def Factorial(): #Se define la función asignándole un nombre que sea en lo posible lo más representativo     
    calculo = int(numero.get())+1 #fórmula para calcular el factorial de un número
    lineEditResult.config(text= math.factorial(calculo))
    for i in range(calculo): #se crea un ciclo for para que a medida que incremente el número de "n" en 1, muestra el factorial del número respectivo
        numero.set(calculo)


#CREACIÓN DE LA ETIQUETA "n"
etiqueta = Label(ventana, width=5, text = "n", font= ("Arial",10), bg = "seagreen1")
etiqueta.grid(row=0, column =0, padx=20, pady=60)

#CREACIÓN DE lineEdit PARA "n", no editable
numero=IntVar(value=0)                                                   
lineEdit = Entry(ventana, width=10, justify = "center", textvariable=numero, state= "readonly",font= ("Arial",10))
lineEdit.grid (row=0, column = 1, padx=10, pady=60)

#CREACIÓN ETIQUETA "Factorial (n)"
etiqueta = Label(ventana, text = "Factorial (n) ",font= ("Arial",10), bg = "seagreen1")
etiqueta.grid(row=0, column =2, padx = 5, pady = 60)

#CREACIÓN DE lineEdit no editable PARA "factorial n"
lineEditResult=Label(ventana, width = 20, font= ("Arial",10)) #
lineEditResult.grid(row=0, column=3, padx=5, pady=60)

#CREACIÓN DEL BOTÓN "Siguiente"
boton = Button(ventana, width = 10, borderwidth= 3, text = "Siguiente", font= ("Arial",10), command= Factorial, bg = "SkyBlue3") #En el botón de invoca a la función del factorial para que se conecten
boton.grid (row=0, column=4, padx=5,pady=60) #ubicación del botón

ventana.mainloop()