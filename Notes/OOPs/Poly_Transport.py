class Transport:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def Display(self):
        print(f'{self.brand} and {self.model}')

class Car(Transport):
   pass

class Boat(Transport):
    pass

class Bike(Transport):
    pass

car = Car("MAruti","i19")
car.Display()

boat = Boat("Shil","Titanic")
boat.Display()

bike = Bike("Passion Pro","109 cc")
bike.Display()