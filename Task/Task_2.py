 
# 2 Question:Write a program which will take input from the user and Returns(Using function)
# 1)Addition on the list
# Example: [2,3,4,5,6,7]  --> 27
# Note: don't use sum()
# 2)Maximum from the list
# Example: [2,3,4,5,6,7]  --> 7
# Note: don't use max()



def main():
    size = int(input('Enter the size if List : '))

    List_Numbers = []
    for num in range(size):
        value = int(input(f'Enter {num+1} value : '))
        List_Numbers.append(value)
    
    while True:
        print('\n1. Addition on the list ')
        print('2. Maximum from the list ')
        print('3. to Exit \n ')

        option = int(input('Please Enter the option : '))

        if option == 1:
            print(f'Addition of {List_Numbers} is : {AdditionOfList(List_Numbers)}')
        elif option == 2:
            print(f'Maximum from the {List_Numbers} is : {MaxfromList(List_Numbers)}')
        elif option == 3:
            break
        else:
            continue

def AdditionOfList(List_Numbers):
    total_num = 0
    for num in List_Numbers:
        total_num += num
    
    return total_num

def MaxfromList(List_Numbers):
    maxNum_inList = 0
    if len(List_Numbers) > 0:
        maxNum_inList = List_Numbers[0]

        for num in List_Numbers:
            if maxNum_inList < num :
                maxNum_inList = num
    else:
        print('List is Empty')

    return maxNum_inList


 
if __name__ =='__main__':
    main()