class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def Displayinfo(self):
        print(f'Name : {self.name} Id: {self.id}')

class employee(Person):

    def __init__(self, id, name,salary):
        self.salary = salary
        # Person.__init__(id, name)
        super().__init__(id, name)

    def show(self):
        print('Child Class')

# Emp=Person('Ajith','4455')
# Emp.Displayinfo()

Emp=employee(2,'Ajith',15000)
Emp.Displayinfo()
Emp.show()