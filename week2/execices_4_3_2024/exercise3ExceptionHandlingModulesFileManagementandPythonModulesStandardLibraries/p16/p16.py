import pickle
def loadFromFile():
    with open("exercise3ExceptionHandlingModulesFileManagementandPythonModulesStandardLibraries/p16/my_variables.data","rb") as file:
        data= pickle.load(file=file)
    return data
print(loadFromFile())