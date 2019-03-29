from Node import Node

class BST:
    
    def __init__(self):
        self.__root = None
        
    def isEmpty(self):
        return self.__root == None
    
    def insertNodes(self,other):
        
        new_node = Node()
        