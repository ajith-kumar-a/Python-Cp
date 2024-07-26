
def sub(n1,n2):
    ans = n1-n2
    return ans

def decorated_function(sub_fun):
    

    def inner(a,b):
        if(a<b):
            a,b = b,a
        output = sub_fun(a,b)
        return output
    return inner

def main():
    num1 = int(input('Enter the First number : '))
    num2 = int(input('Enter the sec Number : '))

    new_func = decorated_function(sub(num1,num2))

    # result = new_func
    print(new_func)

if __name__ == '__main__':
    main()