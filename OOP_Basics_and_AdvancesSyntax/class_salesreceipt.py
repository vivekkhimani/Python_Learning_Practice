class SalesReceipt:
    def __init__(self):
        self.itemname = '[no name]'
        self.itemprice = 0
        self.tax = "yes"
        self.addit = "yes"
        
    def item_name(self,ItemName):
        self.itemname = ItemName
        return self.itemname
    def item_price(self,ItemPrice):
        self.itemprice = ItemPrice
        return self.itemprice
    def taxation(self,Tax):
        self.tax = Tax
        return self.tax
    def addition1(self,Add):
        self.addit = Add
        return self.addit
    
MyReceipt = SalesReceipt()


nameprint = ""
priceprint = 0
texansprint = ""
addansprint = ""

while name1.lower != "exit":
    name1 = input ("Please enter the item name.")
    nameprint = nameprint + name1 + "\n"

    price1 = int(input("Please enter the item price."))
    priceprint = priceprint + price1
    
    texans = input("Pleas answer yes or no for taxation.")

    addans = input ("Please answer yes or no to add.")
    
print("****RECEIPT****")
print(MyReceipt.item_name(nameprint))
print(MyReceipt.item_price(priceprint))
print(MyReceipt.taxation(texans))
print(MyReceipt.addition1(addans))

        
        
        
        