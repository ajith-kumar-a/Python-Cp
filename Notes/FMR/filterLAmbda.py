
#  Write a program which will check the number is greater and equal to 70 and less than and equal to 90

def Check_number(number):
    if number >= 70 and number <= 90:
        return number


def main():
    size = int(input('Enter the size : '))
    lst = []
    print('Enter value : ')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List ', lst)

    filter_list = list(filter(Check_number,lst))
    filter_list = list(filter(lambda x: x>=70 and x<=90 ,lst))
    print('Filter List : ',filter_list)
    
    
    add=lambda x,y: x+y
    print(add(2,3)) 
if __name__ == '__main__':
    main()