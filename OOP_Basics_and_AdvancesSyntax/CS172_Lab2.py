import datetime
disp_date = str(datetime.datetime.now())

class ItemClass:
    def __init__(self,name,price,taxable = True):
        self.__name = name
        self.__price = price
        self.__taxable = taxable
        
    def __str__(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getTax(self,tax_rate):
        return self.__price * (tax_rate/100)
    
    
class ReceiptClass:
    def __init__(self,supp_taxrate = 12):
        self.__taxrate = ItemClass.getTax(supp_taxrate)
        self.__purchases = []
        
    def __str__(self):
        return "Hello"
    
    def addItems(self):
        self.__purchases.append(self)
        

print ("Welcome to the Receipt Creator.")
add_item = ""
while add_item.lower() != "no":
    item_name = input("Please enter the item name.")
    ReceiptClass.addItems(item_name)
    item_price = float(input("Enter item price."))
    taxable_info = input("Is the item taxable? (y/n)")
    if taxable_info.lower() == "y":
        newObject1 = ItemClass(item_name,item_price)
    else:
        newObject1 = ItemClass(item_name,item_price,False)
        
   
    
            
        
    
        
    