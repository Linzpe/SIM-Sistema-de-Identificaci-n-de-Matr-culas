#!/bin/bash
# Code executed on Raspberry Pi 4B
# Tomar una foto con la cámara de la Raspberry
#libcamera-still --width 9150 --height 6944 --output captura.jpg -n -t 1
libcamera-still --width 1200 --height 800 --output /home/javilinzoain/Project/Fotos_matriculas/captura_nueva.jpg -n -t 1
#libcamera-still --output captura-jpg

# Enviar un mensaje al script de Python para indicar que se ha realizado la captura
echo "Captura realizada"
