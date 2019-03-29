class MyClass(object):
    def __init__(self,name,email):
        self.__name = name
        self.__email = email
        
    def fuckOff(self):
        return "Fucker"

class YourClass(MyClass):
    def __init__(self):
        self.__name = "Vivek"
    

vivek = MyClass("Vivek","Khimani")

print(isinstance(vivek,YourClass))