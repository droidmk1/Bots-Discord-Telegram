import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

# etiqueta = tkinter.Label(ventana, text = "toma tu ventana", bg = "blue")
# etiqueta.pack(side = tkinter.BOTTOM)
# etiqueta.pack(fill = tkinter.BOTH, expand = True)

# def saludo(nombre):
#     print("Hola " + nombre)

# boton1 = tkinter.Button(ventana, text = "Presiona", command = lambda: saludo("python"))
# boton1.pack()

# cajaTexto = tkinter.Entry(ventana)
# cajaTexto.pack()

# etiqueta = tkinter.Label(ventana)
# etiqueta.pack()

# def textoDeLaCaja():
#     textocaja = cajaTexto.get()
#     etiqueta["text"] = textocaja

# boton1 = tkinter.Button(ventana, text = "click", command = textoDeLaCaja)
# boton1.pack()

boton1 = tkinter.Button(ventana, text="boton1", width=10, height=5)
boton2 = tkinter.Button(ventana, text="boton2", width=10, height=5)
boton3 = tkinter.Button(ventana, text="boton3", width=10, height=5)

boton1.grid(row=0, column=0)
boton2.grid(row=1, column=0)
boton3.grid(row=2, column=0)

ventana.mainloop()