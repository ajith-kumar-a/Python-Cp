import os
import filecmp

def compareFiles(file_1,file_2):
    if not os.path.exists(file_1):
        print(f'{file_1} is not Exists')
    elif not os.path.exists(file_2):
        print(f'{file_2} is not Exists')
    else:
        compare = filecmp.cmp(file_1,file_2)    
        if compare == True:
            print('Both File Are Same')
        else:
            print('Failed -> Both file are not Same')

def main():
    file_1 = input("Enter the First File Name : ")
    file_2 = input("Enter the Second File Name : ")

    compareFiles(file_1,file_2)
if __name__ == '__main__':
    main()