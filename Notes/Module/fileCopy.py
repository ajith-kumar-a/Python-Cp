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

def createFile(new_file,content_file):
    
    if(os.path.exists(new_file)):
        print("File Already exits")
    else:
        file_create = open(new_file,'w')
        write_file = open(content_file,'r')
        file_create.write(write_file.read())
        print(f'{file_create} created sucessfully' )
       

def main():
    file_1 = input("Enter the file name Which you want to copy : ")

    file_2 = input(f'Enter a New File Name to copy content from {file_1} : ')

    createFile(file_2,file_1)

    compareFiles(file_2,file_1)


if __name__ == '__main__':
    main()