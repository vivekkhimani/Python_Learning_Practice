from EmpNode import MyNode
class LinkedList(MyNode):
    
    def __init__(self,head = None):
        self.__head = head
        
    def isEmpty(self):
        return self.__head == None
        
    def AddNew(self,data):
        myNode = MyNode(data)
        
        if self.isEmpty() == True:
            self.__head = myNode
            
        else:
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
                
            current.setNext(myNode)
            
    def WeeklyWages(self,numhours):
        
        
        