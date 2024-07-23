company = {'Infosys','Changepond','Tcs'}
add_company = {'Newt Global','Vecton Solution','Tcs'}

# Union method
union_method = company.union(add_company)
print('Union method will return all the element in both set',union_method)
print()

union_method = company | add_company
print('Union Operator',union_method)
print()

intersection_method = company.intersection(add_company)   # using operator for intersection &
print('Intersection method will return Common Element ',intersection_method)
print()

difference_method = company.difference(add_company)
print('Difference method ',difference_method)


difference_method = add_company.difference(company)
print('Difference method ',difference_method)

# symmetric difference 
sym_difference = company.symmetric_difference(add_company)
print('Difference method ',sym_difference)
