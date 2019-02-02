import mysql.connector

#La base de datos se llama agentes. En el archivo databaseAgentes.txt se encuentra el scrip
#coneccion con la base de datos
"""""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="Agentes"
)
"""""

""""" Contenido de la tabla
ID INT,
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
def insertDB(hostname,version,puerto,comunidad,FILEUDPrrd,FILEUDPxml,FILETCPrrd,FILETCPxml,FILESNMPrrd,FILESNMPxml,FILEIPrrd,FILEIPxml,FILEICMPrrd,FILEICMPxml,pathimage):
    mydbx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Agentes"
    )
    mycursor = mydbx.cursor()
    sql = "INSERT INTO agente (HOSTNAME,VERSION,PUERTO,COMUNIDAD,FILEUDPrrd,FILEUDPxml,FILETCPrrd,FILETCPxml,FILESNMPrrd,FILESNMPxml,FILEIPrrd,FILEIPxml,FILEICMPrrd,FILEICMPxml,PATHIMAGE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (hostname,version,puerto,comunidad,FILEUDPrrd,FILEUDPxml,FILETCPrrd,FILETCPxml,FILESNMPrrd,FILESNMPxml,FILEIPrrd,FILEIPxml,FILEICMPrrd,FILEICMPxml,pathimage)
    mycursor.execute(sql, val)

    mydbx.commit()


def selectDB():
    mydbx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Agentes"
    )
    mycursor = mydbx.cursor()
    mycursor.execute("SELECT * FROM agente")
    myresult = mycursor.fetchall()
    return myresult

def selectidsDB():
    mydbx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Agentes"
    )
    mycursor = mydbx.cursor()
    mycursor.execute("SELECT id FROM agente")
    myresult = mycursor.fetchall()
    result = []
    for x in range(len(myresult)):
        result.append(myresult[x][0])
    return result

def contadorId():
    mydbx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Agentes"
    )
    mycursor = mydbx.cursor()
    mycursor.execute("SELECT COUNT(ID) FROM agente")
    myresult = mycursor.fetchall()
    result = []
    for x in range(len(myresult)):
        result.append(myresult[x][0])
    return result

def selectColumDB(colum,id):
    mydbx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Agentes"
    )
    mycursor = mydbx.cursor()
    sql="SELECT "+colum+" FROM agente WHERE id="+str(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return (myresult[0][0])

def selectColumDBwhere(colum,where,val):
    mydbx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Agentes"
    )
    mycursor = mydbx.cursor()
    sql="SELECT "+colum+" FROM agente WHERE "+ where+"="+val
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def deleterow(id):
    mydbx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Agentes"
    )
    mycursor = mydbx.cursor(id)
    sql = "DELETE FROM agente WHERE id = "+str(id)
    mycursor.execute(sql)
    mydbx.commit()

def ObtieneArreglo(colum,host):
    mydbx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="Agentes"
    )
    mycursor = mydbx.cursor()
    sql="SELECT "+colum+" FROM agente WHERE HOSTNAME='"+str(host)+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return (myresult[0][0])



