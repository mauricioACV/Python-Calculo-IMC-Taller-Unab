from tkinter import *
from WindowsApp import ImcReportWindow as irw
from Handlers import handlerUserDataPersistence as db
from Handlers import handlerWindowValidation as hv
from Handlers import handlerImc as himc
from Helpers import helpersFunctions as hf
from Behaviors import windowBehavior as wb

def imcDataWindow(userEmail, gender):    
    global imc_data_window
    imc_data_window = Toplevel()
    imc_data_window.overrideredirect(True)
    imc_data_window.title("Datos para calcular IMC")
    imc_data_window.geometry('800x600')

    imc_date_entry = StringVar()
    imc_time_entry = StringVar()
    imc_weight_entry = StringVar()
    user_height_entry = StringVar()

    def handleImcCalculation(mail, date, time, weight, height, gender):
        isValidImcData = hv.validateImcData(date, time, weight, height)
        if(isValidImcData['response']):
            userImcResult = float(himc.calculateImc(weight, height))
            userGender = gender.upper()
            successfulProcess = db.saveImcDataUser(mail, date, time, weight, height, userImcResult)
            if successfulProcess:        
                irw.imcReportWindow(mail, userGender)
                wb.deleteWindow(imc_data_window)
            else:
                wb.alertWindow("Error!", "Ocurrio un problema al registrar datos de IMC... Contacte a mesa de ayuda.")
        else:
            wb.alertWindow("Error!", isValidImcData['message'])

    Label(imc_data_window, text="").pack()
    Label(imc_data_window, text="Datos Cálculo IMC: " + userEmail, height=2, width=60, font=('Comic sens MC',14,'bold'), activebackground="aqua", bg='#1AACC1').pack()
    Label(imc_data_window, text="").pack()

    Label(imc_data_window, text="Género: " + gender.upper(), height=2, width=50, font=('Comic sens MC',11,'bold'), activebackground="aqua", bg='#B5ACD8').pack()
    Label(imc_data_window, text="").pack()

    label_user_date = Label(imc_data_window, text="Ingrese Fecha (ej. dd-mm-aaaa)", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_date.pack()
    entry_user_date = Entry(imc_data_window, textvariable = imc_date_entry)
    entry_user_date.insert(0, hf.getDate())
    entry_user_date.pack()
    Label(imc_data_window, text="").pack()

    label_user_time = Label(imc_data_window, text="Ingrese Hora (ej. hh:mm)", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_time.pack()
    entry_user_time = Entry(imc_data_window, textvariable = imc_time_entry)
    entry_user_time.insert(0, hf.getTime())
    entry_user_time.pack()
    Label(imc_data_window, text="").pack()

    label_user_weight = Label(imc_data_window, text="Ingrese peso kg (solo número)", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_weight.pack()
    entry_user_weight = Entry(imc_data_window, textvariable = imc_weight_entry)
    entry_user_weight.pack()
    Label(imc_data_window, text="").pack()

    label_user_height = Label(imc_data_window, text="Ingrese altura (ej. 1.84)", height=1, width=25, font=('Comic sens MC',11), relief="raised", bg='#B3B9B7')
    label_user_height.pack()
    entry_user_height = Entry(imc_data_window, textvariable = user_height_entry)
    entry_user_height.pack()
    Label(imc_data_window, text="").pack()

    Button(imc_data_window, text="Calcular IMC", command= lambda: handleImcCalculation(userEmail , entry_user_date.get(), entry_user_time.get(), entry_user_weight.get(), entry_user_height.get(), gender), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#3BE3B0', anchor="center").pack()
    Label(imc_data_window, text="").pack()
    Button(imc_data_window, text="Cancelar y Salir", command = lambda: wb.deleteWindow(imc_data_window), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#E33B3B', anchor="center").pack()