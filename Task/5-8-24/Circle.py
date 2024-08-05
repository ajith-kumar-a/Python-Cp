
class Circle:
    __PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0


    def Accept(self):
        self.Radius = int(input("Enter the Radius : "))
        self.CalculateArea()
        self.CalculateCircumference()

    def CalculateArea(self):
        self.Area = self.__PI * self.Radius**2

    def CalculateCircumference(self):
        Circumference = 2 * self.__PI * self.Radius
        self.Circumference = Circumference

    def Display(self):
        print(f'\nRadius \t: {self.Radius} \nArea \t : {self.Area} \nCircumfrence \t: {self.Circumference}')

def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.Display()

    obj2 = Circle()
    obj2.Accept()
    obj2.Display()

    obj3 = Circle()
    obj3.Accept()
    obj3.Display()

if __name__ == "__main__":
    main()

