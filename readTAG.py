#Bibliotecas
import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

#Iniciar el sensor
reader = SimpleMFRC522()

#Cuerpo del programa
try:
    #Leer el tag
    while True:
        print("Coloque el tag cerca del lector")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
