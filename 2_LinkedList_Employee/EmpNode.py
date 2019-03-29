class MyNode:
    def __init__(self, data, next1 = None):
        self.__data = data
        self.__next = next1
        
    def getNext(self):
        return self.__next
    
    def getData(self):
        return self.__data
    
    def setNext(self,other):
        self.__next = other
        
    def setData(self,d):
        self.__data = d
        
    def __str__(self):
        return str(self.__data) + " whose next node is " + str(self.__next)
    
    