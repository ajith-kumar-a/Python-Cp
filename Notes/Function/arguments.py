# Area of Circle = PI*R*R

def AreaOfCircle(Radius,PI=3.14):
    Result = PI*Radius*Radius
    return Result

def main():
    # Positional Argument
    output_1 = AreaOfCircle(10,12)
    print(output_1)

    # first arguments is posional and Defauly
    output_1 = AreaOfCircle(10)
    print(output_1)

    # Keyword Argument
    output_1 = AreaOfCircle(Radius=10)
    print(output_1)
    print(type(output_1))
    print(type(AreaOfCircle(Radius=10)))

if __name__ == '__main__':
    main()