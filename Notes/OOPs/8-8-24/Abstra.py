from abc import ABC,abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

# Implement Abstract method in subclasses

class ConcreteClass(MyAbstractClass):
    def my_abstract_method(self):
        print('Implement of the abstract method')
        return super().my_abstract_method()
    


class Animal(ABC):

    @abstractmethod
    def sound(self):
        print('if nothing in ther means it will excute')

# Implement Abstract method in subclasses
# Define a concrete class that inherites from the abstract base class
class cat(Animal):
    def sound(self):
        print('Implement of the abstract method , Meow')
        return 'Meow'
    
class Dog(Animal):
    def sound(self):
        return 'Bark'

c = cat()
c.sound()

d = Dog()
d.sound()