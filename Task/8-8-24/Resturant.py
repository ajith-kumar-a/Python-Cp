# 9-1. Restaurant: Make a class called Restaurant. The init() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods

class Resturant:

    def __init__(self):
        self.__restaurant_name = ""
        self.__cuisine_type = ""

    def getValues(self):
        return self.__restaurant_name,self.__cuisine_type
    
    def setValues(self,name,type):
        self.__restaurant_name = name
        self.__cuisine_type = type

    def describe_restaurant(self):
        name,type = self.getValues()
        print(f'Welcome to \'{name}\' Here We Serve {type} of Food')

    @staticmethod
    def open_restaurant():
        print("Now The Resturant is OPEN")



r = Resturant()
r.setValues("Ajith Resturant ","Indian Cuisine")
print(r.getValues())
Resturant.open_restaurant()
r.describe_restaurant()

