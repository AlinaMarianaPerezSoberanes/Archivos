from ftplib import FTP 
 
ftp = FTP() 
ftp.connect('192.168.202.15', 21, -999) 
ftp.login('rcp', 'rcp') 
print ftp.getwelcome() 
print ftp.pwd() 
ftp.dir()
#GET 
archivo = ftp.retrlines('RETR startup-config') 
print archivo 

#PUT
ftp.storlines('STOR R2-startup-config', open('/home/alina/ospf-R1.startup-config.txt', 'rb'))

ftp.close()/