#Bibliotecas
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='Manuel16', password='96luam21', host = '127.0.0.1', database = 'codigoIoT')
cursor = cnx.cursor()

query = ("SELECT * FROM rfid WHERE id=17;")
cursor.execute(query)

res = cursor.fetchall()

for x in res:
    print (x)

cnx.close
