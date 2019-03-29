class Node:
    
    def __init__(self,data = None, leftlink = None, rightlink = None):
        self.__data = data
        self.__left = leftlink
        self.__right = rightlink
        
    def getData(self):
        return self.__data
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def setLeft(self,left1):
        self.__left = left1
        
    def setRight(self,right1):
        self.__right = right1
        
