from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
from tkinter import messagebox

#CREACIÓN DE LA VENTANA
ventana = Tk()
ventana.geometry("680x450") #tamaño de la ventana
ventana.title ("Adivinador de número") #título que se muestra en la parte superior de la ventana
ventana.config(bg="deep pink") #Color de fondo de la ventana
ventana.resizable(0,0) #no permite cambiar el tamaño de la ventana desde la nterfaz

#conversión de variables a string o int según corresponda
radio = IntVar()
entryNum1 = StringVar()
entryNum2 = StringVar()
var = StringVar()
entryNum1.set("") # el método set() asigna un valor a una variable. Se usa para modificar el valor
entryNum2.set("")

#Creación del frame principal, que contiene el juego.
frameJuego = tkinter.Frame(ventana)
frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=350)

#Frame que aparece en primera instancia para seleccionar el idioma
frame1 = tkinter.Frame(ventana, bg="turquoise1", bd = 10, relief= "ridge")
frame1.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=350)

#Etquetas de inicio que dan la bienvenida y piden seleccionar el idioma. Se muestran en español e inglés
etiqueta1Frame1 = Label(frame1, text ="Bienvenido a Adivina Adivinador Numérico,\n\nel juego que va a adivinar el Número que pienses, \n\npero antes de comenzar por favor, \n\nSelecciona el idioma", font= ("Arial.",9),justify="left")
etiqueta1Frame1.place(x = 10, y = 30)
etiqueta2Frame1 = Label(frame1, text = "Welcome to Guess Number Guess,\n\nthe game that will guess the Number you think of,\n\nbut before you start please,\n\nSelect the language", font= ("Arial.",9),justify= "left")
etiqueta2Frame1.place(x = 295, y= 30)
    
#Función para limpiar los campos
def resetear():
    entryNum1.set("")
    entryNum2.set("")

#Función para seleccionar el idioma y pasar al frame siguiente correspondiente
def opcionIdioma():
    varFunction = int(radio.get())
    if varFunction == 1:
        boton_siguiente1()
    elif varFunction == 2:
        boton_siguiente2()
    else:
        messagebox.showwarning("Error","Seleccione un Idioma.") #Si no selecciona un idioma, muestra el mensaje que debe seleccionar un idioma

#Creación de botones radio para seleccionar el idioma (Español e inglés)
botonRadioIdioma1 = Radiobutton(frame1, text="Español", variable=radio, value=1,font=("Algerian",10))
botonRadioIdioma1.place(x = 250, y = 180)

botonRadioIdioma2 = Radiobutton(frame1, text="Inglés", variable=radio, value=2,font=("Algerian",10))
botonRadioIdioma2.place(x = 250, y = 210)

#Condicional para seleccionar entre un idioma y otro

if botonRadioIdioma1:
    def boton_siguiente1(): #Idioma español
        frameJuego = tkinter.Frame(ventana, bg= "cyan", bd = 10, relief="ridge")
        frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=350)
        def calculo1(): #función para realizar los cálculos correspondientes solicitados por el juego
            resultado_Resta = int(entryNum1.get())
            resultado_Suma = int(entryNum2.get())
            k = ((resultado_Resta)/9)
            a = ((resultado_Suma - k )/2) 
            b = ((resultado_Suma + k )/2)   
            var=int(a), int(b)
            return messagebox.showerror("Tu numero era: ", var) 

        def validar(char): #funcion para validar datos. Esta función permite ingresar solo números y el signo negativo
            return char in "0123456789-"
        validatecommand = ventana.register(validar)
        
        #Creación de etiquetas que dan las intrucciones del juego
        etiqueta1 = Label(frameJuego, text ="Estás listo? Comencemos!", font= ("Arial.",12),justify="center")
        etiqueta1.place(x = 150, y = 15)

        etiqueta2 = Label(frameJuego, text="1) Piensa un número de dos cifras que no sean iguales", font= ("Arial",12),justify="center")
        etiqueta2.place(x = 40, y = 50)

        etiqueta3 = Label(frameJuego, text="2) Ahora invierte el número y coloca el resultado de la operación. \n*Si el nuevo n° es mayor, se resta el 1ro(el que pensaste) del 2do \n*Si el nuevo n° es menor, entonces restale a este el que pensaste", font= ("Arial",12),justify="center")
        etiqueta3.place(x = 40, y = 85)

        #Creación del primer "entry" para ingresar el primer resultado de la operación que solicita el juego
        resultado1 = Entry(frameJuego, textvariable=entryNum1) #Resultado de la resta del primer número con el segundo
        resultado1.place(x = 40, y = 155)
        resultado1.config( validate="key", validatecommand=(validatecommand, "%S" ))#validacion de datos, solo permite ingresar números  

        etiqueta4 = Label(frameJuego, text="3) Suma los dígitos del número que pensaste y coloca el resultado", font= ("Arial",12))
        etiqueta4.place(x = 40, y = 190)

        #Creación del segundo "entry" para ingresar el segundo resultado solicitado por el juego
        resultado2 = Entry(frameJuego,  textvariable=entryNum2) #Resultado de la suma de los dígitos del número pensado al principio
        resultado2.place(x = 40, y = 225)
        resultado2.config( validate="key", validatecommand=(validatecommand, "%S" )) #Validación, solo permite ingresar números 
        
        resultadoBoton = Button (frameJuego, text="Resultado", command=calculo1, bd= 5) #Botón para obtener el resultado
        resultadoBoton.place(x = 40, y = 255)
        
        etiqueta5= Label(frameJuego, text= "4) El número que pensaste es: ", font= ("Arial",12))
        etiqueta5.place(x = 40, y = 295)
        
        btn_Reset = Button (frameJuego, text="limpiar", command=resetear, bd = 4) #botón para limpiar los campos. En el comando llama a la función "resetear"
        btn_Reset.place(x = 195, y = 257)
        
    #creación del botón Siguiente/Next que pasa al frame del juego   
    btn_Siguiente = Button (ventana, text="Siguiente/\nNext", command= opcionIdioma, bd= 7) #En el comando llama a la función "opcionIdioma" que pasa al frame siguiente en el idioma seleccionado
    btn_Siguiente.place(x = 300, y = 320)

