def checkFrequecy(filename, searchstring):
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"The file {filename} does not exist")
        return

    contentlower = content.lower()
    searchstringlower = searchstring.lower()

    frequency = contentlower.count(searchstringlower)

    print(f"The string '{searchstring}' appears {frequency} times")
    
def main():
    filename = input("Enter the file name: ")
    search_string = input("Enter the string to search : ")

    checkFrequecy(filename, search_string)

if __name__=="__main__":
    main()