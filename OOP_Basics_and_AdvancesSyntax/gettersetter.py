class BankAccount:
    def __init__(self, name, balance=0.0): #constructor
        self.mylog("Account created")
        self.name = name
        self.balance = balance
    def getBalance(self):  #getter
        self.mylog("Your balance was checked at: "+str(self.balance))
        return self.balance
    def setBalance(self,newBalance):  #setter
        self.mylog("Your balance was changed to: "+str(newBalance))
        self.balance = newBalance
    def mylog(self,message):
        myFile = open("log.txt","a")
        print(message,file=myFile)
        myFile.close()
        
myAcct = BankAccount("Vivek Khimani",250.0)
myAcct.setBalance(900)
print(myAcct.getBalance())