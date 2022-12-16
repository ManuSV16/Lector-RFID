#Bibliotecas
import mysql.connector
import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

#Iniciar el sensor
reader = SimpleMFRC522()
#Conexión
cnx = mysql.connector.connect(user='Manuel16', password='96luam21', host = '192.168.100.73', database = 'codigoIoT')
cursor = cnx.cursor()

#Cuerpo del programa
try:
    #Leer el tag
    while True:
        print("Acerca el TAG al lector")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        insertquery = ("INSERT INTO rfid (nombre,texto,rfid) VALUES ('Manu','%s','%s');"%(text,id))
        cursor.execute(insertquery)
        cnx.commit()
        print("La operación del Query fue exitosa\n")
        
        sleep(5)
except KeyboardInterrupt:
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise
