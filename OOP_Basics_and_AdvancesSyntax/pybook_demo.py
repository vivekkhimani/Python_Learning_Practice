import math
class Point:
    def reset(self):
        self.x = 0
        self.y = 0
    def move(self,x=0,y=0):
        self.x = x
        self.y = y
    def calc_distance(self,anotherpoint):
        return math.sqrt((self.x -anotherpoint.x)**2 + (self.y - anotherpoint.y)**2)
    

p1 = Point()
p2 = Point()

p1.reset()
p2.move(3,4)

print(p1.calc_distance(p2))
