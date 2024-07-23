# 5 question:Write a program to check if a string contains any special character

def checkSplletter(checkSplChar):
    special_Char = ['!','@','#','$','%','^','&','*','(',')','-','_','/','?','~',',','<','>','.',':',';','\'','\"','+','=','[',']','{','}']

    for ch in checkSplChar:
        if ch in special_Char:
            print('ji')
            return True
        else:
            continue
            print('hi')
       
   

def main():

    checkSplChar = input('Enter the String to Check Special Character : ')
    check = checkSplletter(checkSplChar)
    if check:
        print(f'{checkSplChar} Given String Contain Special Character')
    else:
        print(f'{checkSplChar} Given String not Contain Special Character')
 
if __name__ =='__main__':
    main()