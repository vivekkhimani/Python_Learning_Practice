class Birthday:
    def __init__(self,day,month,year):
        self.__bday = day
        self.__bmonth = month
        self.__byear = year
        
    def __str__(self):
        return str(self.__bmonth) + " / " + str(self.__bday) + " / " + str(self.__byear)
     
    def __hash__(self):
        ret_value = (self.__bday+self.__bmonth+self.__byear) % 12
        return ret_value
    
    
    def __eq__(self,other):
        if self.__bday == other.__bday and self.__bmonth == other.__bmonth and self.__byear == other.__byear:
            return True
        else:
            return False
        
if __name__ == "__main__":
    test_object = Birthday(7,4,2000)
    
    print (test_object)
    
    
    my_dic = {}
    
    my_dic[test_object] = Birthday(7,4,2000)
    
    print(hash(test_object))
    
    
    
    
    
    
        