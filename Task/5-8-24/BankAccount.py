    
    # 4) Write a program which contains one class named as BankAccount.
    # BankAccount class contains two instance variables as Name & Amount.
    # That Class Contains one class variable as ROI which is initialize to 10.5
    # Inside init method initialize all name and amount variable by accepting the values from user.
    # There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
    # Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
    # Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
    # CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
    # And Display () method will display value of all the instance variables as Name and Amount.
    # After designing the above class call all instance methods by creating multiple objects

class BankAccount:
    ROI = 10.5

    @staticmethod 
    def DisplayKYCInfo():
        print(f'Submit you\'r Aadhar Card \nSubmit your\'r 2 Passport size photo \nSubmit you\'r Pan Details ')


    def __init__(self):
        self.Name = input("Enter User Name : ")
        self.__Amount = int(input('Enter Amount : '))

    def Display(self):
        print("_"* 90)
        print(f'\nUser Name \t: {self.Name} \nAmount \t: {self.__Amount} \nRate Of Intrest \: {self.CalculateIntrest()}')

    def Deposit(self):
        self.__Amount += float(input("Enter The Amount To Deposite : "))

    def Withdraw(self):
        self.__Amount -= float(input("Enter The Withdraw Amount  : "))

    def Withdraw(self,amt):
        self.__Amount -= amt

    def Deposit(self,amt):
         self.__Amount += amt

    def CalculateIntrest(self):
        intrest = (BankAccount.ROI * self.__Amount) /100
        return intrest
    
def main():
    BankAccount.DisplayKYCInfo()
    ajith = BankAccount()
    ajith.Deposit()
    ajith.Display()
    ajith.CalculateIntrest()
    ajith.Display()
    

if __name__ == "__main__":
    main()

    

    