# Watch_details = {
#     'Titan': 8000,
#     'Fasttrack':5000,
#     'Omega':9000,
#     'Titan':12000

# }
# # Titan consider the latest key

# print(f'length of watch is  {len(Watch_details)},and type is {type(Watch_details)}')
# print('Using key ',Watch_details['Titan'])


# for watch in Watch_details:
#     print(f'{watch}:{Watch_details[watch]}')

# Watch_details = {
#     'Titan': 8000,
#     'Fasttrack':5000,
#     'Omega':9000,
#     'Rolex':8000
# }

# print(f'length of watch is  {len(Watch_details)},and type is {type(Watch_details)}')
# print('Using key ',Watch_details['Titan'])
# Watch_details['Cartier'] = 6000
# Watch_details['Rolex'] = 20000

# for watch in Watch_details:
#     print(f'{watch}:{Watch_details[watch]}')


# # Create a dict of food iteam
# food = {
#     'Somosa':10,
#     'Vada':10,
#     'Pani puri':25,
#     'Kachori':15
# }

# food['Pani puri'] = 30
# food['Kachori'] = 20
# food['Pav Baji'] = 35

# print(food)

users = {
    'Ajithbag' : {
        'firstname' :'Ajith',
        'lastname' : 'Kumar',
        'location' : 'chennai'
    },
     'Kumarbag' : {
        'firstname' :'kumar',
        'lastname' : 'A',
        'location' : 'kattankulathur'
    },
    'Ajibag' : {
        'firstname' :'Aji',
        'lastname' : 'A',
        'location' : 'kattankulathur'
    }
}


for user in users:
    print(f'{user}:{users[user]}')
    
aji = users['Ajibag']
print(aji['firstname'])
print(aji['location'])


