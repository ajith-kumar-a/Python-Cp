# public : These are accessible from 

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary

    def DisplaySalaryInfo(self):
        print(f'{self.name} holding salary of {self._salary}')

e1 = Employee('ANKITA',250000)
print(e1._salary)
e1.DisplaySalaryInfo()        

class Employees:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def DisplaySalaryInfo(self):
        print(f'{self.name} holding salary of {self._salary}')

e1 = Employees('ANKITA',250000)
print(e1.__salary)
e1.DisplaySalaryInfo()    