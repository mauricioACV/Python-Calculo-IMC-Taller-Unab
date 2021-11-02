from tkinter import *
from WindowsApp import ImcReportWindow as irw
from Handlers import handlerUserDataPersistence as db
from Handlers import handlerImc as himc
from Helpers import helpersWindowValidation as hv
from Helpers import helpersFunctions as hf
from Behaviors import windowBehavior as wb

def imcDataWindow(userEmail, gender):    
    global imc_data_window
    imc_data_window = Toplevel()
    imc_data_window.overrideredirect(True)
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

    Label(imc_data_window, text="").pack()
    Label(imc_data_window, text="Datos Cálculo IMC: " + userEmail, height=2, width=60, font=('Comic sens MC',14,'bold'), activebackground="aqua", bg='#1AACC1').pack()
    Label(imc_data_window, text="").pack()

    Label(imc_data_window, text="Género: " + gender.upper(), height=2, width=50, font=('Comic sens MC',11,'bold'), activebackground="aqua", bg='#B5ACD8').pack()
    Label(imc_data_window, text="").pack()

    label_user_date = Label(imc_data_window, text="Ingrese Fecha Registro peso", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_date.pack()
    entry_user_date = Entry(imc_data_window, textvariable = imc_date_entry)
    entry_user_date.insert(0, hf.getDate())
    entry_user_date.pack()
    Label(imc_data_window, text="").pack()

    label_user_time = Label(imc_data_window, text="Ingrese Hora registro peso", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_time.pack()
    entry_user_time = Entry(imc_data_window, textvariable = imc_time_entry)
    entry_user_time.insert(0, hf.getTime())
    entry_user_time.pack()
    Label(imc_data_window, text="").pack()

    label_user_weight = Label(imc_data_window, text="Ingrese peso en kg", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_weight.pack()
    entry_user_weight = Entry(imc_data_window, textvariable = imc_weight_entry)
    entry_user_weight.pack()
    Label(imc_data_window, text="").pack()

    label_user_height = Label(imc_data_window, text="Ingrese altura (ej. 1.84)", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_height.pack()
    entry_user_height = Entry(imc_data_window, textvariable = user_height_entry)
    entry_user_height.pack()
    Label(imc_data_window, text="").pack()

    Button(imc_data_window, text="Calcular IMC", command= lambda: startImcCalculator(userEmail , entry_user_date.get(), entry_user_time.get(), entry_user_weight.get(), entry_user_height.get(), gender), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#3BE3B0', anchor="center").pack()
    Label(imc_data_window, text="").pack()
    Button(imc_data_window, text="Cancelar y Salir", command = lambda: wb.deleteWindow(imc_data_window), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#E33B3B', anchor="center").pack()

    def startImcCalculator(mail, date, time, weight, height, gender):
        isImcDataValid = hv.validateDataImc(date, time, weight, height)
        if(isImcDataValid['response']):
            userImcResult = float(himc.calculateImc(weight, height))
            userGender = gender.upper()
            db.saveImcDataUser(mail, date, time, weight, height, userImcResult)        
            irw.imcReportWindow(mail, userGender)
            wb.deleteWindow(imc_data_window)
        else:
            wb.alertWindow("Error!", isImcDataValid['message'])