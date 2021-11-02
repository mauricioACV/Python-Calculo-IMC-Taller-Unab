from tkinter import *
from WindowsApp import imcDataWindow as idw
from WindowsApp import ImcReportWindow as irw
from Behaviors import windowBehavior as wb  

def appUserOptionsWindow(userEmail, userGender):    
    global app_user_options_window
    app_user_options_window = Toplevel()
    app_user_options_window.title("Menú Aplicación IMC")
    app_user_options_window.geometry('800x600')

    Label(app_user_options_window, text="Seleccione una Opción", height=2, width=60, font=('Comic sens MC',14,'bold'), relief="raised", activebackground="aqua", bg='#1AACC1').pack()
    Label(app_user_options_window, text="").pack()

    Button(app_user_options_window, text="Calcular y Registrar IMC", command= lambda: idw.imcDataWindow(userEmail, userGender), borderwidth=2, height=2, width=35, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#999AB8', anchor="center").pack()
    Label(app_user_options_window, text="").pack()

    Button(app_user_options_window, text="Ver Historial IMC", command= lambda: irw.imcReportWindow(userEmail, userGender, ""), borderwidth=2, height=2, width=35, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#999AB8', anchor="center").pack()
    Label(app_user_options_window, text="").pack()

    Button(app_user_options_window, text="Cancelar y Salir", command= lambda: wb.deleteWindow(app_user_options_window), borderwidth=2, height=2, width=35, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#E33B3B', anchor="center").pack()
    Label(app_user_options_window, text="").pack()