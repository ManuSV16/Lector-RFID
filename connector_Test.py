#Bibliotecas
import mysql.connector

#Programa
print("Conectandose a la base de datos")
cnx = mysql.connector.connect(user='Manuel16', password='96luam21', host = '192.168.100.73 ', database = 'codigoIoT') 
print("Conexión realizada")
print(cnx)

print("Cerrar conexión")
cnx.close()
print("Conexión cerrada")
