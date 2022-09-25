
from __future__ import division
from tkinter import *
from tkinter import ttk
import tkinter as tk

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("400x250")
#fijamos los valores para que el usuario no extienda ni achique demasiado la ventana.
ventana.minsize(400,250) 
ventana.maxsize(400,250)
ventana.title("Calculadora")
ventana.config(bg="grey")

#CREACIÓN DEL FRAME PARA COLOCAR LOS WIDGETS
frameCalcu = Frame(ventana, bg= "peach puff")
frameCalcu.place(relx= 0.5, rely=0.5, anchor=CENTER) #centra el frame para que se ajuste al tamaño cualquiera que tome la ventana


#CREACIÓN DE LAS FUNCIONES PARA LAS DIFERENTES OPERACIONES:

def Suma():
    #no admite valores con coma
    # numero1= int(num1.get())
    # numero2= int(num2.get())
    # resultado = numero1 + numero2
    # resultadovar.set(resultado)
    #correccion
    numero1= float(num1.get()) 
    numero2= float(num2.get())
    resultado = numero1 + numero2
    resultadovar.set(resultado)


def Resta():
    numero1= int(num1.get())
    numero2= int(num2.get())
    resultado = numero1 - numero2
    resultadovar.set(resultado)

def Multiplicacion():
    numero1= int(num1.get())
    numero2= int(num2.get())
    resultado = numero1 * numero2
    resultadovar.set(resultado)

def Division():
    numero1= int(num1.get())
    numero2= int(num2.get())
    if numero2 == 0:
        mensaje="Error, división por 0"
        resultadovar.set(mensaje)
    else:
        resultado = numero1 / numero2
        resultadovar.set(resultado)

def Porcentaje():
    numero1= int(num1.get())
    numero2= int(num2.get())
    resultado = numero1/100 * numero2
    resultadovar.set(resultado)

#FUNCIÓN PARA LIMPIAR LOS CAMPOS NUMÉRICOS
def Reset():
    numero1var.set("")
    numero2var.set("")
    resultadovar.set("")

numero1var=StringVar ()
numero2var=StringVar ()
resultadovar=StringVar()
numero1var.set("")
numero2var.set("")
resultadovar.set("")

#CREACIÓN DE LAS ETIQUETAS Y LA UBICACIÓN:

textnum1=Label(frameCalcu, text= "Primer Numero")
textnum1.grid (row=0,column=0, padx=10, pady=5, ipadx=10, ipady= 0)

textnum2= Label(frameCalcu, text= "Segundo Numero")
textnum2.grid (row=1,column=0, padx=10, pady=5, ipadx=10, ipady= 0)

textresultado= Label(frameCalcu, text= "Resultado")
textresultado.grid (row=2,column=0, padx=10, pady=5, ipadx=20, ipady= 0)

#CREACIÓN DE LOS ENTRY PARA INGRESAR LOS VALORES NUMÉRICOS PARA REALIZAR LAS OPERACIONES
num1= Entry (frameCalcu, textvariable= numero1var, justify= "center", width= 24)
num1.grid(row=0,column=1, padx=10, pady=10)

num2= Entry (frameCalcu, textvariable= numero2var, justify= "center", width= 24)
num2.grid(row=1,column=1, padx=10, pady=5)

#EL RESUTADO ES NO EDITABLE (READONLY = SOLO LECTURA)
resultado = Entry (frameCalcu, state="readonly",textvariable= resultadovar, justify= "center", width= 24)
resultado.grid(row=2,column=1, padx=10, pady=5)


#CREACIÓN DE LOS BOTONES DE LAS OPERACIONES (+, -, /, x, %, clear)
suma=Button (frameCalcu, text= "+", command= Suma, width= 20)
suma.grid (row=3,column=0, padx=10, pady=3)

resta=Button (frameCalcu, text= "-", command= Resta, width= 20)
resta.grid (row=3,column=1, padx=10, pady=3)

multipicacion=Button (frameCalcu, text= "x", command= Multiplicacion, width= 20)
multipicacion.grid (row=4,column=0, padx=10, pady=3)

division=Button (frameCalcu, text= "/", command= Division, width= 20)
division.grid (row=4,column=1, padx=10, pady=3)

porcentaje=Button (frameCalcu, text= "%", command= Porcentaje, width= 20)
porcentaje.grid (row=5,column=0, padx=10, pady=3)

reset=Button (frameCalcu, text= "clear", command= Reset, width= 20)
reset.grid (row=5,column=1, padx=10, pady=3)

ventana.mainloop() #Para mostrar la ventana y todo su contenido
