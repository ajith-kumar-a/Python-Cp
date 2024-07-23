# Dynamic Input

def freqCount(lst):
    dictionary = {}
    for l in lst:
        if l in dictionary.keys():
            dictionary[l] += 1
        else:
            dictionary[l] = 1
    
    print(dictionary)


def createList():
    print('Enter the Element you want to enter in the list')

    size = int(input('Enter the Size : '))
    data_input = []
    print('Enter The Values')

    for i in range(size):
        value = int(input(f'Enter the {i+1} value :' ))
        data_input.append(value)

    print('User List: ',data_input)
    freqCount(data_input)

def main():
    createList()

if __name__=='__main__':
    main()