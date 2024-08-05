# 6)Write a program which contains one class named as Numbers.

# Arithmetic class contains one instance variables as Value1,Value2.

# Inside init method initialize all instance variables to 0.

# There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().

# Accept method will accept value of value1 and value2 from user.

# Addition() method will perform addition of Value1 and Value2 and return result.

# Subtraction() method will perform subtraction of Value1 and Value2 and return result.

# Multiplication() method will perform multiplication of Value1 and Value2 and return result.

# Division() method will perform division of Value1 and Value2 and return result.

# After Designing the above class call all instance methods by creating multiple objects.

class Number:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = float(input("Enter Value 1 : "))
        self.value2 = float(input("Enter Value 2 : "))

    def Addition(self):
        add = self.value1 + self.value2
        return add
    
    def Subtraction(self):
        sub = self.value1 - self.value2
        return sub
    
    def Multiplication(self):
        mul = self.value1 * self.value2
        return mul
    
    def Division(self):
        div = self.value1 / self.value2
        return div
    
def main():
    num1 = Number()
    num1.Accept()

    print(num1.Addition())
    print(num1.Subtraction())
    print(num1.Multiplication())
    print(num1.Division())

if __name__ == "__main__":
    main()

