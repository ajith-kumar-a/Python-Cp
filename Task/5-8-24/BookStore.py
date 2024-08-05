
class Bookstore:
    NoofBooks  = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        self.NoofBooks += 1

    def DisplayBookInfo(self):
        print(f'\nAuthor Name \t: {self.Author} \nBook Name \t: {self.Name} \nNo Of Books \t: {self.NoofBooks}')
        print("_" * 90)

def main():
    Obj1=Bookstore('Linux System Programming','Robert Love')
    Obj1.DisplayBookInfo()  # Linux System Programming. No of books : 1
    
    Obj2=Bookstore('C Programming','Robert Love')
    Obj2.DisplayBookInfo()  # C Programming by Dennis Ritchie. No of books :2

if __name__ == "__main__":
    main()