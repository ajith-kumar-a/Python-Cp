class Computer:
    # Attributes -> Varibales
    #  Behaviour -> function 

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.a = ram

    def config(self):
        print("configuration is ",self.cpu,self.a)

    def compare(self,comp):
        if self.cpu == comp.cpu:
            return True
        else:
            return False
            


comp1 = Computer("i5",16)
comp2 = Computer("i7",16)


comp1.config()

print(comp1.compare(comp2))

Computer.config(comp2)