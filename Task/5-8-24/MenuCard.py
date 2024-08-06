# 1) Create a menu_card list
# veg_starter = ['paneer 65','chilly paneer','veg crispy']
# 1) Display menu card
# 2)Add Starter in the menu card
# 3)Update Starter in the menu card
# 4)Remove Starter in the menu card

# Example:
# Add : Which starter you want to add in menu?
# paneer roll
# ['Paneer 65','Chilly paneer','Veg crispy','Paneer roll']
# Added Successfully


class MenuCard:
    def __init__(self):

        self.foodMenu = []
        self.size = len(self.foodMenu)

    def addFoodItem(self):
        food_item = input(f'Enter the {len(self.foodMenu) +1} food item : ')
        self.foodMenu.append(food_item)
        print(f'Added {food_item} Sucessfully\n')
    
    def displayFoodMenu(self):
        print('\nDisplaying Food Items')

        if len(self.foodMenu) == 0:
            print("\nFood Menu is Empty")

        for food in self.foodMenu:
            print(f'{self.foodMenu.index(food) +1}. {food}')
        print('\n')
    
    def updateFoodItem(self):
        self.displayFoodMenu()
        foodIndex = int(input(f'Enter the index between 1 to {len(self.foodMenu) } : '))
        if (foodIndex >= 1 and len(self.foodMenu) >= foodIndex):
            foodItems = input(f'now Your updating {self.foodMenu[foodIndex-1]} to replace New Food :')
            self.foodMenu.pop(foodIndex-1)
            self.foodMenu.insert(foodIndex-1,foodItems)
        else:
            print(f'Please Enter the index between 0 to {len(self.foodMenu) -1 }')
            self.updateFoodItem(self.foodMenu)
    
    def removeFoodItem(self):
        self.displayFoodMenu()
        removeFood = input('Please Enter the above Food Name which you want remove :')

        if removeFood in self.foodMenu:
            self.foodMenu.remove(removeFood)
        else:
            print('Please Enter the valid Food Name which you want remove :')
            self.removeFoodItem(self.foodMenu)


def main():
    m1 = MenuCard()

    while True:
        print('1 Display menu card')
        print('2 Add Starter in the menu card')
        print('3 Update Starter in the menu card')
        print('4 Remove Starter in the menu card')
        print('5 to Exit')

        print()
        option = int(input('Enter the Option :'))

        if option == 1:
            m1.displayFoodMenu()
            print('\n *** Thank You *** \n')
        elif option == 2:
            m1.addFoodItem()
        elif option == 3:
            m1.updateFoodItem()
        elif option == 4:
            m1.removeFoodItem()
        elif option == 5:
            break
        else:
            continue


if __name__ =='__main__':
    main()