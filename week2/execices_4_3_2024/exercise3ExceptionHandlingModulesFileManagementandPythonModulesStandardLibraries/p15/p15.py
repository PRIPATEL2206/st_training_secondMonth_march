import pickle
def storeInFile(**data):
    with open("exercise3ExceptionHandlingModulesFileManagementandPythonModulesStandardLibraries/p15/my_variables.data","wb") as file:
        pickle.dump(data,file=file)

storeInFile(
    data=1,
    some=5.5,
    di={"ok":1},
    li=[1,2,3,4],
    se=(134,5,6,7),
    tu=(1.,6,7,8)
)