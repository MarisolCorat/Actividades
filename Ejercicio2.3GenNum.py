#Actividad 2.3 GENERADOR DE NÚMEROS ALEATRORIOS ENTRE UN RANGO ESTABLECIDO

from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("400x300")
ventana.title ("Generador de números")
ventana.config(bg="pink")

#Función para generar un número aleatorio entre un rango establecido
def Generador_Num():
    num1 = int(n1.get()) #ingreso del primer número
    num2 = int(n2.get()) #ingreso del segundo número
    if num1 == num2: #compara que el número 1 no sea igual al número 2
        msj = "Error:", num1, "=", num2 #si son iguales muestra un mensaje de error diciendo que el número 1 es igual al número 2
        resultado.set(msj)
    elif num1 > num2: #comprueba que el primer número no sea mayor al segundo número ingresado
        msj = "Error:", num1, "debe ser <", num2 #Si el número 1 es mayor que el número 2, muestra un mensaje de error
        resultado.set(msj)
    else:
        generado = random.randint(num1, num2) #genera un número aleatorio en el rango establecido entre el número 1 y el número 2
        resultado.set(generado)
    

resultado = StringVar() #para mostrar en cadena
resultado.set("")

#CREACIÓN DEL FRAME PARA COLOCAR LOS WIDGETS 
frameGenerador = Frame(ventana)
frameGenerador.place(relx= 0.5, rely=0.5, anchor=CENTER, width=300, height=200)


#CREACIÓN DE ETIQUETAS
etiqueta1 = Label(frameGenerador, text = "Número 1 ", font= ("TkFixedFont.",10))
etiqueta1.grid(row=0,column =0,padx=7,pady=7, ipady = 10 )

etiqueta2 = Label(frameGenerador, text = "Número 2 ", font= ("TkFixedFont.",10))
etiqueta2.grid(row=1,column =0,padx=7,pady=7, ipady = 10 )

etiqueta3 = Label(frameGenerador, text = "Número generado ", font= ("TkFixedFont.",10))
etiqueta3.grid(row=2,column =0,padx=7,pady=7, ipady = 10 )

#CREACIÓN DE SPINBOX (el spinbox es un campo numérico que tiene flechitas que pueden aumentar o disminuir el número al presionarla)
n1 = Spinbox(frameGenerador, from_=0,to=100,width=20,borderwidth =3,relief="groove")
n1.grid(row = 0, column = 1)
n2 = Spinbox(frameGenerador, from_=0,to=100,width=20,borderwidth =3,relief="groove")
n2.grid(row = 1, column = 1)
ResultadoGen = Entry(frameGenerador, state="readonly", textvariable=resultado, width = 25, borderwidth= 4, relief = "ridge")
ResultadoGen.grid(row = 2, column = 1)

#CREACIÓN DEL BOTÓN "generar" para generar el número aleatorio
BotonGenerar = Button(frameGenerador, text= "Generar", command=Generador_Num) # en el command se llama a la función para conectar el botón con la función de generar el número aleatorio
BotonGenerar.grid(row = 3, column =1)

ventana.mainloop() #Muestra la ventana y todo su contenido