# Create a tuple 
# Homogenus

student_id = (1,2,3,4,5,6)
ice_creame = ('Vanilla','Choco-chips','Blueberry')

# Hetrogenus
mixed_type = (123,'Hello',False,56.78)


print("length of student id ",len(student_id))
print("Blueberry",ice_creame[2])
print("False ",mixed_type[-2])
print("'Hello',False",mixed_type[1:3])


ice_creame = ('Vanilla')        # str
print(ice_creame,type(ice_creame))
ice_creame = ('Vanilla',)       # comma (tuple)
print(ice_creame,type(ice_creame))

# immutable
# mixed_type[0] = True
# print("False ",mixed_type)

ice_creame = ('Vanilla','Choco-chips','Blueberry','Vanilla')

# COUNT METHOD 
countmethod = ice_creame.count('Vanilla')
print(countmethod)

indexmethod = ice_creame.index('Vanilla')
print(indexmethod)