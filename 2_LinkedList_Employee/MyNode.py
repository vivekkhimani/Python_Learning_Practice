from employee import Employee
class MyNode:
    def __init__(self,data,next1 = None):
        self.__data = data
        self.__next = next1
        
    def getNext(self):
        return self.__next
    
    def setNext(self,other):
        self.__next = other
        
    def getData(self):
        return self.__data
    
    def setData(self,other1):
        self.__data = other1
        
        