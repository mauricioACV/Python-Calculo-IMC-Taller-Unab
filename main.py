from tkinter import *
from Helpers import helpersWindowValidation as hv
from Handlers import handlerImc as himc
from Behaviors import windowBehavior as wb

user_mail_global=""
user_gender_global=""

# *************************************************************************************************
# ****************************************** Windows App ******************************************
# *************************************************************************************************

def registrationWindow():    
    global registration_window
    registration_window = Toplevel()
    registration_window.title("Inscripción")
    registration_window.geometry('800x600')

    global user_email_entry
    global user_pass_entry
    user_mail_entry = StringVar()
    user_pass_entry = StringVar()

    Label(registration_window, text="Formulario Inscripción").pack()
    Label(registration_window, text="").pack()

    label_user_email = Label(registration_window, text="Ingrese Email")
    label_user_email.pack()
    entry_user_email = Entry(registration_window, textvariable = user_mail_entry)
    entry_user_email.pack()
    Label(registration_window, text="").pack()
    label_user_pass = Label(registration_window, text="Ingrese Password")
    label_user_pass.pack()
    entry_user_pass = Entry(registration_window, textvariable = user_pass_entry)
    entry_user_pass.pack()
    Label(registration_window, text="").pack()
    Button(registration_window, text="Registrarse", command= lambda: starRegister(entry_user_email.get(), entry_user_pass.get())).pack()

    def starRegister(email, password):
        global user_mail_global
        isRegisterProcessValid = hv.validateRegister(email, password)
        if(isRegisterProcessValid['response']):
            user_mail_global = email
            dataPersonWindow()
        else:
            wb.alertWindow("Error!", isRegisterProcessValid['message'])

def dataPersonWindow():
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

    Label(registration_window, text="Datos Persona").pack()
    Label(registration_window, text="").pack()

    label_user_welcome = Label(data_person_window, text="Hola: " + user_mail_global.upper())
    label_user_welcome.pack()
    label_user_message = Label(data_person_window, text="Su inscripción fue exitosa! \n Por favor Ingrese los siguientes datos:")
    label_user_message.pack()
    Label(data_person_window, text="").pack()

    label_user_name = Label(data_person_window, text="Ingrese Nombre")
    label_user_name.pack()
    entry_user_name = Entry(data_person_window, textvariable = user_name_entry)
    entry_user_name.pack()
    Label(data_person_window, text="").pack()
    label_user_last = Label(data_person_window, text="Ingrese Apellidos")
    label_user_last.pack()
    entry_user_last = Entry(data_person_window, textvariable = user_last_name_entry)
    entry_user_last.pack()
    Label(data_person_window, text="").pack()
    label_user_age = Label(data_person_window, text="Ingrese Edad")
    label_user_age.pack()
    entry_user_age = Entry(data_person_window, textvariable = user_age_entry)
    entry_user_age.pack()
    Label(data_person_window, text="").pack()
    label_user_gender = Label(data_person_window, text="Ingrese Género (M o F)")
    label_user_gender.pack()
    entry_user_gender = Entry(data_person_window, textvariable = user_gender_entry)
    entry_user_gender.pack()
    Label(data_person_window, text="").pack()
    Button(data_person_window, text="Registrarse", command= lambda: setDataPerson(entry_user_name.get(), entry_user_last.get(), entry_user_gender.get(), entry_user_age.get())).pack()

    def setDataPerson(name, lastName, gender, age):
        global user_gender_global
        isPersonDataValid = hv.validateDataPerson(name, lastName, gender, age)
        if(isPersonDataValid['response']):
            user_gender_global = gender
            imcDataWindow()
        else:
            wb.alertWindow("Error!", isPersonDataValid['message'])

def imcDataWindow():    
    global imc_data_window
    imc_data_window = Toplevel()
    imc_data_window.title("Datos para calcular IMC")
    imc_data_window.geometry('800x600')

    global imc_date_entry
    global imc_time_entry
    global imc_weight_entry
    global user_height_entry
    imc_date_entry = StringVar()
    imc_time_entry = StringVar()
    imc_weight_entry = StringVar()
    user_height_entry = StringVar()
    
    Label(imc_data_window, text="Datos Cálculo IMC").pack()
    Label(imc_data_window, text="").pack()

    Label(imc_data_window, text="Género: " + user_gender_global.upper()).pack()
    Label(imc_data_window, text="").pack()

    label_user_date = Label(imc_data_window, text="Ingrese Fecha Resgistro peso")
    label_user_date.pack()
    entry_user_date = Entry(imc_data_window, textvariable = imc_date_entry)
    entry_user_date.pack()
    Label(imc_data_window, text="").pack()

    label_user_time = Label(imc_data_window, text="Ingrese Hora registro peso")
    label_user_time.pack()
    entry_user_time = Entry(imc_data_window, textvariable = imc_time_entry)
    entry_user_time.pack()
    Label(imc_data_window, text="").pack()

    label_user_weight = Label(imc_data_window, text="Ingrese peso en kg")
    label_user_weight.pack()
    entry_user_weight = Entry(imc_data_window, textvariable = imc_weight_entry)
    entry_user_weight.pack()
    Label(imc_data_window, text="").pack()

    label_user_height = Label(imc_data_window, text="Ingrese altura en con dos decimales (ej. 1.84)")
    label_user_height.pack()
    entry_user_height = Entry(imc_data_window, textvariable = user_height_entry)
    entry_user_height.pack()
    Label(imc_data_window, text="").pack()

    Button(imc_data_window, text="Calcular IMC", command= lambda: startImcCalculator(entry_user_date.get(), entry_user_time.get(), entry_user_weight.get(), entry_user_height.get(), user_gender_global.upper())).pack()

    def startImcCalculator(date, time, weight, height, gender):
        isImcDataValid = hv.validateDataImc(date, time, weight, height)
        if(isImcDataValid['response']):
            userImcResult = float(himc.calculateImc(weight, height))
            userGender = gender.upper()
            if userGender == "M":
                message = himc.evaluateManImc(userImcResult)        
            if userGender =="F":
                message = himc.evaluateWomanImc(userImcResult)
            wb.alertWindow("IMC Calculado", "Su IMC es: " + str(userImcResult) + " y el resultado es: " + message)
        else:
            wb.alertWindow("Error!", isImcDataValid['message'])

# *************************************************************************************************
# ************************************ Main App ************************************
# *************************************************************************************************

def mainWindow():
    global principal_window
    principal_window = Tk()
    principal_window.title("Calculadora IMC")
    principal_window.geometry('800x600')
    principal_window.resizable(0,0)

    Label(text="CALCULA TU ÍNDICE DE MASA CORPORAL").pack()
    Label(text="").pack()
    Button(text="Registrate", command=registrationWindow).pack()
    Label(text="").pack()
    Button(text="Inicia Sesión", command=registrationWindow).pack()

    principal_window.mainloop()

mainWindow()