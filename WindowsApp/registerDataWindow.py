from tkinter import *
from WindowsApp import personDataWindow as dpw
from Handlers import handlerUserDataPersistence as db
from Handlers import handlerWindowValidation as hv
from Behaviors import windowBehavior as wb

def registerDataWindow():    
    global register_window
    register_window = Toplevel()
    register_window.overrideredirect(True)
    register_window.title("Inscripción")
    register_window.geometry('800x600')

    global user_email_entry
    global user_pass_entry
    user_mail_entry = StringVar()
    user_pass_entry = StringVar()

    def handleUserRegister(email, password):
        isValidCredentialFormat = hv.validateFormatCredentials(email, password)
        if(isValidCredentialFormat['response']):
            if(db.isRegisteredUser(email)):
                wb.alertWindow("Error!", "Error Usuario Existente, intente con otro correo electrónico")
            else:            
                successfulProcess = db.saveUserCredentials(email, password)
                if successfulProcess:
                    dpw.personDataWindow(email)
                    wb.deleteWindow(register_window)
                else:
                    wb.alertWindow("Error!", "Ocurrio un problema al registrar datos... Contacte a mesa de ayuda.")
        else:
            wb.alertWindow("Error!", isValidCredentialFormat['message'])

    Label(register_window, text="").pack()
    Label(register_window, text="Formulario Inscripción", height=2, width=60, font=('Comic sens MC',14,'bold'), activebackground="aqua", bg='#1AACC1').pack()
    Label(register_window, text="").pack()

    label_user_email = Label(register_window, text="Ingrese Email", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_email.pack()
    Label(register_window, text="").pack()
    entry_user_email = Entry(register_window, textvariable = user_mail_entry)
    entry_user_email.pack()
    Label(register_window, text="").pack()
    label_user_pass = Label(register_window, text="Ingrese Password", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_pass.pack()
    Label(register_window, text="").pack()
    entry_user_pass = Entry(register_window, textvariable = user_pass_entry)
    entry_user_pass.pack()
    
    Label(register_window, text="").pack()
    Button(register_window, text="Registrarse", command= lambda: handleUserRegister(entry_user_email.get(), entry_user_pass.get()), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#3BE3B0', anchor="center").pack()
    
    Label(register_window, text="").pack()
    Button(register_window, text="Cancelar y Salir", command = lambda: wb.deleteWindow(register_window), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#E33B3B', anchor="center").pack()