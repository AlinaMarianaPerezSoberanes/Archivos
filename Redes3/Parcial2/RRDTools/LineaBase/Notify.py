import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Ruta de archivos a enviar
rrdpath = '/home/alina/Documentos/Redes3/Parcial2/Adquisicion/'
pngpath = '/home/alina/Documentos/Redes3/Parcial2/Adquisicion/'
fname = 'net3.rrd'                                                  #BD a consultar
width = '500'
height = '200'
mailsender = "dummycuenta3@gmail.com"                               #email del cual se enva el correo
mailreceip = "amarianaps95@gmail.com"                               #email al que se envia
mailserver = 'smtp.gmail.com: 587'                                  #servidor gmail
password = 'Secreto123'                                             #contrasea

def send_alert_attached(subject):
    """ Will send e-mail, attaching png
    files in the flist.
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(pngpath+'Lbase.png', 'rb')                            #Carga la imagen de la ruta anterior
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    mserver = smtplib.SMTP(mailserver)
    mserver.starttls()
    # Login Credentials for sending the mail
    mserver.login(mailsender, password)

    mserver.sendmail(mailsender, mailreceip, msg.as_string())
    mserver.quit()



