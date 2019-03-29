#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172


#This class defines a generic monster
#It doesn't actually DO anything.
#It just gives you a template for how a monster works.

#We can make any number of monsters and have them fight
#they just all need to INHERIT from this one so that work the same way

#Since this class is not intended to be used
#none of the methods do anything
#This class is cannot be used by itself.
import abc

class monster(metaclass=abc.ABCMeta):
	def __init__(self):
		return
	def __str__(self):
		return "Generic Monster Class"
	#Methods that need to be implemented
	#The description is printed at the start to give
	#additional details
	
	#Name the monster we are fighting
	#The description is printed at the start to give
	#additional details
	@abc.abstractmethod
	def getName(self):
		pass
		
	@abc.abstractmethod
	def getDescription(self):
		pass
		
	#Basic Attack Move
	#This will be the most common attack the monster makes
	#You are passed the monster you are fighting
	@abc.abstractmethod
	def basicAttack(self,enemy):
		pass
		
	#Print the name of the attack used
	@abc.abstractmethod
	def basicName(self):
		pass
		
	#Defense Move
	#This move is used less frequently to
	#let the monster defend itself
	@abc.abstractmethod
	def defenseAttack(self,enemy):
		pass
		
	#Print out the name of the attack used
	@abc.abstractmethod
	def defenseName(self):
		pass
		
	#Special Attack
	#This move is used less frequently
	#but is the most powerful move the monster has
	@abc.abstractmethod
	def specialAttack(self,enemy):
		pass
		
	@abc.abstractmethod
	def specialName(self):
		pass
		
	#Health Management
	#A monster at health <= 0 is unconscious
	#This returns the current health level
	@abc.abstractmethod
	def getHealth(self):
		pass
		
	#This function is used by the other monster to
	#either do damage (positive int) or heal (negative int)
	@abc.abstractmethod
	def doDamage(self,damage):
		pass
		
	#Reset Health for next match
	@abc.abstractmethod
	def resetHealth(self):
		pass
	    
	    
class m1 (monster):
    def __init__(self):
        self.name = "MonsterVivek"
        self.description = "VIVEK is the most dangerous monster"
        self.health = 100
    
    def getName (self):
        return self.name
    
    def getDescription (self):
        return self.description
    
    def basicAttack (self,enemy):
        enemy.health = enemy.health - 2
        #FixReturn
    
    def basicName (self):
        return "Vivek Basic Attack"
    
    def defenseAttack (self,enemy):
        enemy.health = enemy.health
        #FixReturn
    
    def defenseName (self):
        return "Vivek Defense Attack"
    
    def specialAttack (self,enemy):
        enemy.health = enemy.health - 5
    
    def specialName (self):
        return "Vivek Special Attack"
    
    def doDamage (self,damage):
        
    
    
        
    
    
    

