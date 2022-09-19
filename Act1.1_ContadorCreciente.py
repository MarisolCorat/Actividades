# Actividad 1.1 CONTADOR CRECIENTE

from tkinter import *
from tkinter import ttk
import tkinter as tk

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("300x150") #Tamaño de la ventana
ventana.title ("Contador Creciente") #Título en a parte superior de la ventana
ventana.config(bg="black") #color de fondo de la ventana

def Contador(): #defino funcion 
        contador.set(int(contador.get())+1) #incrementa el número del contador en 1

#CREACIÓN DE LA ETIQUETA CONTADOR
etuqietaCont = Label(ventana, text="Contador")
etuqietaCont.grid(row=0, column=0, padx=25, pady=50) #ubicación de la etiqueta dentro de la ventana

#CREACIÓN DEL ENTRY PARA VER EL CONTADOR QUE AUMENTA DE 1 EN 1
contador=tk.IntVar(ventana,1) # IntVar función que crea una nueva variable de tipo entera. Se asigna que el contador comience en un número, en este caso el "1"
etiquetaNum=ttk.Entry(state="readonly", textvariable=contador) # redonly hace que el número del entry sea de solo lectura. El textvariable en este caso va a ser el número que aparece en el entry del contador que no puede ser modificado por el usuario
etiquetaNum.grid (row=0, column=2) #ubicación del entry

#CREACIÓN DEL BOTON PARA AUMENTAR EL CONTADOR (botón "+")
boton=Button(ventana, text="+", command=Contador) #en el command se llama a la función del contador que creamos más arriba (def Contador())
boton.grid(row=0, column=3, padx=25, pady=0)


ventana.mainloop() #Muestra la ventana, sin esto no se abre la ventana, no muestra nada.