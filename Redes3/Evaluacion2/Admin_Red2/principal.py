
from tkinter import ttk as tk
from tkinter import *
from tkinter import messagebox
from ConsultaBD import *
from threading import Thread
from Main import*
from Consultas import *
from PIL import Image, ImageTk

#Funcion HILO
#creacion del hilo

class MiHilo(Thread):
  def run(self):
    while True:
      startmonitoreo()


def create_table():
    tv['columns'] = (1,'puerto', 'comunidad', 'ninterfaces')
    tv.heading("#0", text='Hostname', anchor='w')
    tv.column("#0", anchor="w",width=100)
    tv.heading(1, text='Version')
    tv.column(1, anchor='center', width=100)
    tv.heading('puerto', text='Puerto')
    tv.column('puerto', anchor='center', width=100)
    tv.heading('comunidad', text='Comunidad')
    tv.column('comunidad', anchor='center')
    tv.heading('ninterfaces', text='Interfaces')
    tv.column('ninterfaces', anchor='center', width=100)
    tv.grid(row=2, column=2)

def borrarTabla():
    for i in tv.get_children():
        tv.delete(i)

def actualizarTabla():
    create_table()
    cont=contadorId()
    n=int(cont[0])
    print(n)
    ids=[]
    ids=selectidsDB()
    print(ids)
    borrarTabla()
    for i in range(n):
        a_host=selectColumDB("HOSTNAME",ids[i])
        obtenerGraficas(a_host)
        a_version=selectColumDB("VERSION",ids[i])
        a_puerto=selectColumDB("PUERTO",ids[i])
        a_com=selectColumDB("COMUNIDAD",ids[i])
        a=[a_host,a_puerto,a_com]
        a_interfaces=ifNumber(a)
        llenarTabla(i,a_host,a_version,a_puerto,a_com,a_interfaces)

def llenarTabla(n,host,version,puerto,com,ninter):
        tv.insert('', 'end', text=host, values=(version,puerto,com,ninter))

def guardarDatos():
    # Obtener datos#
    host=entrada[0].get()
    version=entrada[1].get()
    puerto = entrada[2].get()
    comunidad = entrada[3].get()
    # Obtener datos#
    print (host,version,puerto,comunidad)
    #Funcion
    registrarAgente(host,version,puerto,comunidad )

def AgregarAgente():
    ventana = Toplevel(root)
    # Graficos
    ventana.title("Agregar Agente")
    ventana.configure(background="snow")
    # Ventana principal
    va = Frame(ventana)
    va.grid(column=0, row=0, padx=(50, 50), pady=(5, 5))
    va.columnconfigure(0, weight=1)
    va.rowconfigure(0, weight=1)

    # Agregar agente
    lbll = Label(va, text="Ingrese datos del Agente", bg="dodger blue")
    lbll.grid(column=0, row=3, sticky=(W, E))
    lbl1 = Label(va, text="Host: ")
    lbl1.grid(column=0, row=4)
    entrada.append(Entry(va, width=20, textvariable=host))
    entrada[0].grid(column=1, row=4)

    lbl2 = Label(va, text="Version: ")
    lbl2.grid(column=0, row=5)
    entrada.append(Entry(va, width=20, textvariable=version))
    entrada[1].grid(column=1, row=5)

    lbl3 = Label(va, text="Puerto: ")
    lbl3.grid(column=0, row=6)
    entrada.append(Entry(va, width=20, textvariable=puerto))
    entrada[2].grid(column=1, row=6)

    lbl4 = Label(va, text="Comunidad: ")
    lbl4.grid(column=0, row=7)
    entrada.append(Entry(va, width=20, textvariable=comunidad))
    entrada[3].grid(column=1, row=7)

    btn1 = Button(va, text="Agregar Agente", command=guardarDatos)
    btn1.grid(column=2, row=5)
    


    # agregar agente

def ventana_eliminarAgente():
    eliminar = Toplevel(root)
    # Graficosprint("salio")
    eliminar.title("Eliminar Agente")
    eliminar.configure(background="snow")
    # Ventana principal
    ve = Frame(eliminar)
    ve.grid(column=0, row=0, padx=(50, 50), pady=(5, 5))
    ve.columnconfigure(0, weight=1)
    ve.rowconfigure(0, weight=1)

    # Agregar agente
    lblle = Label(ve, text="Ingrese datos del Agente", bg="dodger blue")
    lblle.grid(column=0, row=3, sticky=(W, E))
    lbl1e = Label(ve, text="Host: ")
    lbl1e.grid(column=0, row=4)
    entradae.append(Entry(ve, width=20, textvariable=hoste))
    entradae[0].grid(column=1, row=4)

    btn1 = Button(ve, text="Eliminar", command=eliminarAgentef)
    btn1.grid(column=2, row=5)

