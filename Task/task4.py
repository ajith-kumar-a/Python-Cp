# 4 question:Write a program which will count the frequency of letters of the string

def freqCountOfString(givenString):

    frequencyCount = {}

    for str in givenString:
        if str in frequencyCount.keys():
            frequencyCount[str] += 1
        else:
            frequencyCount[str] = 1

    for freq in frequencyCount:
        print(f'\'{freq}\' is Present {frequencyCount[freq] } Times')
        


def main():
    givenString = input('Enter the Strig to get Frequency of Each letter : ')
    freqCountOfString(givenString)


 
if __name__ =='__main__':
    main()