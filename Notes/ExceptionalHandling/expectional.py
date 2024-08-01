import datetime  
year = datetime.date.today().year

student_id = [123,123,124,126]
try:
    num = int(input())
    num2 = int(input())
    for i in range(5):
        print(i, '- ', student_id[i])
        

    reslut = num/num2
    print(reslut)
    assert num %2 ==0


except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
except IndexError as i:
    print(i)
except AssertionError as a:
    print('Entered value is not matching the test case')
else:
    print(num, " is even")
finally:
    print('Print program is over ')

yob = int(input('Enter your year of birth : '))

age = year - yob

if(age < 18):
    raise Exception(f'Your under 18 bro ')