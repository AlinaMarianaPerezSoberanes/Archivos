from pysnmp.hlapi import *
import rrdtool
from ConsultaBD import *
#Nombre#

def SysDesc(agente):

    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(agente[2], mpModel=0),
           UdpTransportTarget((agente[0], agente[1])),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0')))
    )
    x = ""
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
    return resultado

#NUmero de interfaces#
def ifNumber(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(agente[2], mpModel=0),
           UdpTransportTarget((agente[0], agente[1])),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.2.1.0')))
    )
    resultado=""
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            varB =(' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
    return resultado

#Estado de interfaz#
def ifAdminStatus(num_interfaz,agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[2], mpModel=0),
            UdpTransportTarget((agente[0], agente[1])),
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
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
        return resultado
#Nombre de interfaces#
def nombre_interfaz(num_interfaz,agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[2], mpModel=0),
            UdpTransportTarget((agente[0], agente[1])),
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
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
        return resultado
#Version del SO#
def ver_System(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[2], mpModel=0),
            UdpTransportTarget((agente[0], agente[1])),
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
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            if (agente[0]=='localhost'):
                r1 = varB.split()[2]
                r2= varB.split()[4]
                r3=varB.split()[5]
            else:                
                r1=varB.split()[14]
                r2=varB.split()[15]
                r3=varB.split()[16]
            resultado=r1+r2+r3
        return resultado
#IP#

def IpAddress(agente,host):
    if host=='localhost':
        host='127.0.0.1'
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[2], mpModel=0),
            UdpTransportTarget((agente[0], agente[1])),
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
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
        return resultado

def SysUpTime(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[2], mpModel=0),
            UdpTransportTarget((agente[0], agente[1])),
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
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
        return resultado

def sysLocation(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[2], mpModel=0),
            UdpTransportTarget((agente[0], agente[1])),
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
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
        return resultado

def sysContact(agente):
    errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
            CommunityData(agente[2], mpModel=0),
            UdpTransportTarget((agente[0], agente[1])),
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
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
        return resultado



def crearRDDTOOL(filename):
    #print(filename)
    ret = rrdtool.create(filename,
                         "--start", 'N',
                         "--step", '60',
                         "DS:inoctets:COUNTER:600:U:U",
                         "DS:outoctets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:6:700",
                         "RRA:AVERAGE:0.5:1:600")

    if ret:
        print(rrdtool.error())

def infoAgente(host):
    a=[]
    puerto=ObtieneArreglo("PUERTO",host)
    com=ObtieneArreglo("COMUNIDAD",host)
    a=[host,puerto,com]
    print (a)
    return a
