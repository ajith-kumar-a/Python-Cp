#Creating Class

class Student:
    def __init__(self,firstname,lastname):
        self.firstname = firstname      #instance variable  #Properties
        self.lastname = lastname

    def Display(self):
        print(f'{self.firstname} {self.lastname}')

obj = Student("Ajith","Kumar")
Student.Display(obj)
