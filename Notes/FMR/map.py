from functools import reduce
def main():
    size = int(input('Enter the size : '))
    lst = []
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List ', lst)

    map_list = list(map(lambda num:num**3,lst))
    print('Map List ',map_list,'\n')

    reduce_list = reduce((lambda num1,num2 : num1+num2),map_list)
    print('Reduce Value ', reduce_list)


if __name__ == '__main__':
    main()