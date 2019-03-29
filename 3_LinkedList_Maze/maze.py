from rooms import Room
class MyMaze(Room):
    def __init__ (self, st= None, ex = None):
        self.__start = st
        self.__exit = ex
        self.__current = st
        
    def getCurrent(self):
        return self.__current
    
    def moveNorth(self):
        if self.getNorth() == None:
            return False
        else:
            self.__current = self.getNorth()
            return True
            
    def moveSouth(self):
        if self.getSouth() == None:
            return False
        else:
            self.__current = self.getSouth()
            return True
        
    def moveWest(self):
        if self.getWest() == None:
            return False
        else:
            self.__current = self.getWest()
            return True
    
    def moveEast(self):
        if self.getEast() == None:
            return False
        else:
            self.__current = self.getEast()
            return True
        
    def atExit(self):
        if self.__current == self.__exit:
            return True
        else:
            return False
        
    def reset(self):
        self.__current == self.__start
        
        
            
            