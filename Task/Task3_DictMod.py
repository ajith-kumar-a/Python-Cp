# 3 Question:Create a simple calculator which will take two input number from the
# user and give following option
# 1)Addition
# 2) Subtraction
# 3)Multiplication
# 4)Division
# (you can solve above question using normal function )
# (also try to solve using dictionary)

import ArthimeticOperation

def main():

    calculator = {1:'Addition',2:'Subtraction',3:'Multiplication',4:'Division',5:'History',6:'Exit'}
    operator = {1:'+',2:'-',3:'X',4:'/'}

    siNo = 0
    prevOperation = {}

    while True:
        for cal in calculator:
            print(f'{cal}. {calculator[cal]}')

        operations = {
        1: ArthimeticOperation.Addition,
        2: ArthimeticOperation.Subtraction,
        3: ArthimeticOperation.Multiply,
        4: ArthimeticOperation.Division
        }
    
        choice = int(input("\nEnter choice : "))

        if choice in operations:
            num1,num2,siNo = getNumberFromUser(siNo)

            operation = operations[choice]
            result = operation(num1, num2)
            print(f'Result: {result}\n')
            storedHistory = f'{num1} {operator[choice]} {num2} \t= {result}'
            # prevOperation.update({'e',storedHistory})
            prevOperation[siNo] = storedHistory
        elif choice == 5:
            history(prevOperation)
        elif choice == 6:
            break
        else:
            print("Invalid Input")

def history(prevOperation):
    print('SI No.\t Operation History')
    for prevHistory in prevOperation:
        print(f'{prevHistory}.\t {prevOperation[prevHistory]}')
    print('\n')


def getNumberFromUser(siNo):
   num1 = int(input('Entet the 1st Number : '))
   num2 = int(input('Entet the 2nd Number : '))
   
   siNo += 1

   return num1,num2,siNo

 
if __name__ =='__main__':
    main()