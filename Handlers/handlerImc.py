def calculateImc(weight, height):
    return round(int(weight) / pow(float(height), 2), 1)

def getImcDiagnosticByGender(imc, gender):
    if gender == "M":
        message = evaluateManImc(imc)
    if gender =="F":
        message = evaluateWomanImc(imc)
    return message

def evaluateManImc(imc):
    imcVal = float(imc)
    if imcVal < 20:
        return "Bajo Peso"
    if imcVal >= 20 and imcVal < 25:
        return "Normal"
    if imcVal >= 25 and imcVal < 30:
        return "Obesidad Leve"
    if imcVal >= 30 and imcVal <= 40:
        return "Obesidad Severa"
    if imcVal > 40:
        return "Obesidad muy severa"

def evaluateWomanImc(imc):
    imcVal = float(imc)
    if imcVal < 20:
        return "Bajo Peso"
    if imcVal >= 20 and imcVal < 24:
        return "Normal"
    if imcVal >= 24 and imcVal < 29:
        return "Obesidad Leve"
    if imcVal >= 29 and imcVal <= 37:
        return "Obesidad Severa"
    if imcVal > 37:
        return "Obesidad muy severa"