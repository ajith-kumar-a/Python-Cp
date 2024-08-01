from abc import ABC,abstractmethod
class Student:

    def __init__(self,m1,m2):
        self.math = m1
        self.phy = m2
        self.lap = self.Laptop()
    
    def show(self):
        print(self.math, self.phy)
        self.lap.show()

    class Laptop:

        def __init__(self):
            print("inner class")
            self.ram = 'i6'
            self.cpu = 'amd'

        def show(self):
            print(f'{self.ram} {self.cpu}')

s = Student(23,45)

s.show()
 
s.lap.show()

