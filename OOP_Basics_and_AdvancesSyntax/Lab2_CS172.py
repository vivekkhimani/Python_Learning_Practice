import datetime
display_date = str(datetime.datetime.now())

class ItemClass:
    def __init__(self, name, price, tax):
        self.__name = name
        self.__price = price
        self.__taxable = tax
        
    def __str__(self):
        return str(self.__name)
    
    def getPrice(self):
        return self.__price
    
    def getTax(self,tax_rate):
        tax_charged = self.__price * (tax_rate/100)
        return float(tax_charged)

class Receipt:
    tax_sum = 0
    price_without_tax = 0
    total = 0
    def __init__(self, tax1_rate, itemsobject):
        self.__tax_rate = tax1_rate
        self.__purchases = itemsobject
        
    def __str__(self):
        for products in self.__purchases:
            price_without_tax = price_without_tax + products.getPrice()
            if products.self.__taxable == True:
                tax_sum = tax_sum + products.getTax(self.__tax_rate)
            total = price_without_tax + tax_sum
            return str(products.__str__()) + "--------------------" + "{:.2f}".format(products.getPrice())
        return "Subtotal --------------------" + "{:.2f}".format(price_without_tax)
        return "Tax --------------------" + "{:.2f}".format(tax_sum)
        return "Total --------------------" + "{:.2f}".format(total)
           
    def  addItem(itemname):
        print("Hi")
        

print ("***WELCOME TO THE RECEIPT CREATOR***")

add_more = ""
my_tax = True
receipt_items = []

while add_more.upper() != "NO":
    my_item = input("Please enter the name of your item.\n")
    receipt_items.append(my_item)
    my_price = float(input("Please enter the price of that item.\n"))
    is_taxable = input("Is your item taxable? (y/n)")
    if is_taxable.lower() == "y":
        my_tax = True
    else:
        my_tax = False
        
    new_item_obj = ItemClass(my_item,my_price,my_tax)
    receipt_items.append(new_item_obj)
    
    add_more = input("Do you want to add more item? (yes/no)")
    if add_more.upper() == "NO":
        new_receipt_obj = Receipt (25,receipt_items)
        print (new_receipt_obj)
                
            
            
        
        
    