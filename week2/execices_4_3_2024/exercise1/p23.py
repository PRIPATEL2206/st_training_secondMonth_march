class Vihical:
    def run(self):
        print("vihical is running")

class Car(Vihical):
    # over loading
    def run(self):
        print("Car in running")
    #Over Overwrite
    def selfDrive(self):
        print("Self Drive Car")

   

if __name__ == "__main__":
    c=Car()
    p=Vihical()
    p.run()
    c.run()
    c.selfDrive()