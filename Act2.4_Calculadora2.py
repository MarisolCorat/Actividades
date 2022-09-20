#Actividad 2.4 CALCULADORA 2

from __future__ import division
from tkinter import *
from tkinter import ttk
import tkinter as tk

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("400x300") #tamaño de la ventana
ventana.title ("CALCULADORA 2") #título que se muestra en la parte superior de la ventana
ventana.config(bg="pink") #color de fonde de la ventana

#CREACIÓN DE LAS FUNCIONES. UNA PARA CADA OPERACIÓN

def Suma():
    numero1= int(num1.get()) #ingreso del valor 1
    numero2= int(num2.get()) #ingreso del valor 2
    resultado = numero1 + numero2
    resultadovar.set(resultado) #variable para mostrar el resultado

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
    if numero2 == 0: #si el valor 2 es igual a 0, muestra un mensaje de error que no se puede dividir por 0
        mensaje="error, división por 0"
        resultadovar.set(mensaje)
    else:
        resultado = numero1 / numero2 #si es diferente a 0, hace la operación con normalidad
        resultadovar.set(resultado)
        
#CREACIÓN DE LA FUNCIÓN PARA REALIZAR LA OPERACIÓN CORRESPONDIENTE DE ACUERDO A LA OPCIÓN SELECCIONADA POR EL USUARIO
def Opciones_Calculos():
    opcion = int(opcRadio.get())
    if opcion == 1:
        Suma()
    elif opcion == 2:
        Resta()
    elif opcion == 3:
        Multiplicacion()
    elif opcion == 4:
        Division()
    else:
        msj = "Debe seleccionar una opción"
        
#Se convierten los números en variable string para mostrarlos como cadena
numero1var=StringVar ()
numero2var=StringVar ()
resultadovar=StringVar()
opcRadio =StringVar()
numero1var.set("")
numero2var.set("")
resultadovar.set("")

#Creación del frame, cuadro contenedor para colocar los widgets
frameCalcu = Frame(ventana)
frameCalcu.place(relx= 0.5, rely=0.5, anchor=CENTER, width=350, height=200)

#CREAMOS LAS ETIQUETAS CON LOS RESPECTIVOS NOMBRES
etiqueta1 = Label(frameCalcu, text = "Valor 1 ", font= ("TkFixedFont.",10))
etiqueta1.grid(row=0, column =0, padx=7, pady=7)

etiqueta2 = Label(frameCalcu, text = "Valor 2 ", font= ("TkFixedFont.",10))
etiqueta2.grid(row=1,column =0, padx=7, pady=7)

etiqueta3 = Label(frameCalcu, text = "Resultado ", font= ("TkFixedFont.",10))
etiqueta3.grid(row=2,column =0, padx=7, pady=7)

etiqueta4 = Label(frameCalcu, text = "Operaciones", font= ("TkFixedFont.",10))
etiqueta4.grid(row=0,column =2, padx=7, pady=7)

num1= Entry (frameCalcu, textvariable= numero1var)
num1.grid(row=0,column=1, padx=10)

num2= Entry (frameCalcu, textvariable= numero2var)
num2.grid(row=1,column=1, padx=10, pady=0)

resultado = Entry (frameCalcu, state="readonly",textvariable= resultadovar)
resultado.grid(row=2,column=1, padx=10, pady=0)

#CREACIÓN DE LOS BOTONES DE SELECCIÓN
opc_Sumar = Radiobutton(frameCalcu, text = "Sumar", variable= opcRadio, value = 1) # en value ee le asigna un valor a cada botón para luego realizar la operación correspondiente de acuerdo al valor que tenga(definidos en el def Opciones_Calculos():)
opc_Sumar.grid(row=1, column=2, sticky="w", padx = 5, pady = 5)

opc_Restar = Radiobutton(frameCalcu, text = "Restar", variable= opcRadio, value = 2)
opc_Restar.grid(row=2, column=2, sticky="w", padx = 5, pady = 5)

opc_Multiplicar = Radiobutton(frameCalcu, text = "Multiplicar", variable= opcRadio, value = 3)
opc_Multiplicar.grid(row=3, column=2, sticky="w", padx = 5, pady = 5)

opc_Dividir = Radiobutton(frameCalcu, text = "Dividir", variable= opcRadio, value = 4)
opc_Dividir.grid(row=4, column=2, sticky="w", padx = 5, pady = 5)

#BOTÓN CALCULAR
botonCalcular = Button(frameCalcu, text = "Calcular", width=10, borderwidth=5, command= Opciones_Calculos) #en el command se invoca a la función para conectar el botón con las operaciones y poder hacer el cálculo
botonCalcular.grid(row = 3, column=1)

ventana.mainloop() #Muesta la ventana y su contenido