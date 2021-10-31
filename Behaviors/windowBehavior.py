from tkinter import *

def alertWindow(title, message):
    global alert_window
    alert_window = Toplevel()
    alert_window.title(title)
    alert_window.geometry('350x200')
    
    Label(alert_window, text="").pack()
    Label(alert_window, text=message).pack()
    Label(alert_window, text="").pack()
    Button(alert_window, text="Aceptar", command= lambda: deleteWindow(alert_window)).pack()

def deleteWindow(window):
    window.destroy()


def successWindow(title, message, backWindow):
    global success_window
    success_window = Toplevel()
    success_window.title(title)
    success_window.geometry('350x200')
    
    Label(success_window, text="").pack()
    Label(success_window, text=message).pack()
    Label(success_window, text="").pack()
    Button(success_window, text="Aceptar", command= lambda: closeSuccessWindow(success_window, backWindow)).pack()

def closeSuccessWindow(thisWindow, backWindow):
    thisWindow.destroy()
    backWindow.destroy()