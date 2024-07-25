#  using list comprehension creating a list of square numbers

new_list = [i for i in range(1,11)]
print('List Comprehsion : ',new_list)

new_list = [i for i in range(1,11) if(i%2 == 0)]
print('List Compresion : ',new_list)

vowel = ['a','e,','i','o','u']
name = 'Ajith Kumar A'

vowel_list = [i for i in name if i in vowel]
print(vowel_list)