# 
import os

def appendFile(filename,text_content):
    if os.path.exists(filename):
       file = open(filename,'a')
       file.write(text_content)
       print('Appended Sucessfully')
    else:
       print(f'{filename} Not Found')
    

def main():
    filename = input("Enter the file name Which you want to copy : ")

    text_content = input(f'Write a Content to Append {filename} file : ')

    appendFile(filename,text_content)


if __name__ == '__main__':
    main()