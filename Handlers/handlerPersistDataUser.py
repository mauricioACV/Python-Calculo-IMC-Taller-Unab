import os

def saveUserCredentials(userName, userPass):
    file = open("Data/"+ userName +"_credentials", "a")
    file.write(userName + "\n")
    file.write(userPass + "\n")
    file.close()

def saveDataUser(userMail, userName, userLastName, userAge, userGender):
    file = open("Data/"+ userMail +"_data", "a")
    file.write(userName + "\n")
    file.write(userLastName + "\n")
    file.write(userAge + "\n")
    file.write(userGender + "\n")
    file.close()

def saveImcDataUser(userMail, date, time, weight, height, imc):
    file = open("Data/"+ userMail +"_imc_history", "a")
    file.write(date + "\n")
    file.write(time + "\n")
    file.write(weight + "\n")
    file.write(height + "\n")
    file.write(str(imc) + "\n")
    file.close()

def getUserPassword(userEmail):
    path = open("Data/"+ userEmail + "_credentials", "r")
    data = path.readlines()
    userData = list(map(str.rstrip, data))
    path.close()
    return userData[1]

def getUserGender(userEmail):
    path = open("Data/"+ userEmail + "_data_user", "r")
    data = path.readlines()
    userData = list(map(str.rstrip, data))
    path.close()
    return userData[3]

def isRegisteredUser(userEmail):
    path = "Data/"+ userEmail + "_credentials"
    alreadyExist = os.path.exists(path)
    if alreadyExist:
        response = True
    else:
        response = False
    
    return response