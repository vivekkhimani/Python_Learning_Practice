from MyNode import MyNode as Node
from employee import Employee

class LinkedList(Node):
    def __init__(self):
        self.__head = None
        
    def isEmpty(self):
        return self.__head == None
        
    def AddNewMethod(self,data):
        newNode = Node(data)
        
        if self.isEmpty() == True:
            self.__head = newNode
            
        else:
            current = self.__head
            
            while current.getNext() != None:
                current = current.getNext()
                
            current.setNext(newNode)
            
        
    def WeeklyWages(self):
        
        current = self.__head
        
        if self.isEmpty() == True:
            return "No Employee"
        
        else:
            current = self.__head
            
            while current.getNext() != None:
                emp_object = current.getData()
                my_id = emp_object.getID()
                input_quest = "Input number of hours for " + my_id
                hours_data = int(input(input_quest))
                emp_object.setWeekHours(hours_data)
                gross_value = emp_object.getGross()
                emp_object.setGross(gross_value)
                current = current.getNext()
                
    
    def DisplayPayroll(self):          #DisplayPayroll
        
        if self.isEmpty() == True:
            print("No Employee")
        
        else:
            current = self.__head
            
            while current.getNext() != None:
                emp_object = current.getData()
                print(emp_object)
                current = current.getNext()
                
    def HourlyRate(self,iddata,rateupdate):
        
        if self.isEmpty() == True:
            return "No Employee"
        
        else:
            current = self.__head
            
            while current.getNext() != None:
                emp_object = current.getData()
                if iddata == emp_object.getID():
                    emp_object.setHoursPay(rateupdate)
                    break
                else:
                    current = current.getNext()
                    
    
    def EmpRemove(self,emp_id_data):
        
        if self.isEmpty() == True:
            return "No Employee"
        
        else:
            current = self.__head
            
            while current.getNext() != None:
                emp_object = current.getData()
                if emp_object.getID() == emp_id_data:
                    current.setData(None)
                    break
                    
                else:
                    current = current.getNext()
                