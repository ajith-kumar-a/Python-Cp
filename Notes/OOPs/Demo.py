class Demo:
    value = "i lo"

    def __init__(self,value1,value2) -> None:
        self.value1 = value1
        self.value2 = value2

    def Fun(self):
        print(f'Fun Method {self.value1} , {self.value2}')

    def Gun(self):
        print(f'Gun Method {self.value1} , {self.value2} {Demo.value}')


obj1 = Demo(11,123)
obj2 = Demo(22,44)

obj1.Fun()
obj1.Fun()

obj1.Gun()
obj1.Gun()

print(obj1.value)