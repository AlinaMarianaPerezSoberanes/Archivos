
from ConsultaBD import *
from threading import Thread
from Consultas import*
import os
from ConsultasOIDS  import *
from GraficarOIDS  import *


""""" Contenido de la tabla

create table agente(
ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
HOSTNAME VARCHAR(30),
VERSION INT,
PUERTO INT,
COMUNIDAD VARCHAR(30),
FILEUDPrrd VARCHAR(200),
FILEUDPxml VARCHAR(200),
FILETCPrrd VARCHAR(200),
FILETCPxml VARCHAR(200),
FILESNMPrrd VARCHAR(200),
FILESNMPxml VARCHAR(200),
FILEIPrrd VARCHAR(200),
FILEIPxml VARCHAR(200),
FILEICMPrrd VARCHAR(200),
FILEICMPxml VARCHAR(200),
PATHIMAGE VARCHAR(200));
"""""

"""""

#Obtener IDS de los agentes guardados en la base de datos
agentesID=selectidsDB()
#Por cada agente obtener host, puerto, comunidad
for ID in range(len(agentesID)):
  hostame=selectColumDB("HOSTNAME", str(agentesID[ID]))
  puerto = selectColumDB("PUERTO", str(agentesID[ID]))
  comunidad = selectColumDB("COMUNIDAD", str(agentesID[ID]))
  agente=[hostame,puerto,comunidad]
  print(agente)
  print(SysDesc(agente))
  InterfaceDisponible=int(ifNumber(agente))
  interfaces = []
  nom_interfaces = []
  for i in range(1, int( InterfaceDisponible) + 1):
    stat_i = ifAdminStatus(i, agente)
    if stat_i == 1:
      stat_i = "up"
    if stat_i == 2:
      stat_i = "down"
    if stat_i == 3:
      stat_i = "testing"
    nom_i = nombre_interfaz(i, agente)
    interfaces.append(stat_i)
    nom_interfaces.append(str(nom_i))

  print(ver_System(agente))
  print(SysUpTime(agente))
  print(sysLocation(agente))
  print(sysContact(agente))
"""""


#Informacion general por agente
#def infoAgente():






#Por cada agente en la base de datos consulta los 5 objetos de la MIB, guarda los datos en sus respectivos rrd y xml

def startmonitoreo():
  agentesID = selectidsDB()
  for ID in range(len(agentesID)):
    getUDP(selectColumDB("COMUNIDAD", str(agentesID[ID])),selectColumDB("HOSTNAME", str(agentesID[ID])), selectColumDB("FILEUDPrrd", str(agentesID[ID])), selectColumDB("FILEUDPxml", str(agentesID[ID])))
    getTCP(selectColumDB("COMUNIDAD", str(agentesID[ID])), selectColumDB("HOSTNAME", str(agentesID[ID])), selectColumDB("FILETCPrrd", str(agentesID[ID])), selectColumDB("FILETCPxml", str(agentesID[ID])))
    getSNMP(selectColumDB("COMUNIDAD", str(agentesID[ID])), selectColumDB("HOSTNAME", str(agentesID[ID])), selectColumDB("FILESNMPrrd", str(agentesID[ID])),selectColumDB("FILESNMPxml", str(agentesID[ID])))
    getIP(selectColumDB("COMUNIDAD", str(agentesID[ID])), selectColumDB("HOSTNAME", str(agentesID[ID])), selectColumDB("FILEIPrrd", str(agentesID[ID])), selectColumDB("FILEIPxml", str(agentesID[ID])))
    getICMP(selectColumDB("COMUNIDAD", str(agentesID[ID])), selectColumDB("HOSTNAME", str(agentesID[ID])), selectColumDB("FILEICMPrrd", str(agentesID[ID])), selectColumDB("FILEICMPxml", str(agentesID[ID])))

#obtiene las graficas del agente
def obtenerGraficas(agente):
  hostname="'"+agente+"'"
  IDagente=selectColumDBwhere("id", "HOSTNAME", hostname)

  PATHIMAGE=selectColumDB("PATHIMAGE",str(IDagente))

  FILETCPrrd=selectColumDB("FILETCPrrd",str(IDagente))
  graficaOIDget(PATHIMAGE, "TCP", FILETCPrrd)

  FILEUDPrrd = selectColumDB("FILEUDPrrd", IDagente)
  graficaOIDget(PATHIMAGE, "UDP", FILEUDPrrd)

  FILESNMPrrd = selectColumDB("FILESNMPrrd", IDagente)
  graficaOIDget(PATHIMAGE, "SNMP", FILESNMPrrd)

  FILEIPrrd = selectColumDB("FILEIPrrd", IDagente)
  graficaOIDget(PATHIMAGE, "IP", FILEIPrrd)

  FILEICMPrrd = selectColumDB("FILEICMPrrd", IDagente)
  graficaOIDget(PATHIMAGE, "ICMP", FILEICMPrrd)

#Registra en la base de datos un nuevo agente y crea los archivos RDD por cada OID
def registrarAgente(hostname,version,puerto,comunidad ):
  f1 = open('/etc/snmp/snmpd.conf', 'a')
  f1.write('\nrwcommunity' + '\t' + comunidad)
  f1.close()

  agentesID = selectidsDB()
  id=str(agentesID[len(agentesID)-1]+1)
  #id=str(1)
  os.mkdir(id)
  FILEUDPrrd = "./"+id+"/UDP.rrd"
  FILEUDPxml = "./"+id+"/UDP.xml"
  crearRDDTOOL(FILEUDPrrd)

  FILETCPrrd = "./"+id+"/TCP.rrd"
  FILETCPxml = "./"+id+"/TCP.xml"
  crearRDDTOOL(FILETCPrrd)

  FILESNMPrrd = "./"+id+"/SNMP.rrd"
  FILESNMPxml = "./"+id+"/SNMP.xml"
  crearRDDTOOL(FILESNMPrrd)

  FILEIPrrd = "./"+id+"/IP.rrd"
  FILEIPxml = "./"+id+"/IP.xml"
  crearRDDTOOL(FILEIPrrd)

  FILEICMPrrd = "./"+id+"/ICMP.rrd"
  FILEICMPxml = "./"+id+"/ICMP.xml"
  crearRDDTOOL(FILEICMPrrd)

  pathimage = "./"+id+"/image/"
  os.mkdir("./"+id+"/image/")
  insertDB(hostname, version, puerto, comunidad, FILEUDPrrd, FILEUDPxml, FILETCPrrd, FILETCPxml, FILESNMPrrd,
           FILESNMPxml, FILEIPrrd, FILEIPxml, FILEICMPrrd,FILEICMPxml,pathimage)



def eliminarAgente(agente):
  hostname = "'" + agente + "'"
  IDagente = selectColumDBwhere("id", "HOSTNAME", hostname)
  deleterow(IDagente)



