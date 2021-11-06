from tkinter import *
from Handlers import handlerUserDataPersistence as db
from Handlers import handlerWindowValidation as hv
from Behaviors import windowBehavior as wb

def personDataWindow(email):
    global data_person_window
    data_person_window = Toplevel()
    data_person_window.title("Datos Persona")
    data_person_window.geometry('800x600')

    global user_name_entry
    global user_last_name_entry
    global user_age_entry
    global user_gender_entry
    user_name_entry = StringVar()
    user_last_name_entry = StringVar()
    user_age_entry = StringVar()
    user_gender_entry = StringVar()

    def handleSaveDataPerson(mail, name, lastName, gender, age):
        isValidDataPerson = hv.validateDataPerson(name, lastName, gender, age)
        if(isValidDataPerson['response']):
            successfulProcess = db.saveDataUser(mail, name, lastName, age, gender)
            if successfulProcess:
                wb.successWindow("Éxito", "Datos de usuario registados correctamente", data_person_window)
            else:
                wb.alertWindow("Error!", "Ocurrio un problema al registrar los datos... Contacte a mesa de ayuda.")
        else:
            wb.alertWindow("Error!", isValidDataPerson['message'])

    Label(data_person_window, text="").pack()
    Label(data_person_window, text="Datos Personales", height=2, width=60, font=('Comic sens MC',14,'bold'), activebackground="aqua", bg='#1AACC1').pack()
    Label(data_person_window, text="").pack()

    label_user_welcome = Label(data_person_window, text="Cuenta de usuario: " + email.upper(), height=2, width=50, font=('Comic sens MC',11,'bold'), activebackground="aqua", bg='#B5ACD8')
    label_user_welcome.pack()
    label_user_message = Label(data_person_window, text="Su cuenta de usuario se creó correctamente \n Por favor registre los siguientes datos:", height=2, width=50, font=('Comic sens MC',11,'bold'), activebackground="aqua", bg='#B5ACD8')
    label_user_message.pack()
    Label(data_person_window, text="").pack()

    label_user_name = Label(data_person_window, text="Ingrese Nombre", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_name.pack()
    Label(data_person_window, text="").pack()
    entry_user_name = Entry(data_person_window, textvariable = user_name_entry)
    entry_user_name.pack()
    Label(data_person_window, text="").pack()
    label_user_last = Label(data_person_window, text="Ingrese Apellidos", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_last.pack()
    Label(data_person_window, text="").pack()
    entry_user_last = Entry(data_person_window, textvariable = user_last_name_entry)
    entry_user_last.pack()
    Label(data_person_window, text="").pack()
    label_user_age = Label(data_person_window, text="Ingrese Edad", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_age.pack()
    Label(data_person_window, text="").pack()
    entry_user_age = Entry(data_person_window, textvariable = user_age_entry)
    entry_user_age.pack()
    Label(data_person_window, text="").pack()
    label_user_gender = Label(data_person_window, text="Ingrese Género (M o F)", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_gender.pack()
    Label(data_person_window, text="").pack()
    entry_user_gender = Entry(data_person_window, textvariable = user_gender_entry)
    entry_user_gender.pack()

    Label(data_person_window, text="").pack()
    Button(data_person_window, text="Registrame", command= lambda: handleSaveDataPerson(email, entry_user_name.get(), entry_user_last.get(), entry_user_gender.get(), entry_user_age.get()), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#3BE3B0', anchor="center").pack()