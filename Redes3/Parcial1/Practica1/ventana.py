import sys
from Tkinter import * 
from pysnmp.hlapi import *

#Nombre#
def SysDesc(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(agente[3], mpModel=0),
           UdpTransportTarget((agente[1], agente[2])),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0')))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
    return x

#NUmero de interfaces#
def ifNumber(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(agente[3], mpModel=0),
           UdpTransportTarget((agente[1], agente[2])),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.2.1.0')))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
    return x
#Estado de interfaz#
def ifAdminStatus(num_interfaz,agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[3], mpModel=0),
            UdpTransportTarget((agente[1], agente[2])),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.'+str(num_interfaz))))
    )

    if errorIndication:
            print(errorIndication)
    elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))
        return x
#Nombre de interfaces#
def nombre_interfaz(num_interfaz,agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[3], mpModel=0),
            UdpTransportTarget((agente[1], agente[2])),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.'+str(num_interfaz))))
    )

    if errorIndication:
            print(errorIndication)
    elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))
        return x
#Version del SO#
def ver_System(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[3], mpModel=0),
            UdpTransportTarget((agente[1], agente[2])),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))
    )

    if errorIndication:
            print(errorIndication)
    elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))
        return x
#IP#

def IpAddress(agente,host):
    if host=='localhost':
        host='127.0.0.1'
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[3], mpModel=0),
            UdpTransportTarget((agente[1], agente[2])),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.4.20.1.1.'+str(host))))
    )

    if errorIndication:
            print(errorIndication)
    elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))
        return varBind

def SysUpTime(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[3], mpModel=0),
            UdpTransportTarget((agente[1], agente[2])),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')))
    )

    if errorIndication:
            print(errorIndication)
    elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))
        return x

def sysLocation(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[3], mpModel=0),
            UdpTransportTarget((agente[1], agente[2])),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')))
    )

    if errorIndication:
            print(errorIndication)
    elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))
        return x

def sysContact(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[3], mpModel=0),
            UdpTransportTarget((agente[1], agente[2])),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0')))
    )

    if errorIndication:
            print(errorIndication)
    elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))
        return x

        
def monitoreo(agente,host,num_agente):
    #Metodos#
    nombre=SysDesc(agente)
    stat_nom=""
    if nombre!="":
        stat_nom="up"
    else:
        stat_nom="down"

    num_interfaces=ifNumber(agente)
    interfaces=[]
    nom_interfaces=[]
    for i in range(1,int(num_interfaces)+1):
        stat_i=ifAdminStatus(i,agente)
        if stat_i==1:
            stat_i="up"
        if stat_i==2:
            stat_i="down"
        if stat_i==3:
            stat_i="testing"
        nom_i=nombre_interfaz(i,agente)
        interfaces.append(stat_i)
        nom_interfaces.append(str(nom_i))

    sistemaO=ver_System(agente)
    ip=IpAddress(agente,host)
    time=SysUpTime(agente)
    ub=sysLocation(agente)
    contacto=sysContact(agente)
    #Metodos#

    #Verficar#
    print nombre, num_interfaces, interfaces, nom_interfaces, ip, time,ub,contacto
    #Verificar#

    #Ventana principal#
    principal= Tk() #Nombre interfaz
    #Graficos
    principal.title("Practica 1- Admisnitracion de Servicios en Red")
    principal.configure(background="snow")
        #Ventana principal
    vp=Frame(principal)
    vp.grid(column=0,row=0,padx=(50,50), pady=(5,5))
    vp.columnconfigure(0,weight=1)
    vp.rowconfigure(0,weight=1)
    lbln= Label(vp,text="RESUMEN DE MONITOREO",bg="navy",fg="white")
    lbln.grid(column=1,row=0,sticky=(W,E))

    lbln1= Label(vp,text="Dispositivos monitorizados: ")
    lbln1.grid(column=0,row=2)
    lbln2= Label(vp,text=str(len(num_agente)))
    lbln2.grid(column=1,row=2)

    lbln9= Label(vp,text="Dispositivo: ")
    lbln9.grid(column=0,row=4)
    lbln10= Label(vp,text=nombre)
    lbln10.grid(column=1,row=4)

    lbln3= Label(vp,text="Estado de conexion: ")
    lbln3.grid(column=0,row=5)
    lbln4= Label(vp,text=stat_nom)
    lbln4.grid(column=1,row=5)

    lbln5= Label(vp,text="Interfaces de red: ")
    lbln5.grid(column=0,row=6)
    lbln6= Label(vp,text=num_interfaces)
    lbln6.grid(column=1,row=6)
    
    lbln7= Label(vp,text="Estado de interfaz: ")
    lbln7.grid(column=0,row=7)
    cadena=[]
    for i in range(0,int(num_interfaces)):
        cadena.append(str(nom_interfaces[i])+' - '+str(interfaces[i]+'\n'))
    print cadena 

    lbln8=Label(vp,text=cadena)
    lbln8.grid(column=1,row=7)

    lbln11=Label(vp,text="Sistema Operativo: ")
    lbln11.grid(column=0,row=8)
    lbln12=Label(vp,text=sistemaO)
    lbln12.grid(column=1,row=8)

    lbln13=Label(vp,text="IpAddress: ")
    lbln13.grid(column=0,row=9)
    lbln14=Label(vp,text=ip)
    lbln14.grid(column=1,row=9)

    lbln15=Label(vp,text="Tiempo de Actividad: ")
    lbln15.grid(column=0,row=10)
    lbln16=Label(vp,text=time)
    lbln16.grid(column=1,row=10)

    lbln17=Label(vp,text="Ubicacion Fisica: ")
    lbln17.grid(column=0,row=11)
    lbln18=Label(vp,text=ub)
    lbln18.grid(column=1,row=11)

    lbln19=Label(vp,text="Contacto: ")
    lbln19.grid(column=0,row=12)
    lbln20=Label(vp,text=contacto)
    lbln20.grid(column=1,row=12)

    
    if str(sistemaO).find("Ubuntu") == -1:
        img = PhotoImage(file="win.png",master=vp)
    else:
        img = PhotoImage(file="linux.png",master=vp)
    lbln21=Label(vp,text="Logo: ")
    lbln21.grid(column=0,row=13)
    imagenl = Label(vp, image=img)
    imagenl.grid(column=1,row=13)

    principal.mainloop()
    #Ventana principal#

 #VENTANA2# 



