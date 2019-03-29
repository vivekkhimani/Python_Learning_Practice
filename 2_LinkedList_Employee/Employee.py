class Employee:
    def __init__(self,emp_id, hours_pay = 0, week_hours = 0):
        self.__id = emp_id
        self.__hours = week_hours
        self.__pay = hours_pay
        self.__gross = self.__hours * self.__pay
        
    def setWeekHours(self,wh):
        self.__hours = wh
        
    def setHoursPay(self,p):
        self.__pay = p
        
    def getID(self):
        return self.__id
    
    def getWeekHours(self):
        return self.__hours
    
    def getWeekPay(self):
        return self.__pay
    
    def getGross(self):
        return self.__hours * self.__pay
    
    def setGross(self,other):
        self.__gross = other
    
    def __str__(self):
         return "***PAYROLL*** \n Employee ID:  " + self.__empid + "\n Hourly Rate:  " + str(self.__hourlyrate) + "\n Hourse Worked:  " + str(self.__hours) + "\n Gross Wages:  " + str(self.__grosswages)
        
        