def sum_all(*args):
    count = 0
    for i in args:
        count += i
    return count

output = sum_all(2,3,4,4,5,6,7,8,9,9)
print(output)

#  changepond = [] 



def name (*args):
    for name in args:
            print(name)

def staffDetails(**kwarg):
     for key,value in kwarg.items():
          print(f'{value}')
     
def  main():

    changepond = {'Name':'Ajtih','Age':21,'MobileNum':123456789}

    staffDetails(**changepond)

    fresher = ['Ajith','Gokul','Vijay','Prasanth']
    name(*fresher)


if __name__ == '__main__':
    main()