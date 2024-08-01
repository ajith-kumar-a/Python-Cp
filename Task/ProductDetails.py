# product ->id auto, name , price , desc 
# getdetails
# addproduct


class Product:

    pId = 0
    def __init__(self):
        self._pname = ""
        self._price = ""
        self._desc = ""
        Product.pId += 1
        self.__id = Product.pId
        

    def getProductDetails(self):

        if self._pname != "" or self._price != "" or self._desc != "":

            print(f'Product Id \t: {self.__id}')
            print(f'Product Name \t: {self._pname}')
            print(f'{self._pname} Price \t: {self._price}')
            print(f'{self._pname} Description  \t: {self._desc}')
        else :
            raise Exception("Error, Before Get Details You need Add Product Details")


    def addProcuct(self):
        try: 
            name = input("Enter Product Name : ")
            price = int(input(f"Enter {name} Price : "))
            desc = input(f'Enter {name} Description : ')
        
            self._pname = name
            self._desc = desc
            self._price = price
            print(f'{name} Added Sucessfully \n')
        except ValueError as e:
            print(f'Error ,{e}')
        except Exception as e:
            print(f'Error , {e}')



p1 = Product()
p1.addProcuct()
p1.getProductDetails()

print("*"* 70)
p2 = Product()
p2.addProcuct()
p2.getProductDetails()