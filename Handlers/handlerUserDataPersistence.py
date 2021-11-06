import os
import json
import ast

def saveUserCredentials(userName, userPass):
    try:
        file = open("Data/"+ userName.lower() +"_credentials", "a")
        userCredentials = {'userName':userName.upper(), 'userPass':userPass}
        jsonCredentials = json.dumps(userCredentials)
        file.write(jsonCredentials + "\n")
    except:
        file.close()
        return False
    finally:
        file.close()
        return True

def saveDataUser(userMail, userName, userLastName, userAge, userGender):
    try:        
        file = open("Data/"+ userMail.lower() +"_data_user", "a")
        file2 = open("Data/"+ userMail.lower() +"_imc_history", "a")
        dataUser = {'userMail':userMail.upper(), 'name':userName.upper(), 'lastName':userLastName.upper(), 'age':userAge, 'gender':userGender.upper()}
        jsonDataUser = json.dumps(dataUser)
        file.write(jsonDataUser + "\n")
    except:
        file.close()
        file2.close()
        return False
    finally:
        file.close()
        file2.close()
        return True

def saveImcDataUser(userMail, date, time, weight, height, imc):
    try:
        file = open("Data/"+ userMail.lower() +"_imc_history", "a")
        userImc = {'date':date, 'time':time, 'weight':weight, 'height':height, 'imc':str(imc)}
        jsonUserImc = json.dumps(userImc)
        file.write(jsonUserImc + "\n")
    except:
        file.close()
        return False
    finally:
        file.close()
        return True

def getUserPassword(userEmail):
    path = open("Data/"+ userEmail.lower() + "_credentials", "r")
    data = path.readlines()
    userData = list(map(str.rstrip, data))
    dataDictionary = ast.literal_eval(userData[0])
    path.close()
    return dataDictionary['userPass']

def getUserGender(userEmail):
    path = open("Data/"+ userEmail.lower() + "_data_user", "r")
    data = path.readlines()
    userData = list(map(str.rstrip, data))
    dataDictionary = ast.literal_eval(userData[0])
    path.close()
    return dataDictionary['gender']

def getImcUserHistory(userEmail):
    path = open("Data/"+ userEmail.lower() + "_imc_history", "r")
    data = path.readlines()
    cleanUserData = list(map(str.rstrip, data))
    imcDataListDictionary = list(map(ast.literal_eval, cleanUserData))
    path.close()
    return imcDataListDictionary

def isRegisteredUser(userEmail):
    path = "Data/"+ userEmail.lower() + "_credentials"
    alreadyExist = os.path.exists(path)
    if alreadyExist:
        response = True
    else:
        response = False    
    return response