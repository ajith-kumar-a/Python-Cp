from Salary import Salary


class Allowance(Salary):

    __HRA = 20

    __DA = 40

    __TA = 25

    def getAllowance(self):
      bsalary =   self.getBaseSalary()
      HRA = self._calculatePersent(bsalary,Allowance.__HRA)
      DA = self._calculatePersent(bsalary,Allowance.__DA)
      TA = self._calculatePersent(bsalary,Allowance.__TA)

      return HRA,DA,TA

    

       

