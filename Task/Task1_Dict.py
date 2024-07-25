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

def main():
    size = int(input('Enter the no of Item you Want to add in Food Menu : '))

    foodMenu = {}

    for food in range(size):
        addFoodItem(foodMenu)
    
    displayFoodMenu(foodMenu)
    print(list(foodMenu)[0])

    dashBoard = {1:'Display menu card',2:'Add Starter in the menu card',3:'Update Starter in the menu card',4:'Remove Starter in the menu card',5:'to Exit'}

    while True:
       
        for menu in dashBoard:
            print(f'{menu}. {dashBoard[menu]}')

        print('')
        option = int(input('Enter the Option :'))

        if option == 1:
            displayFoodMenu(foodMenu)
            print('\n *** Thank You *** \n')
        elif option == 2:
            addFoodItem(foodMenu)
        elif option == 3:
            foodMenu=updateFoodItem(foodMenu)
        elif option == 4:
            removeFoodItem(foodMenu)
        elif option == 5:
            break
        else:
            continue

def displayFoodMenu(foodMenu):
    print('\nDisplaying Food Items')
    print(f'No\t FoodName \t Price')
    for food in foodMenu:
        print(f'{list(foodMenu.keys()).index(food) + 1} \t {food} \t {foodMenu[food]}')
    print('\n')

def addFoodItem(foodMenu):
    food_item = input(f'Enter the {len(foodMenu) +1} food item : ')
    food_price = input(f'Enter the \'{food_item}\' Price : ')
    foodMenu.update({food_item:food_price})
    print(f'Added {food_item} Sucessfully\n')


def updateFoodItem(foodMenu):
    displayFoodMenu(foodMenu)
    foodIndex = int(input(f'Enter the index between 1 to {len(foodMenu) } : '))
    if (foodIndex >= 1 and len(foodMenu) >= foodIndex):

        foodItems = input(f'now Your updating \'{list(foodMenu)[foodIndex-1]}\' to replace New Food :')
        foodPrice = input(f'now Your updating \'{foodItems}\'s Price :')
    
        foodMenu.pop(list(foodMenu)[foodIndex-1])

        items = list(foodMenu.items())
        items.insert(foodIndex-1,(foodItems,foodPrice))
      
        foodMenu=dict(items)
        print()
    else:
        print(f'Please Enter the index between 0 to {len(foodMenu) -1 }')
        updateFoodItem(foodMenu)
    return foodMenu


def removeFoodItem(foodMenu):
    displayFoodMenu(foodMenu)
    removeFood = input('Please Enter the above Food Name which you want remove :')

    if removeFood in foodMenu:
        print(f'{removeFood} Sucessfully \n')
        foodMenu.pop(removeFood)

    else:
        print('*****Enter The Valid Food Name ******')
        removeFoodItem(foodMenu)


 
if __name__ =='__main__':
    main()