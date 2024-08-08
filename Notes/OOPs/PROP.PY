class Arithmatic:

    def __init__(self,value):
        self._value = value

    def getValue(self):
        print("Getting Value ")
        return self._value
    
    def setValue(self,value):
        print("Setting up Value ")
        self._value = value

    def delValue(self):
        print("Deleting Value ")
        del self._value

    value = property(getValue,setValue,delValue)

# A = Arithmatic(33)

# A.value

# A.value = 888

# del A.value

class PropertyUsingDecorator:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print('Getting value')
        return self._value

    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value


x = PropertyUsingDecorator('Ajith')
print(x.value)

x.value = 'Diesel'

del x.value