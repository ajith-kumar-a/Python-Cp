# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.


class User:
    def __init__(self):

        self.__emp_id=int(input('Enter empid : '))
        self.first_name=input('Enter First Name : ')
        self.last_name=input('Enter Last Name : ')
        self.email=input('Enter Email : ')
        self.phone_num=int(input('Enter your phonenumber : '))
        self.address=input('Enter your address : ')

    def describe_user(self):
        print(f'User details \nEmpid \t: {self.__emp_id} \nFirst_name \t: {self.first_name} \nLast_Name \t: {self.last_name} \nEmail \t: {self.email}  \nPhone \t: {self.phone_num} \nAddress \t: {self.address}')
   
    def greet_user(self):
        print(f'Hi {self.first_name}{self.last_name} Welcome To ChangePond')

def main():

    Ajith = User()
    Ajith.describe_user()
    Ajith.greet_user()


    Kumar = User()
    Kumar.describe_user()
    Kumar.greet_user()

if __name__ == "__main__":
    main()