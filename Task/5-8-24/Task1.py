# Instance Variable : Name , Amount , Address , AccountNo
# Instance Method  : CreateAccount() , DisplayAccountInfo()
#Class variable : Bank_name,ROI_On_FD 

class Account:
    Bank_Name = "ICICI BANK"
    ROI_On_FD = 12

    def __init__(self) :
        Name,Amount,Address,AccountNo = self.__CreateAccount()

        self.Name = Name
        self.Amount = Amount
        self.Address = Address
        self.AccountNo = AccountNo

    @classmethod
    def DisplayBankInformation(cls):
        print(f'Bank Name \t: {cls.Bank_Name} \nROI on FD \t: {cls.ROI_On_FD} ')

    def __CreateAccount(self):
        Name = input("Enter Name : ")
        Amount = int(input("Enter The Amount : "))
        Address = input("Enter The User Address : ")
        AccountNo = int(input("Enter the Account Number : "))

        return Name,Amount,Address,AccountNo



    def DisplayAccountInfo(self):
        print("_"* 90)
        print("---------------------- Your Account Info is Below -----------------")
        print(f'Bank Name \t:  {Account.Bank_Name} \nROI ON FD \t: {Account.ROI_On_FD} \nName \t\t: {self.Name} \nAmount \t\t: {self.Amount} \nAddress \t: {self.Address} \nAccount No \t: {self.AccountNo}')

def main():
    user1 = Account()
    user1.DisplayBankInformation()

    user1.DisplayAccountInfo()

if __name__ == "__main__":
    main()