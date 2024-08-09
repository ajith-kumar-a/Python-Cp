from abc import *

class Car(ABC):

    @abstractmethod
    def start_Engine(self):
        pass

    @abstractmethod
    def stop_Engine(self):
        pass

class ElectricCar(Car):
    def start_Engine(self):
        return 'Now The Electric Car Engine is Start'
    
    def stop_Engine(self):
        return 'Now the Electric Car Engine is Stoped'
    
    def Drive_car(self):
        return 'Now Your Driving GasOilCar car'
    
class GasOilCar(Car):
    def start_Engine(self):
        return 'Now The GasOilCar  Engine is Start'
    
    def stop_Engine(self):
        return 'Now the GasOilCar  Engine is Stoped'
    
    
    def Drive_car(self):
        return 'Now Your Driving GasOilCar car'

class OperateCar(ElectricCar):
   pass
    

ajith = OperateCar()
print(ajith.start_Engine())
print(ajith.stop_Engine())
print(ajith.Drive_car())