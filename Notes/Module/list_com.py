#  Using for loop you have create list of square numbr

def square_numbers(n):
    square_list=[]
    for i in range(1,n+1):
        square_list.append(i*i)
    print(square_list)

if __name__=="__main__":
    square_numbers(5)
    print(min)