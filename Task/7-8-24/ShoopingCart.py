# Create a class representing a shopping cart. 
# Which include methods for adding items , removing items , 
# total items and total price

class ShoppingCart:

    def __init__(self):
        self.cart ={}

    def displayCart(self):
        print('\nDisplaying Cart Items')
        print(f'No\t CartItem \t Price')
        for cart in self.cart:
            print(f'{list(self.cart.keys()).index(cart) + 1} \t {cart} \t {self.cart[cart]}')
        print('\n')

    def adding(self):
        item = input("Enter the Item You wand to Add : ")
        price = float(input(f'Enter {item} Price : '))
        self.cart[item] = price

    def removing(self):
        self.displayCart()
        removeFood = input('Please Enter the above Cart Name which you want remove :')

        if removeFood in self.cart:
            print(f'{removeFood} Sucessfully \n')
            self.cart.pop(removeFood)

        else:
            print('*****Enter The Valid Cart Item Name ******')
            self.removing()
       

    def totalItem(self):
        totalItem =  len(self.cart)
        return totalItem

    def totalPrice(self):
        totalPrice = 0
        for i in self.cart.values():
            totalPrice += i

        return totalPrice


def main():
    ajith = ShoppingCart()

    while(True):
        

        dashBoard = {1:'Display Cart Item ',2:'Add Cart Item ',3:'Check Total Item',4:'Remove Cart Item ',5:'Check Total Price ',6:'to Exit'}
        print("\n")
        for menu in dashBoard:
            print(f'{menu}. {dashBoard[menu]}')

        print("\n")
        option = int(input('Enter the Option :'))

        if option == 1:
            ajith.displayCart()
            print('\n *** Thank You *** \n')
        elif option == 2:
            ajith.adding()
        elif option == 3:
            print(ajith.totalItem())
        elif option == 4:
            ajith.removing()
        elif option == 5:
            print(ajith.totalPrice())
        elif option == 6:
            break
        else:
            continue

    ajith.removing()

if __name__ == "__main__":
    main()