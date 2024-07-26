

def checkSplletter(checkSplChar):
    special_Char = ['!','@','#','$','%','^','&','*','(',')','-','_','/','?','~',',','<','>','.',':',';','\'','\"','+','=','[',']','{','}']
    for ch in checkSplChar:
        if ch in special_Char:
            return False
        else:
            continue
    return checkSplChar    
      
def filterChar(id_string):

    end = len(id_string)
    start = id_string.find('-')

    id_string = id_string[start+1:end]
    ans = id_string

    return ans

def filter_list_dict(list_dict):
    list_dict.sort(key=lambda x : x['name'])



def main():
    name_list = [
    {'name':'shreya','age':15},
    {'name':'pratiksha','age':13},
    {'name':'prerna','age':15}
    ]

    # name_list.sorted()
    
    name_list.sort(key=lambda x : x['name'])
    print(name_list)

    filter_name = list(map(filter_list_dict,name_list))

    print(filter_name)

    product_id = ['HEM-234','HEM-123','HEM-566',]

    filter_id = list(map(filterChar,product_id))
    print('Filter id : ',filter_id)
    
    course = ['','Python','java',',,','angul:ar','php']

    filter_list = list(filter(checkSplletter,course))
    # print('Filter List : ',filter_list)

   

if __name__ == '__main__':
    main()



# course = ['','Python','java',',,','angular','php']