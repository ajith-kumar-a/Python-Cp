"""
country = ['India','south korea','iran','japan','turkey','iraq']

for name in country:
    print(f'{name.title()}')

auhtor_names = ('k k rowling','rachel aaron','verna aadrma')

for author_name in auhtor_names:
    print(f'{author_name.title()}')

"""
auhtor_names = ('k k rowling','rachel aaron','verna aadrma','hans aanrud')

for index in range(len(auhtor_names)):
    print(f'{index+1}. {auhtor_names[index].title()}')

# iterate ovr a string using loop
time_update = "it's 4.15pm"
for s in range(len(time_update)):
    print(time_update[s],end="")

