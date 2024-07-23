# student_name = ["Ajith","Vijay","Prasandh","Sala"]
# student_id = [123,123,112]
# mixed_data = ['Ajith',123,True,78.9]  #Hetrogenus

# #Acces value
# #positive index
# print('Accessing value of list position element : ',student_name)


# # Creating a list
# # Creating same data type / Homogenus
# course = ['Python','Java','React']      #String
# rollNo = [111,112,113,114]              #Integer

# # Creating mixed type #heterogenus
# mixed_type = ['Ajith',222,True,67.78]   
# print('Hetrogenus :',mixed_type)
# print('Length :',len(mixed_type))

# # Positive Index
# print('Access value of 222 ',mixed_type[1])
# print('Access value of true ',mixed_type[2])
# print('Access value of 67.78 ',mixed_type[3])

# # Negative Index ->
# print('Access value of 222 ',mixed_type[-4])
# print('Access value of true ',mixed_type[-3])
# print('Access value of 67.78 ',mixed_type[-2])

# # Slicing : [start(include) : stop(excluded)]
# print('Slicing : ',mixed_type[1:3])

# print('Slicing : ',mixed_type[0:3])

# print('Slicing : ',mixed_type[-4:-1])

# Mutable (can change , add and delete )

fruits = ['Mango','Banana','Graphe','WaterMelon']
fruits[1] = 'Kiwi'
print('Using Index replacin banana with kiwi' ,fruits)
del fruits[3]
print('Removing WaterMelon ',fruits)

#slicing replaced Kiwi, Graph ->
fruits[1:3] = 'Banana','Orange'
print('Using Index replacin banana with kiwi' ,fruits)

