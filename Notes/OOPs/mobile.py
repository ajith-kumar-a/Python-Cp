
class Mobile:

    def __init__(self,brand,RAM):
        self.ram = RAM
        self.brand = brand

    def Display(self):
        print(f'{self.brand} {self.ram}')

mobile1 = Mobile("Vivo","4 Gb")
mobile1.Display()