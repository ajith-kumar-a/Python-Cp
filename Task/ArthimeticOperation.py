def  Addition(num1,num2):
   Add = num1+num2
   return Add

def Subtraction(num1,num2):
    Sub = num1-num2
    return Sub

def Multiply(num1,num2):
    Mul = num1*num2
    return Mul

def Division(num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero!"