from tkinter import ttk as tk
from tkinter import *
from tkinter import messagebox
from ConsultaBD import *
from threading import Thread
from Main import*
from Consultas import *
from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import *

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

   
def main(i):
    i_host=i
    root = Tk()
    App(root)
    root.mainloop()

i_host=""



"""""  
    
    #Metodos#
    lbln= Label(vp,text="RESUMEN DE MONITOREO",bg="navy",fg="white")
    lbln.grid(column=1,row=0,sticky=(W,E))

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

    #if str(sistemaO).find("Linux") == -1:
     #   img = PhotoImage(file="win.png",master=vp)
    #else:
    img = PhotoImage(file="linux.png")
    imagenl = Label(vp, image=img)
    imagenl.grid(column=2,row=4)
    """""

