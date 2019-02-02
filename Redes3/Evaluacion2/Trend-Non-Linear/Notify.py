import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Ruta de archivos a enviar
rrdpath = '/home/alina/Escritorio/Trend-Non-Linear/'
pngpath = '/home/alina/Escritorio/Trend-Non-Linear/'
fname = 'net3.rrd'                                                  #BD a consultar
width = '500'
height = '200'
mailsender = "dummycuenta3@gmail.com"                               #email del cual se envia el correo
mailreceip = "amarianaps5@gmail.com"                               #email al que se envia
mailserver = 'smtp.gmail.com: 587'                                  #servidor gmail
password = 'Secreto123'                                             #contrasena

def send_alert_attached(subject):
    """ Will send e-mail, attaching png
    files in the flist.
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(pngpath+'netPalphaBajoFallas1.png', 'rb')                            #Carga la imagen de la ruta anterior
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    mserver = smtplib.SMTP(mailserver)
    mserver.starttls()
    # Login Credentials for sending the mail
    mserver.login(mailsender, password)

    mserver.sendmail(mailsender, mailreceip, msg.as_string())
    mserver.quit()



