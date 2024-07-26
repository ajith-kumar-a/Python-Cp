def Outer():
    print('Inside Outer')
    print()

    def Inner():
        print('Inside Inner')
        def ir():
            print('Inside Inner')
        return ir
    print('Inner:',id(Inner))

    return Inner

Outer()()()