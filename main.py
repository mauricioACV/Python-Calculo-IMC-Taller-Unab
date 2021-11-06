from tkinter import *
from WindowsApp import registerDataWindow as rw
from WindowsApp import loginWindow as lw
from Behaviors import windowBehavior as wb    
# *************************************************************************************************
# ***************************************** Main App **********************************************
# *************************************************************************************************

def mainWindow():
    global principal_window
    principal_window = Tk()
    principal_window.overrideredirect(True)
    principal_window.title("Calculadora IMC")
    principal_window.geometry('800x600')
    principal_window.resizable(0,0)

    Label(text="").pack()
    Label(text="").pack()
    Label(text="CALCULADORA ÍNDICE MASA CORPORAL", height=2, width=60, font=('Comic sens MC',14,'bold'), relief="raised", activebackground="aqua", bg='#1AACC1').pack()
    
    Label(text="").pack()
    Button(text="Registrate antes de utilizar la app", command = rw.registerDataWindow, borderwidth=2, height=2, width=35, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#999AB8', anchor="center").pack()
    
    Label(text="").pack()
    Button(text="Inicia Sesión si ya eres usuario registrado", command = lw.loginWindow, borderwidth=2, height=2, width=35, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#999AB8', anchor="center").pack()
    
    Label(text="").pack()
    Button(text="Salir de la App", command = lambda: wb.deleteWindow(principal_window), borderwidth=2, height=2, width=35, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#E33B3B', anchor="center").pack()

    principal_window.mainloop()

mainWindow()