#segundo condicional, para el idioma inglés
#Es el mismo código del primer condicional pero con  las sentencias en inglés
if botonRadioIdioma2:
    def boton_siguiente2():
        frameJuego = tkinter.Frame(ventana, bg= "cyan", bd = 10, relief="ridge")
        frameJuego.place(relx= 0.5, rely=0.5, anchor=CENTER, width=600, height=350)
        def calculo2():
            resultado_Resta = int(entryNum1.get())
            resultado_Suma = int(entryNum2.get())
            k = ((resultado_Resta)/9)
            a = ((resultado_Suma - k )/2) 
            b = ((resultado_Suma + k )/2)   
            var=int(a), int(b)
            return messagebox.showerror("your number is: ", var)

        #Función para vaidar datos, solo permite ingresar números y el signo negativo 
        def validar(char): 
            return char in "0123456789-"
        validatecommand = ventana.register(validar) 
            
        #Etiquetas en idioma inglés
        etiqueta1 = Label(frameJuego, text ="Are you ready? Let's start!", font= ("Arial.",12),justify="center")
        etiqueta1.place(x = 150, y = 15)

        etiqueta2 = Label(frameJuego, text="1) Think of a two-digit number that is not the same", font= ("Arial",12),justify="left")
        etiqueta2.place(x = 20, y = 50)

        etiqueta3 = Label(frameJuego, text="2) Now reverse the number and place the result of the operation. \n*If the new n° is greater, subtract the 1st (the one you thought of) from the 2nd \n*If the new n° is less, then subtract the one you thought of", font= ("Arial",12),justify="left")
        etiqueta3.place(x = 20, y = 85)

        resultado1 = Entry(frameJuego, textvariable=entryNum1) #Resultado de la resta del primer número con el segundo
        resultado1.place(x = 20, y = 155)
        resultado1.config( validate="key", validatecommand=(validatecommand, "%S" ))#validacion, permite ingresar solo números y el signo negativo 

        etiqueta4 = Label(frameJuego, text="3) Add the digits of the number you thought of and put the result", font= ("Arial",12), justify="left")
        etiqueta4.place(x = 20, y = 190)

        resultado2 = Entry(frameJuego,  textvariable=entryNum2) #Resultado de la suma de los dígitos del número pensado
        resultado2.place(x = 20, y = 225)
        resultado2.config( validate="key", validatecommand=(validatecommand, "%S" ))#validacion, permite ingresar solo números y el signo negativo  
            
        resultadoBoton = Button (frameJuego, text="Result", command=calculo2, bd= 5) #Botón para obtener el resultado
        resultadoBoton.place(x = 20, y = 255)
            
        etiqueta5= Label(frameJuego, text= "4) The number you thought of is: ", font= ("Arial",12))
        etiqueta5.place(x = 20, y = 295)
            
        btn_Reset = Button (frameJuego, text="Clear", command=resetear, bd = 4) #botón para limpiar los campos
        btn_Reset.place(x = 190, y = 255)
    
ventana.mainloop()
