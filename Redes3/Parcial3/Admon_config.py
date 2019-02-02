#Modulo de configuracion automatica
import getpass
import sys
import telnetlib
from ftplib import FTP 
#from cliente_http import *


def extraer():
    host = raw_input("Router: ")                        
    #extraer archivo GET
    ftp = FTP() 
    ftp.connect(host) 
    ftp.login(user, password) 
    print (ftp.getwelcome())
    print (ftp.pwd()) 
    ftp.dir()
    #GET 

    #archivo = open("startup-config-"+str(host)+".txt", "w")
    #ftp.retrlines('RETR startup-config') 
    ftp.retrbinary('RETR startup-config', open('startup-config-'+str(host)+'.txt', 'wb').write)
    #print(lines)
    #print contenido 
    #archivo.close
    print ("Archivo descargado como: startup-config-"+str(host)+".txt ....")
    tn.close()
    ftp.close()



def importar():
    #PUT
    host = raw_input("Router: ")                        #ip de host
    path = raw_input("Archivo origen /ruta/archivo: ")         #Archivo
    path_d = raw_input("Archivo destino: ")         #Archivo
    #Conexion telnet
    print ("Conectando al router via Telnet...")
    tn = telnetlib.Telnet(host,23)
    tn.read_until("User: ")
    tn.write(user + "\n")
    tn.read_until("Password: ")
    tn.write(password + "\n")
    tn.write("ena\n")
    tn.write("config\n")
    tn.write("service ftp\n")
    tn.write("service tftp\n")
    tn.write("exit\n")
    tn.write("exit\n")
    print ("Consola...")
    print (tn.read_all())
    print ("Se actualizo el archivo -startup-config- en la carpeta tftpboot")
    #extraer archivo GET
    #extraer archivo GET
    ftp = FTP() 
    ftp.connect(host) 
    ftp.login(user, password) 
    print (ftp.getwelcome())
    print (ftp.pwd())
    ftp.storbinary('STOR '+str(path_d), open(str(path), 'rb'))
    ftp.dir()
    ftp.close()
    tn.close()


def mover():
    host_o = raw_input("Router origen: ")
    host_d = raw_input("Router destino: ")
    archivo_o= raw_input("Archivo origen: ")
    archivo_d= raw_input("Archivo destino: ")

    print ("Conectando al router via Telnet...")
    tn = telnetlib.Telnet(host_o,23)
    tn.read_until("User: ")
    tn.write(user + "\n")
    tn.read_until("Password: ")
    tn.write(password + "\n")
    tn.write("ena\n")
    tn.write("config\n")
    tn.write("service ftp\n")
    tn.write("service tftp\n")
    tn.write("copy "+str(archivo_o)+" ftp://rcp:rcp@"+str(host_d)+"/"+str(archivo_d)+"\n")
    tn.write("exit\n")
    tn.write("exit\n")
    print ("Consola...")
    print (tn.read_all())
    tn.close()


#Credenciales
user = "rcp"
password = "rcp"

#Menu de opciones
print ("  .:: Sistema de administracion de Red GNS3 ::.\n ")
print ("1. Extraer la configuracion ")
print ("2. Importar la configuracion desde un archivo ")
print ("3. Mover archivos de configuracion entre dispositivos")
print ("4. Sensor HTTP")
print ("5. Sensor SMTP")
print ("6. Sensor FTP")
print ("7. Sensor impresion")
print ("0. Salir")
opcion=int (raw_input("\n\nOpcion: "))

while (opcion !=0):
        if (opcion == 1):
            print("opcion: ",opcion)
            extraer()

        if (opcion == 2):
            print("opcion: ",opcion)
            importar()

        if (opcion == 3):
            print("opcion: ",opcion)
            mover()
        if (opcion == 4):
            print("opcion: ",opcion)
            #main()            
        
        print (" \n\n\n .:: Sistema de administracion de Red GNS3 ::.\n ")
        print ("1. Extraer la configuracion ")
        print ("2. Importar la configuracion desde un archivo ")
        print ("3. Mover archivos de configuracion entre dispositivos")
        print ("4. Sensor HTTP")
        print ("5. Sensor SMTP")
        print ("6. Sensor FTP")
        print ("7. Sensor impresion")
        print ("0. Salir")
        opcion=int (raw_input("\n\nOpcion: "))
