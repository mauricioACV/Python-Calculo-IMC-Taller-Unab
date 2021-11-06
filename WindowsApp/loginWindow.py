from tkinter import *
from WindowsApp import appUserOptionsWindow as uow
from Handlers import handlerUserDataPersistence as db
from Handlers import handlerWindowValidation as hv
from Behaviors import windowBehavior as wb

def loginWindow():    
    global login_window
    login_window = Toplevel()
    login_window.overrideredirect(True)
    login_window.title("Inicio de Sesión")
    login_window.geometry('800x600')

    global user_email_entry
    global user_pass_entry
    user_mail_entry = StringVar()
    user_pass_entry = StringVar()

    def handleUserLogin(userEmail, password):
        isValidCredentialFormat = hv.validateFormatCredentials(userEmail, password)
        if(isValidCredentialFormat['response']):
            if(db.isRegisteredUser(userEmail)):
                dbUserPass = db.getUserPassword(userEmail)
                if dbUserPass == password:
                    dbUserGender = db.getUserGender(userEmail)
                    uow.appUserOptionsWindow(userEmail, dbUserGender)
                    wb.deleteWindow(login_window)
                else:
                    wb.alertWindow("Error!", "Error, Contraseña Incorrecta")
            else:
                wb.alertWindow("Error!", "Error, Usuario no registrado")                
        else:
            wb.alertWindow("Error!", isValidCredentialFormat['message'])
    
    Label(login_window, text="").pack()
    Label(login_window, text="Iniciar Sesión", height=2, width=60, font=('Comic sens MC',14,'bold'), activebackground="aqua", bg='#1AACC1').pack()
    Label(login_window, text="").pack()

    label_user_email = Label(login_window, text="Ingrese Email", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_email.pack()
    Label(login_window, text="").pack()
    entry_user_email = Entry(login_window, textvariable = user_mail_entry)
    entry_user_email.pack()
    Label(login_window, text="").pack()
    label_user_pass = Label(login_window, text="Ingrese Password", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_pass.pack()
    Label(login_window, text="").pack()
    entry_user_pass = Entry(login_window, textvariable = user_pass_entry)
    entry_user_pass.pack()
    Label(login_window, text="").pack()

    Button(login_window, text="Iniciar Sesión",command= lambda: handleUserLogin(entry_user_email.get(), entry_user_pass.get()), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#3BE3B0', anchor="center").pack()
    Label(login_window, text="").pack()
    Button(login_window, text="Cancelar y Salir", command = lambda: wb.deleteWindow(login_window), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#E33B3B', anchor="center").pack()