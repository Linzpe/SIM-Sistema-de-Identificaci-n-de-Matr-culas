# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:08:37 2024

@author: Angel Gomez Hurtado
@author: Javier Linzoain Pedraza

"""
import RPi.GPIO as GPIO
import time
import subprocess
import tkinter as tk
import time
import subprocess
import tkinter as tk
from tkinter import ttk
import threading

GPIO.setwarnings(False)  # Desactiva las advertencias GPIO
GPIO.cleanup()          # Limpia cualquier configuración previa

GPIO.setmode(GPIO.BCM)

TRIG = 17  # pines de la Raspberry (salida del ultrasonido)
ECHO = 27 # pin de la Raspberry (entrada del ultrasonido)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def calculaDistancia():
    # Ponemos en bajo el trigger y esperamos medio segundo para que se estabilice:
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.5)
    
    # Lanzamos un pulso de 10 us:
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    
    # OJO, IMPORTANTE. El echo se pone HIGH cuando se envía la señal por el trigger.
    # esto lo hace el sensor automáticamente.
    while True:
        inicio = time.time()
        if GPIO.input(ECHO) == GPIO.HIGH: #SIGNIFICA QUE SE HA ENVIADO EL PULSO Y EMPIEZA A MEDIR
            break
    
    # Ahora, se entra en el siguiente while en el que se va actualizando el tiempo
    # hasta que se recibe un pulso en echo y entonces se pone LOW:
    while True:
        fin = time.time()
        if GPIO.input(ECHO) == GPIO.LOW:
            break
        
    t = fin-inicio
    
    # V = cm/s: 34300. Espacio recorrido es V*t, pero entre que se lanza el pulso y se detecta
    # realmente recorre dos veces la distancia, por lo que tenemos que dividir entre 2:
    distancia = (34300/2)*t
    
    return distancia
        


while True:
    distancia = calculaDistancia()
    print("Distancia del objeto: {}".format(distancia))
    time.sleep(1)    #ajustar tambien

    if distancia <= 35:  #si es menor o igual de 10 se ejecuta el otro codigo
        print('Detectado')
        subprocess.call(["python","/home/javilinzoain/Project/Detecta_final.py"])
        time.sleep(10)
        
GPIO.cleanup()          # Limpia cualquier configuración previa
root.mainloop()
