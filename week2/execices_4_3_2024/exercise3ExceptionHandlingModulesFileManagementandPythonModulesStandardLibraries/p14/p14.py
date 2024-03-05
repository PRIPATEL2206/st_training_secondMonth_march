with open("exercise3ExceptionHandlingModulesFileManagementandPythonModulesStandardLibraries/p14/test_file.txt","b+r") as file:
    print(file.read())

with open("exercise3ExceptionHandlingModulesFileManagementandPythonModulesStandardLibraries/p14/test_file.txt","ab") as file:
    file.write(bytes(b"\nok"))