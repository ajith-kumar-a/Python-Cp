# 3 Question:Create a simple calculator which will take two input number from the
# user and give following option
# 1)Addition
# 2) Subtraction
# 3)Multiplication
# 4)Division
# (you can solve above question using normal function )
# (also try to solve using dictionary)

def main():
    while True:
        print('\n1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division\n')

        option = int(input('Enter the option : '))

        if option == 1:
            num1,num2=  getNumberFromUser()
            print(f'Addition of {num1} + {num2} =  {Addition(num1,num2)}')
        elif option == 2:
            num1,num2=  getNumberFromUser()
            print(f'Subtraction of {num1} - {num2} =  {Subtraction(num1,num2)}')
        elif option == 3:
            num1,num2=  getNumberFromUser()
            print(f'Multiplication of {num1} X {num2} =  {Multiply(num1,num2)}')
        elif option == 4:
            num1,num2=  getNumberFromUser()
            print(f'Division of {num1} / {num2} =  {Division(num1,num2)}')


def getNumberFromUser():
   num1 = int(input('Entet the 1st Number : '))
   num2 = int(input('Entet the 2nd Number : '))

   return num1,num2

def  Addition(num1,num2):
   Add = num1+num2
   return Add

def Subtraction(num1,num2):
    Sub = num1-num2
    return Sub

def Multiply(num1,num2):
    Mul = num1*num2
    return Mul

def Division(num1,num2):
    Div = num1/num2
    return Div
   
 
if __name__ =='__main__':
    main()