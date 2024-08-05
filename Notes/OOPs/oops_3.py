#Creating Class

class Student:
    Gradution = "BE"
    def __init__(self,firstname,lastname):
        self.firstname = firstname      #instance variable  #Properties
        self.lastname = lastname
        self.Gradution = "ME"

    def Display(self):
        print(f'{self.firstname} {self.lastname}')

obj = Student("Ajith","Kumar")
Student.Display(obj)

print(obj.Gradution)
print(obj.__class__.Gradution)
