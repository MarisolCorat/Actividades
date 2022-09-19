# Actividad 1.4 CONTADOR CRECIENTE Y DECRECIENTE

from tkinter import *
from tkinter import ttk
import tkinter as tk

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("600x200")
ventana.title("Contador")
ventana.config(bg="grey")

frameCont = Frame(ventana, bg = "dark turquoise") #Creación de un frame(cuadro contenedor) para colocar los widgets
frameCont.place(relx= 0.5, rely=0.3, anchor=CENTER)

campoNum= StringVar() #Convertir el campo numérico en variable string para mostrar el número
campoNum.set(0)

#CREACIÓN DE FUNCIÓN PARA CONTADOR CRECIENTE
def Botonup():
        numero= int (campo.get())
        numero +=1
        campoNum.set(numero)

#CREACIÓN DE FUNCIÓN PARA CONTADOR DECRECIENTE
def BotonDown():
        numero= int (campo.get())
        numero -=1
        campoNum.set(numero)

#CREACIÓN DE FUNCIÓN PARA RESETEAR EL CAMPO NUMÉRICO
def BotonReset():
    numero=0
    campoNum.set(numero)

textocont=Label(frameCont, text="Contador" ,width = 10, font= ("TkFixedFont",10), bg = "misty rose")
textocont.grid(row=0,column=0, padx=10, pady=10, ipady = 4)
#Se coloca frameCont para colocar las etiquetas dentro del frame.
#text = texto de la etiqueta "contador"

#CREACIÓN LineEdit que comienza en 0 y no puede ser modificada por el usuario(Solo lectura)
campo= Entry (frameCont, state="readonly", textvariable=campoNum, justify = "center", width = 10, font= ("TkFixedFont",10))
campo.grid(row=0 , column=1, padx=10, pady=0, ipady= 4)

#CREACIÓN DEL BOTON PARA AUMENTAR EL CONTADOR 
boton=Button(frameCont, text="Count Up", command=Botonup, borderwidth=5, width = 10, font= ("TkFixedFont",10), bg = "dark olive green1") #llamo a funcion 
boton.grid(row=0, column=3, padx=10, pady=0)

#CREACIÓN DEL BOTON  PARA LA FUNCION DECRECIENTE
boton2=Button(frameCont, text="Count Down", command=BotonDown, borderwidth=5, width = 10, font= ("TkFixedFont",10), bg ="light steel blue")
boton2.grid(row=0, column=4, padx=10, pady=0)

#CREACIÓN DEL BOTÓN PARA RESETEAR EL CONTADOR A 0
boton3=Button(frameCont, text=" Reset ", command=BotonReset, borderwidth=5, width = 10, font= ("TkFixedFont",10), bg = "plum1")
boton3.grid(row=0, column=5, padx=10, pady=0)


ventana.mainloop()
