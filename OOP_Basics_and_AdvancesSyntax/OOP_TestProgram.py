class MyClass:
    def __init__(self, firstname = "Vivek", lastname = "Khimani"):
        self.name1 = firstname
        self.name2 = lastname
        
    def getName (self,age):
        self.name2 = age
        return self.name1
    
    
myObject = MyClass("Bhargav","Khimani")

print(myObject.name1)
print(myObject.name2)

print (myObject.getName("25"))