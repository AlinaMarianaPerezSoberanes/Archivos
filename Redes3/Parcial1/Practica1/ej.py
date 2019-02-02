import Tkinter

# Primer ventana con valores positivos
primer_ventana = Tkinter.Tk()
primer_ventana.geometry("300x300+0+0")
# A modo estetico le di un titulo
primer_ventana.title("Posicion x=+0 y=+0")
# Este tambien es estetico y no influye en el uso del metodo
etiqueta = Tkinter.Label(primer_ventana, text="Posicion x=+0 y=+0", width=100, height=100, anchor="center")
etiqueta.pack()

# Segunda ventana con valores negativos
segunda_ventana = Tkinter.Tk()
segunda_ventana.geometry("300x300-0-0")
segunda_ventana.title("Posicion x=-0 y=-0")
etiqueta = Tkinter.Label(segunda_ventana, text="Posicion x=-0 y=-0", width=100, height=100, anchor="center")
etiqueta.pack()

primer_ventana.mainloop()
segunda_ventana.mainloop()