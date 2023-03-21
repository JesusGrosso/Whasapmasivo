from turtle import width
import pandas as pd
import pyautogui as pg
import webbrowser as web
import time

datos= pd.read_csv('Libro1.csv',delimiter=";")
print(datos)
data_dict = datos.to_dict('list')
celulares = data_dict['CELULARES']
nombres = data_dict['NOMBRES']
mensaje = data_dict['MENSAJE']
completo = data_dict['MENSAJE COMPLETO']
combo = zip(celulares,completo)
first= True
for celulares,completo in combo:
    time.sleep(8)
    web.open("https://web.whatsapp.com/send?phone="+celulares+"&text="+str(completo))
    if first:
        time.sleep(10)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(10)
    pg.press('enter')
    time.sleep(6)
    pg.hotkey('ctrl','w')



print(datos)