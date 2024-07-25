#  Write a program which will check the number is greater and equal to 70 and less than and equal to 90

def Check_number(number):
    if number >= 70 and number <= 90:
        return number


def main():
    size = int(input('Enter the size : '))
    lst = []
    print('Enter value : ',float('-inf'))
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List ', lst)

    filter_list = list(filter(Check_number,lst))
    print('Filter List : ',filter_list)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    second_max = float('-inf')
    print(second_max)
    for i in arr:   
        print(i)

    
    # main()