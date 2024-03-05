class Student:
    name=False
    regNo=False
    rollNo=False
    standard=False
    admissionYear=False
    marks=[]
    result=False
    def __init__(self,name:str,regNo:str,rollNo:str,standard:str,admissionYear:str) -> None:
        if not (name.isalnum() and regNo.isalnum()):
            raise Exception("name and regNo mustbe alphanumeric")
        if not (rollNo.isnumeric() and standard.isnumeric() and admissionYear.isnumeric()):
            raise Exception("rollNo , standard , admissionYear must be in numaric")
        self.name=name
        self.regNo=regNo
        self.rollNo=rollNo
        self.standard=standard
        self.admissionYear=admissionYear
        self.result="Pass"

    def addMarks(self,marks:dict):
        for key,val in marks.items():
            if val<0 and val>100:
                raise Exception("marks should be in range 0 to 100")
           
            if (val<40):
                self.result="Fail"    
            self.marks.append({
                "subject":key,
                "marks":val
            })

    def genarateResult(self):
        if len(self.marks)==0:
            return
        totalSub=len(self.marks)
        totalMarks=0

        print(f'''
*******************************************************************
Name : {self.name}
Roll No : {self.rollNo}                   Standard: {self.standard}
*******************************************************************
'''
            )
        print("Subject    Total Marks   Passing Marks    Obtained Marks    Result")
        for re in self.marks:
            totalMarks+=re["marks"]
            print(f"{re["subject"]}         100              40               {re["marks"]}           {"Fail" if re["marks"]<40 else "pass"}")
        print("*******************************************************************")
        print(f"TOTAL        {100*totalSub}            {40*totalSub}                {totalMarks}")
        print(f"Result: {self.result}                                     Percentage: {round(totalMarks/(100*totalSub)*100,2)} %")

s=Student("stu1","s23","12","11","2020")
marks={
    "maths":97,
    "phy":96,
    "che":96
}
s.addMarks(marks)
s.genarateResult()