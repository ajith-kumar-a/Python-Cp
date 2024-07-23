menu_card = ['Panner','Dal','Rice','Rice']

print('Available Items in Menu Card :',menu_card)
#append() --> Adds an element at the end of the list

menu_card.append('Kofta')
print('After using append method in  Menu Card :',menu_card)

# Dal Tadka , Biriyani
# Extend() --> Add the element of a list (or iterable) to the end
menu_card.extend(['Dal Tadka','Biriyani'])
print('After using extend method in  Menu Card :',menu_card)

# Insert --> Adds an element to the specific positon
menu_card.insert(1,'Mutton Biriyani')
print('After using insert method in  Menu Card :',menu_card)

# Remove() --> it will remove specified value
menu_card.remove('Dal Tadka')
print('After using remove method in  Menu Card :',menu_card)

# pop() method --> remove element from specific position
menu_card.pop(2)
print('After using pop method in  Menu Card :',menu_card)


# index method
index_method = menu_card.index('Rice')
print('index position :',index_method)

# sort method
menu_card.sort()
print('sort position :',menu_card)

