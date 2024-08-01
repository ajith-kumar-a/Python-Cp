
class Student:

    sclName = "Ajith Hr Sec School"

    def __init__(self,math,phy,che) :
        self.math = math
        self.phy = phy
        self.che = che
    
    def avg(self):
        return (self.phy+self.math+self.che) / 3
    
    @classmethod
    def getSchoolName(cls):
        return cls.sclName
    
    @staticmethod
    def info():
        print(f'welcome All to ')
        return "hi"


s = Student(99,95,97)

print(s.avg())
print(Student.info())
print(Student.getSchoolName())