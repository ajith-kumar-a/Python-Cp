import datetime
year = datetime.date.today().year

class Company:

    area = "SIPCOD IT, SiruSeri"
    __city = "Chennai"

    def __init__(self,cname):
        self._cname = cname

    def display(self):
        print("Company Name : ",self._cname)

    def address(self):
        return self.area + " , "+self.__city + ", TamilNadu"

class Employee(Company):
    empId = 0
    isMarried = False

    def __init__(self,fname,lname,yob):
        self._fname = fname
        self._lname = lname
        self.__age = year + yob
        Employee.empId += 1
        self.__Id = Employee.empId

    def getEmpDetails(self):
        self.address
        print(f'Employee Id : {self.__Id}')
        print(f'Employee Name : {self._fname} {self._lname}')
        print(f'Employee Age : {self.__age}')
        print(f'Martial Status : {self.isMarried}')


c1 = Company("ChangePond")

c1.display()

print(c1.address())

e1 = Employee("Ajith","Kumar",2001)
e2 = Employee("Kumar","A",2000)

e1.getEmpDetails()

print("*"* 80)
e2.getEmpDetails()
print("*"* 80)