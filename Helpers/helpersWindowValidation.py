from Helpers import helpersFunctions as hf

def validateFormatCredentials(email, password):
    if(not email and not password):
        return {'response':False, 'message':'Campos vacíos'}
    if(not hf.validEmailFormat(email)):
        return {'response':False, 'message':'Correo no válido, \n el formato requerido es correo@dominio.com'}
    if(not hf.validPassFormat(password)):
        return {'response':False, 'message':'Password no válida! \n intente digitar:\n al menos una letra en mayúscula, , \n al menos una letra en minúscula,\n al menos un carácter especial,\n y al menos un número'}
    return {'response':True}
    
def validateDataPerson(name, lastName, gender, age):
    if(not name or not lastName or not gender or not age):
        return {'response':False, 'message':'Campos vácios'}
    if not hf.onlyString(name):
        return {'response':False, 'message':'Nombre no válido'}
    if not hf.onlyString(lastName):
        return {'response':False, 'message':'Apellidos no válidos'}
    if not hf.validAge(age):
        return {'response':False, 'message':'Edad no válida, \n el rango permitodo es entre 15 y 70 años'}
    if not hf.validGender(gender):
        return {'response':False, 'message':'Género no válido, \n debe digitar "M" para masculino y "F" para femenino'}
    return {'response':True}

def validateImcData(date, time, weight, height):
    if(not date or not time or not weight or not height):
        return {'response':False, 'message':'Campos vácios'}
    if not hf.validDateFormat(date):
        return {'response':False, 'message':'Fecha no válida, \n el formato requerido es dd-mm-aaaa'}
    if not hf.validTimeFormat(time):
        return {'response':False, 'message':'Hora no válida, \n el formato requerido es HH:mm'}
    if not hf.onlyIntNumbers(weight):
        return {'response':False, 'message':'Peso no válido, \n el formato requerido es solo número entero en kg.'}
    if not hf.validHeight(height):
        return {'response':False, 'message':'Altura no válida, \n el formato requerido es un número entero y dos decimales ej: 1.90'}
    return {'response':True}