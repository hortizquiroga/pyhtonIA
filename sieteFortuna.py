# Seccion para las importaciones
from tkinter import *
import random

class sieteFortuna:
    def __init__(self):
        self.crear_interfaz()
    
    def crear_interfaz(self):
        ventana = Tk()
        ventana.minsize(340,450)
        ventana.geometry('340x450')

        buton = Button(ventana, text='Jugar', font='arial 18 bold', command=self.jugar)
        buton.pack()

        foto = PhotoImage(file=r'dinero.png')
        self.gano = Label(ventana, image=foto)

        self.campos = [StringVar() for elemento in range(3)]
        incremento =10
        for campo in self.campos:
            label = Label(ventana, textvariable=campo, background='white', foreground='black', font='arial 42 bold')
            label.place(x=incremento, y=100, width=100, height=100)
            incremento+=110
        mainloop()

    def generar_aleatorio(self):
        return random.randint(0,9)

    def jugar(self):
        hay_siete= False
        for i in range(3):
            valor = self.generar_aleatorio()
            self.campos[i].set(valor)

            if(valor==7):
                hay_siete=True

            if(hay_siete):
                self.gano.pack(side=BOTTOM)
            else:
                self.gano.pack_forget()
jugar= sieteFortuna()


