import math
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setXY(self, newX, newY):
        self.__x = newX
        self.__y = newY
    def printxy(self):
        print ("The value of X is",str(self.__x),"and the value of Y is",str(self.__y))
    def reset(self):
        self.__x = 0
        self.__y = 0
    def distance(self,another):
        return math.sqrt(((self.getX() - another.getX())**2) + ((self.getY() + another.getY())**2))
    
newobj = Point(2,5)
anotherobj = Point(1,2)
print ("Get X:",str(newobj.getX()))
print ("Get Y: ",str(newobj.getY()))
print (newobj.distance(anotherobj))