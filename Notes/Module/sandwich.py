
def addXtraItem(sandwish):

    size = int(input('How Many item you want :'))
    for i in range(size):
        add_item = input('Enter the {i}. Xtra Item Sandwish : ')
        if not add_item in sandwish:
            sandwish.append(add_item)
        else:
            print('already exists')

def showXtraItem(*sandwish):
    print('\nSandwich contains Extra : ')
    for xtra in sandwish:
        print(f'\t->{xtra}')

def main():
    
    sandwish = []

    addXtraItem(sandwish)

    showXtraItem(*sandwish)

if __name__  == '__main__':
    main()