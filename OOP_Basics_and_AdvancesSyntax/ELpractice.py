class EnglishLength:
    def __init__(self, yards=0, feet=0, inches=0):
        self.__yards = yards + feet//3
        self.__feets = feet + inches//12
        self.__inches = inches%12
        self.__feets%=3
        
    def __add__ (self,other):
        return (self.__inches + other.__inches, self.__yards + other.__yards, self.__feets + other.__feets)
    
test1 = EnglishLength(25,15,14)
test2 = EnglishLength(30,15,14)
print(test1.__add__(test2))
        