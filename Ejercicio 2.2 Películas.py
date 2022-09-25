# Actividad 2.2 PELICULAS 

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("600x400")
ventana.title("Películas")
ventana.config(bg="black")

#CREACIÓN DEL FRAME PARA COLOCAR LOS WIDGETS
framePeli = Frame(ventana, bg= "darkolivegreen3")
framePeli.place(relx= 0.5, rely=0.5, anchor=CENTER, width=500, height=350) #width=ancho height=largo

#CREACIÓN DE LA FUNCIÓN PARA AÑADIR EL TÍTULO DE UNA PELÍCULA A UNA LISTA
def Peliculas():
    a = peli.get()
    # entrada=input()
    #VALIDACION PARA QUE NO INGRESE CADENAS VACÍAS EN EL LISTBOX
    if (a.isspace() or len(a) <= 1):
        messagebox.showinfo(message="El nombre de la película no debe comenzar con un espacio", title="Error")
    else:
        listaPeli.insert(END,a)
        peli.delete(0,END)


#CONVERTIR VARIABLES PARA QUE SE VEAN EN ENTRY EN VARIABLE TIPO CADENA 
peli=StringVar()
peli.set("")

#CREACIÓN DE LAS ETIQUETAS (LABEL)

#TÍTULO DE PELÍCULA 
tituloPeli=Label(framePeli,width=24,borderwidth =2, font= ("arial",10),text= "Escribe el título de una película: ",bg="pink")
tituloPeli.grid(row=1, column=0, padx=10,pady=30)

#Peliculas
peliculas=Label(framePeli,width=15,borderwidth =2,relief="ridge",font= ("Arial Black",10),text="Peliculas", bg="light blue")
peliculas.grid(row=1, column=1,padx=10,pady=10)

#entry para escribir el título de la película que se desea añadir
peli=Entry (framePeli, textvariable=Peliculas ,width=25,borderwidth =3, relief="groove")
peli.grid(row=2,column=0 ,padx=5, pady=5, ipadx=10, ipady= 5)

#CREACIÓN DE LA LISTA PARA GUARDAR PELI
listaPeli=Listbox(framePeli,width=35, borderwidth =3, relief="sunken",font=("Arial",10))
listaPeli.grid(row=2,column=1, padx=5,pady=5)

#crear boton 
añadir=Button(framePeli,text="Añadir", width=18,borderwidth =6,relief="groove",font=("Cooper Black",10), bg="salmon",command=Peliculas)
añadir.grid(row=3,column=0)

ventana.mainloop()

#lita Peli = listbox para crear lista para guardar lista de pelicula 
#insert = se inserta la película en en la lista 
