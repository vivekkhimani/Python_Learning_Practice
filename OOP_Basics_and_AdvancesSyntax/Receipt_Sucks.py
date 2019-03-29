import datetime

class Item_Class:
    def __init__(self, item_name, item_price = 0.0, item_tax = True):
        self.__name = item_name
        self.__price = item_price
        self.__taxable = item_tax
        
    def __str__ (self):
        return self.__name     
    
    def getPrice (self):
        return self.__price
    
    def getTax(self,taxrate):
        return ((self.__price * taxrate)/100)
    
    
class Receipt_Class (Item_Class):
    def __init__ (self,tax1rate,listofitems):
        self.__tax_rate = tax1rate
        self.__purchases = listofitems
        
    def __str__ (self):
        line1_string = "Receipt " + str(datetime.datetime.now())
        string1 = ""
        subtotal = 0
        taxtotal = 0
        for items in self.__purchases:
            string1 = string1 + str(items) + "          " + str(items.getPrice()) + "\n"
            subtotal = subtotal + items.getPrice()
            if items._Item_Class__taxable == True:
                taxtotal = taxtotal  + items.getTax(self.__tax_rate)
            else:
                pass
        overall_total = subtotal + taxtotal
        
        return line1_string + "\n" + string1 + "\n" + str(subtotal) + "\n" + str(taxtotal) + "\n" + str(overall_total)
    
    
    def addItem (self,newitem):
        self.__purchases.append (newitem)    #FIX_IT
        
        

print ("Welcome to the Receipt Generator")
add_item_or_not = ""
user_boolean = True
item_list = []

while add_item_or_not.lower() != "n":
    user_input = input("Please enter the name of the item.")
    user_price = float(input("Please enter the price of the item."))
    user_taxable = input ("Please enter \"y\" if the item is taxable, \"no\" otherwise.")
    if user_taxable.lower() == "y":
        user_boolean = True
    else:
        user_boolean = False
        
    item_class_object = Item_Class (user_input,user_price,user_boolean)
    item_list.append(item_class_object)
    add_item_or_not = input("Do you want to add another item? \"y\" or \"n\"?")
                
new_receipt_object = Receipt_Class (25,item_list)
print (str(new_receipt_object))
    


        
