# open() function -> filename , mode (r , w write and creae, a....)

# file_read = open('cal.py','r')

# print(file_read.read())

import os
def createFile(file_name):
    
    if(os.path.exists(file_name)):
        print("File Already exits")
    else:
        file_create = open(file_name,'w')
        print(f'{file_create} created sucessfully' )

def main():
    print('Enter the file name you want to create: ')
    file_name = input()

    createFile(file_name)

if __name__=="__main__":
    main()