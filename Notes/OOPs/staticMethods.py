
class Student:

    @staticmethod
    def RollNumber(y):
        print("Inside Static Method",y)

Student.RollNumber(102)

s1 = Student()
s1.RollNumber(103)

class Student:

    

    @staticmethod
    def RollNumber(y):
        print("Inside Static Method",y)

Student.RollNumber = staticmethod(Student.RollNumber)
Student.RollNumber(102)
