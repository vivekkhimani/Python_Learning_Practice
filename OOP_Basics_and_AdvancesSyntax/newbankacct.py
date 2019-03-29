class NewBank:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance
        
    def getBalance(self):
        self.mylog ("Balance was checked at: " + str(self.balance))
        return self.balance
    
    def deposit(self,amount):
        self.mylog("The amount deposited: " + str(amount))
        self.balance = self.balance + amount
        self.mylog("Amount after deposit: " + str(self.balance))
        print("Amount after deposit: " + str(self.balance))
        
    def withdraw(self,amount1):
        try:
            self.mylog("The amount withdrawn: " + str(amount1))
            self.balance = self.balance - withdraw
            self.mylog("The amount remaining: " + str(self.balance))
            print("The remaining amount: " + str(self.balance))
            valid = True
        except:
            print ("Insufficient Funds. Try again.")
                
    def mylog(self,message):
        myFile = open ("log.txt","a")
        print(message,file=myFile)
        myFile.close()
        
NewAcct = NewBank("Vivek Khimani", 1000)
NewAcct.deposit(1000)
print(NewAcct.getBalance())
NewAcct.withdraw(2500)
                        