def agregarAgente():
    #Obtener datos#
    host=ent_host.get()
    puerto_s=ent_puerto.get()
    comunidad=ent_com.get()
    cont_agente=ent_cont.get()
    puerto=int(puerto_s)
    num=int(cont_agente)
    agente=[num,host,puerto,comunidad]
    num_agente.append(cont_agente)
    #Obtener datos#
    monitoreo(agente,host,num_agente)
    
    




#VENTANA1#

agente=[]
host="" 
puerto_s=""
comunidad=""
cont_agente=""
nombre=""
puerto=0
num_agente=[]




ventana= Tk() #Nombre interfaz
 #Graficos
ventana.title("Practica 1- Admisnitracion de Servicios en Red")
ventana.configure(background="snow")
    #Ventana principal
va=Frame(ventana)
va.grid(column=0,row=0,padx=(50,50), pady=(5,5))
va.columnconfigure(0,weight=1)
va.rowconfigure(0,weight=1)
#Ventana princial

#Agregar agente
lbll= Label(va,text="Ingrese datos del Agente",bg="dodger blue")
lbll.grid(column=0,row=3,sticky=(W,E))
lbl1=Label(va,text="Host: ")
lbl1= Label(va,text="Host: ")
lbl1.grid(column=0,row=4)
ent_host=Entry(va,width=20,textvariable=host)
ent_host.grid(column=1,row=4)


lbl2= Label(va,text="Puerto: ")
lbl2.grid(column=0,row=5)
ent_puerto=Entry(va,width=20,textvariable=puerto_s)
ent_puerto.grid(column=1,row=5)
    
lbl3= Label(va,text="Comunidad: ")
lbl3.grid(column=0,row=6)
ent_com=Entry(va,width=20,textvariable=comunidad)
ent_com.grid(column=1,row=6)

lbl4= Label(va,text="Numero: ")
lbl4.grid(column=0,row=7)
ent_cont=Entry(va,width=20,textvariable=cont_agente)
ent_cont.grid(column=1,row=7)
    
btn1= Button(va,text="Agregar Agente", command=agregarAgente)
btn1.grid(column=2,row=5)

#Agregar agente

ventana.mainloop()