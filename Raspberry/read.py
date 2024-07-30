#librerias
import imaplib
import os

#Variables
SERVER= 'imap.gmail.com'
USER= 'faithsoloq' #Usuario utilizado
PASS= 'caqgdhrehpivbzrq'
MAIL='faithsoloq@gmail.com'

# Conexion al server
server=imaplib.IMAP4_SSL(SERVER,993)
# Iniciar sesion
server.login(USER,PASS)
status,count= server.select('Inbox')
status,data= server.fetch(count[0],'(UID BODY[TEXT])') #Guarda la busqueda de count

# Bandera
flag = str((data[0][1]))
print(flag)


# Cerrar la conexion
server.close()
server.logout()

