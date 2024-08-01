from Allowances import Allowance
from Deduction import Deduction
from functools import reduce


class CalculateSalary(Allowance,Deduction):

    def __init__(self,bsalary):
        super().__init__(bsalary)
        # self.setBaseSalary(bsalary)

    def getSalarySlip(self):
        bSalary = self.getBaseSalary()

        allowance = reduce((lambda num1 ,num2 : num1 + num2 ),self.getAllowance())
        deduction = reduce((lambda num1,num2 : num1 + num2),self.getDeduction())
        grossSalary = bSalary + allowance
        netSalary = grossSalary - deduction
     
        print("|"+"_" *38,"|")
        print(f'| Base Salary \t= \t{bSalary:10.2f}\t|')
        print(f'| Allowances \t= \t{allowance:10.2f}\t|')
        print(f'| Deduction \t= \t{deduction:10.2f}\t|')
        print(f'| GroSS Salary \t= \t{grossSalary:10.2f}\t|')
        print("|"+"_" * 38,"|")
        print(f'| Net Salary \t= \t{netSalary:10.2f}\t|')
        print("|"+"_" * 38,"|")
        


