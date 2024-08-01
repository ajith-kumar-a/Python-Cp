
class Salary:

    def __init__(self,eee):
        self._baseSalary = eee
        

    # def setBaseSalary(self,bsalary):
    #     self._baseSalary = bsalary
        

    def getBaseSalary(self):
        return self._baseSalary
    
    def _calculatePersent(self,salary,allowance):
       persent = allowance/100
       allowanceAmount = persent*salary

       return allowanceAmount