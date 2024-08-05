# class student:
#     graduation='BE'
#     def __init__(self,firstname,lastname):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.graduation='ME'
# obj1=student('Suresh','Manikandan')
# print(obj1.graduation)
# print(obj1.__class__.graduation)


class student:
    graduation='BE'

    def Graduate_In(cls):
        print('Graduation in:',cls.graduation)
student.Graduate=classmethod(student.Graduate_In)
student.Graduate()
print()
class student:
    graduation='BE'
    @classmethod
    def Graduate_In(cls):
        print('Graduation in:',cls.graduation)
student.Graduate_In()
