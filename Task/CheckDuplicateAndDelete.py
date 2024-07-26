

import os 
import filecmp

def compareFiles(file_1,file_2):
    compare = False
    
    if not os.path.exists(file_1):
        print(f'{file_1} not Found')

    elif not os.path.exists(file_2):
        print(f'{file_2} not Found')
       
    else:
        compare = filecmp.cmp(file_1,file_2)
    return compare

def deleteDuplicateFile(delFile):
    os.remove(delFile)


def main():

    file_1 = print('Enter the File 1 name : ')
    file_2 = print('Enter the file 2 name : ')

    compareTwoFiles = compareFiles(file_1,file_2)

    if compareTwoFiles:
        deleteDuplicateFile(file_2)
    else:
        print(f'{file_1} And {file_2} Are Different Files')


if __name__ == '__main__':
    main()