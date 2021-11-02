import re

def validPassFormat(password):
    regexPattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%.,*?&])[A-Za-z\d$@$!%*?&][^'\s]")
    return bool(regexPattern.match(password))

def onlyIntNumbers(val):
    regexPattern = re.compile("^[0-9]+$")
    return bool(regexPattern.match(str(val)))

def validAge(age):
    if not onlyIntNumbers(age):
        return False
    if int(age) < 15 or int(age) > 70:
        return False
    else:
        return True

def validHeight(height):
    regexPattern = re.compile("^\d+\.\d{2,2}$")
    return bool(regexPattern.match(str(height)))

def onlyString(val):
    regexPattern = re.compile("^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$")
    return bool(regexPattern.match(val))

def validDateFormat(date):
    regexPattern = re.compile("^(?:(?:(?:0?[1-9]|1\d|2[0-8])[/](?:0?[1-9]|1[0-2])|(?:29|30)[/](?:0?[13-9]|1[0-2])|31[/](?:0?[13578]|1[02]))[/](?:0{2,3}[1-9]|0{1,2}[1-9]\d|0?[1-9]\d{2}|[1-9]\d{3})|29[/]0?2[/](?:\d{1,2}(?:0[48]|[2468][048]|[13579][26])|(?:0?[48]|[13579][26]|[2468][048])00))$")
    return bool(regexPattern.match(date))

def validTimeFormat(time):
    regexPattern = re.compile("^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
    return bool(regexPattern.match(time))

def validEmailFormat(email):
    regexPattern = re.compile("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")
    return bool(regexPattern.match(email))

def validGender(gender):
    if gender.upper() == "M" or gender.upper() == "F":
        return True
    else:
        return False

def getTime():
    import time
    hora = time.ctime()
    hora_hh_mm = hora.split()
    return hora_hh_mm[3][:-3]