import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
        
    def getRadius (self):
        return self.__radius
    
    def setRadius (self, newRadius):
        self.__radius = newRadius
        
    def area(self):
        return math.pi * (self.__radius**2)
    
    def __add__(self, anothercircle):
        return Circle(self.__radius + anothercircle.__radius)
    
newObject = Circle (50)
print (newObject.getRadius())
newObject.setRadius(100)
print (newObject.getRadius())
newObject1 = Circle (100)

newObject3 = newObject + newObject1
print(newObject3.getRadius())
