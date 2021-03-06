from tkinter import *
from Handlers import handlerUserDataPersistence as db
from Handlers import handlerImc as himc
from Behaviors import windowBehavior as wb

def imcReportWindow(userEmail, userGender):
    global imc_report_window
    imc_report_window = Toplevel()
    imc_report_window.overrideredirect(True)
    imc_report_window.title("Historial IMC")
    imc_report_window.geometry('800x600')


    Label(imc_report_window, text="").pack()
    Label(imc_report_window, text="Historial de IMC de: " + userEmail, height=2, width=60, font=('Comic sens MC',14,'bold'), activebackground="aqua", bg='#1AACC1').pack()
    Label(imc_report_window, text="").pack()

    imcList = db.getImcUserHistory(userEmail)

    if len(imcList) > 0:
        for imcItem in imcList:
            diagnostic = himc.getImcDiagnosticByGender(imcItem['imc'], userGender)
            Label(imc_report_window, text="Fecha Registro: " + imcItem['date']).pack()
            Label(imc_report_window, text="Hora Registro: " + imcItem['time'] + " ->> Peso: " + imcItem['weight'] + " ->> Altura: " + imcItem['height']).pack()
            Label(imc_report_window, text="IMC: " + imcItem['imc']).pack()
            Label(imc_report_window, text="Diagnóstico: " + diagnostic).pack()
            Label(imc_report_window, text="").pack()
    else:
        label_no_result = Label(imc_report_window, text="No tiene IMC registrados...", height=1, width=25, font=('Comic sens MC',12), relief="raised", bg='#B3B9B7')
        label_no_result.pack()
    
    Label(imc_report_window, text="").pack()
    Button(imc_report_window, text="Salir", command= lambda: wb.deleteWindow(imc_report_window), borderwidth=2, height=2, width=25, font=('Comic sens MC',12,'bold'), relief="raised", activebackground="aqua", bg='#E33B3B', anchor="center").pack()        