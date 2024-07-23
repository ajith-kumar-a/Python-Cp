Watch_details = {
    'Titan': 8000,
    'Fasttrack':5000,
    'Omega':9000,
    'Titan':12000

}

# keys() -> returns a list containing the dicitionary's Key
key_method = Watch_details.keys()
print('key method: ',key_method)

value_method = Watch_details.values()
print('value method: ',value_method)

get_method = Watch_details.get('Titan')
print('get method: ',get_method)

item_method = Watch_details.items()
print('Item method :',item_method)

Watch_details.update({'new Watch':5000})
print('update method :',Watch_details)

Watch_details.pop('Omega')
print('update method :',Watch_details)



