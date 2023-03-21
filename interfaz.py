from cProfile import label
from cgitb import text
from hmac import trans_36
from logging import root
from struct import pack
from tkinter import *
from tkinter.tix import COLUMN

from turtle import width
import pandas as pd
import pyautogui as pg
import webbrowser as web
import time
raiz = Tk()
datos= pd.read_csv('Libro1.csv',delimiter=";")
data_dict = datos.to_dict('list')
celulares = data_dict['CELULARES']
nombres = data_dict['NOMBRES']
mensaje = data_dict['MENSAJE']
completo = data_dict['MENSAJE COMPLETO']
combo = zip(celulares,completo)
first= True
activarMensaje=0


def enviar():
    global activarMensaje
    activarMensaje=1
    print("Enviando mensajes...")
    activacion()

def click():
    width,height = pg.size()
    pg.click(width/2,height/2)

def activacion():
    global activarMensaje
    if activarMensaje==1:
        for celulares,completo in combo:
            time.sleep(6)
            web.open("https://web.whatsapp.com/send?phone="+celulares+"&text="+str(completo))
            global first
            if first:
                time.sleep(8)
                print("Primer tiempo")
                first=False
            click()
            time.sleep(6)
            print("Segundo Tiempo")
            pg.press('enter')
            time.sleep(4)
            print("Tercer Tiempo")
            pg.hotkey('ctrl','w')
            first= True
    else:
        print("El Mensaje no se ha enviado",activarMensaje)        









raiz.title("Envios masivo de Whattsap") # titulo del programa

raiz.iconbitmap("WZ.ico") #icono tiene que estar en la misma carpeta que el archivo

#raiz.geometry("650x350") #tamaño de la ventana

raiz.config(bg="green") #color de la ventana
miFrame=Frame() #creamos un frame o cuerpo dentro de la ventana


miFrame.config(bg="green") #color del frame

foto=PhotoImage(file="whasapN.png")
imagenW= Label(raiz, image=foto,padx=10,pady=10).pack()

Comentario= Label(miFrame,text="Envios Masivos de Whatsapp",padx=10,pady=10,fg="black",font=("Arial Black",11),background="green")
Comentario.pack()

Comentario1= Label(miFrame,text="Recordatorio: Antes de abrir este programa edite primero la hoja de calculo",padx=10,pady=10,fg="black",font=("Arial Black",11),background="green")
Comentario1.pack()

Comentario2= Label(miFrame,text="Tiempo de envio por contacto: 30 segundos",padx=10,pady=10,fg="red",font=("Arial Black",8),background="green")
Comentario2.pack()

Boton=Button(raiz,text="Enviar Mensajes",command=lambda:enviar(),padx=10,pady=10).pack()



miFrame.config(width="500",height="400") #tamaño del frame
miFrame.pack() #cerramos nuestro frame o cuerpo













raiz.mainloop()








