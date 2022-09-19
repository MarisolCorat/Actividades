#Actividad 1.2 CONTADOR DECRECIENTE 

from tkinter import *
from tkinter import ttk
import tkinter as tk

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("300x150") #Tamaño de la ventana
ventana.title ("ContDecreciente") #Título qe se muestra en el borde superior de la ventana
ventana.config(bg="brown") #color de fondo de la ventana

#CREACIÓN DE LA FUNCIÓN PARA HACER UN CONTADOR DECRECIENTE (QUE VA A IR DE 1 EN 1 EN ESTE CASO)
def Contador():       
        contador.set(int(contador.get())-1) #hace que el contador decrezca de 1 en 1

#CREACIÓN DE LA ETIQUETA "CONTADOR"
etiquetaCon=Label(ventana, text="Contador") #Label se usa para mostrar texto en una etiqueta
etiquetaCon.grid(row=0, column=0, padx=25, pady=60)

#CREAMOS ENTRY PARA VER EL CONTADOR 
contador=tk.IntVar(ventana,88) #el contador comienza en el número 88
etiquetaNum=ttk.Entry(state="readonly", textvariable=contador) #se muestra el número del contador y no es editable
etiquetaNum.grid (row=0, column=2, padx=10)

#CREAMOS EL BOTON PARA DISMINUIR EL CONTADOR (botón "-")
boton=Button(ventana, text="-", command=Contador) #en el command se llama a la función que creamos más arriba para crear el contador decreciente
boton.grid(row=0, column=3, padx=15)

ventana.mainloop() #Muestra la ventana con todo su contenido