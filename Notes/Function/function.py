def Addiiton():
    print('inside Addition function') #No parameter ,# No Argument
Addiiton()

def Addiiton(num1,num2):
    # print('inside Addition function') #2 parameter ,# 2 Argument
    add = num1+num2
    sub = num2-num1
    return add,sub

add,sub = Addiiton(25,35)
print(add)
print(sub)