def eliminarAgentef():
    hoste = entradae[0].get()
    print("Agente "+hoste+" eliminado")
    #Funcion eliminar agente
    eliminarAgente(hoste)


def ventana_informacion():
    reporte = Toplevel(root)
    # Graficos
    reporte.title("Informacion General")
    reporte.configure(background="snow")
    vr = Frame(reporte)
    vr.grid(column=0, row=0, padx=(50, 50), pady=(5, 5))
    vr.columnconfigure(0, weight=1)
    vr.rowconfigure(0, weight=1)

    lblle = Label(vr, text="Ingrese datos del Agente", bg="dodger blue")
    lblle.grid(column=0, row=3, sticky=(W, E))
    lbl1e = Label(vr, text="Host: ")
    lbl1e.grid(column=0, row=4)
    entradai.append(Entry(vr, width=20, textvariable=i))
    entradai[0].grid(column=1, row=4)

    btn1 = Button(vr, text="Seleccionar", command=informacion)
    btn1.grid(column=2, row=5)

def informacion():
    i = entradai[0].get()
    print(i)
    inf = Toplevel(root)
    tvr = tk.Treeview(inf)
    venatana_reporte(tvr)
    LoadTable(i,tvr)
    i = 'linux.png'
    root_pic1 = Image.open(i)                           # Open the image like this first
    img = ImageTk.PhotoImage(root_pic1)   
    imagenl = Label(inf, image=img)
    imagenl.grid(column=0,row=3)
    
    
def venatana_reporte(tvr):
        
        tvr['columns'] = (1,2,3,4,5,6,7,8,9)

        tvr.heading("#0", text='Dispositivo', anchor='center')
        tvr.column("#0", anchor='w')

        tvr.heading(1, text='Conexion')
        tvr.column(1, anchor='center', width=80)

        tvr.heading(2, text='Interfaces')
        tvr.column(2, anchor='center', width=80)

        tvr.heading(3, text='Edo Interfaces')
        tvr.column(3, anchor='w')

        tvr.heading(4, text='Sistema')
        tvr.column(4, anchor='w',width=80)
        
        tvr.heading(5, text='IP')
        tvr.column(5, anchor='w')

        tvr.heading(6, text='Tiempo')
        tvr.column(6, anchor='w',width=100)

        tvr.heading(7, text='Ubicacion')
        tvr.column(7, anchor='w')

        tvr.heading(8, text='Contacto')
        tvr.column(8, anchor='w')
        tvr.grid(row=0, column=0)
   
   
def LoadTable(i_host,tvr):
        agente=infoAgente(i_host)
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
        ip=IpAddress(agente,agente[0])
        time=SysUpTime(agente)
        ub=sysLocation(agente)
        contacto=sysContact(agente)

        if str(sistemaO).find("Linux") == -1:
            i = 'win.png'
        else:
            i = 'linux.png'
        tvr.insert('', 'end',text=nombre, values=(stat_nom,num_interfaces,nom_interfaces,sistemaO,ip,time,ub,contacto))
        root_pic1 = Image.open(i)                           # Open the image like this first
        img = ImageTk.PhotoImage(root_pic1)      # Then with PhotoImage. NOTE: self.root_pic2 =     and not     root_pic2 =
        tvr.insert('', 'end', text="", open=True, image=img)



#Variables
host=""
version=""
puerto=""
comunidad=""
entrada=[]
entradae=[]
hoste=""
entradar=[]
r=""
entradai=[]
i=""


root = Tk()
root.title("Bienvenido al administrador de Red")
root.geometry('1100x330')

nb = tk.Notebook(root, name='nb')
nb.pack(fill=BOTH, expand='yes',padx=5,pady=5)

master_agentes = Frame(nb, name='master-agentes',bg='gray85')
tv = tk.Treeview(master_agentes)
tv.pack(fill=BOTH, padx=20,pady=(20,0))

create_table()
btn1= Button(master_agentes,text="Agregar Agente",command=AgregarAgente,bg='springgreen2')
btn1.grid(column=0,row=0)
btn2= Button(master_agentes,text="Eliminar Agente", command=ventana_eliminarAgente,bg='orangered2')
btn2.grid(column=0,row=1)
btn4= Button(master_agentes,text="Actualizar tabla",command=actualizarTabla,bg='dodgerblue')
btn4.grid(column=1,row=0)
btn5= Button(master_agentes,text="Ver Informacion",command=ventana_informacion,bg='azure3')
btn5.grid(column=2,row=0)


img = PhotoImage(file="img.png",master=master_agentes)
imagenl = Label(master_agentes, image=img)
imagenl.grid(column=0,row=2)


nb.add(master_agentes, text='Agentes')

#El hilo que monitoriza todos lo agentes que estan registrados en la base de datos
hilo = MiHilo()
hilo.start()

root.mainloop()