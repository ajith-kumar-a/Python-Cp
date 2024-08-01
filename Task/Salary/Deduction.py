from Salary import Salary

class Deduction(Salary):

    _insurance = 5578

    __PF = 12

    __Graduity = 5

    def getDeduction(self):
        bsalary =   self.getBaseSalary()
        PF = self._calculatePersent(bsalary,self.__PF)
        Gradutity = self._calculatePersent(bsalary,self.__Graduity)
        insurance = self._insurance

        return PF,Gradutity,insurance
