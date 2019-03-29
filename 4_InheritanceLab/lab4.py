#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

from hamster import *
import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

	#first reset everyone's health!
	#####TODO######

	#next print out who is battling
	print("Starting Battle Between")
	print(m1.getName()+": "+m1.getDescription())
	print(m2.getName()+": "+m2.getDescription())
	
	
	#Whose turn is it?
	attacker = None
	defender = None
	
	#Select Randomly whether m1 or m2 is the initial attacker
	#to other is the initial definder
	######TODO######
	
	
	print(attacker.getName()+" goes first.")
	#Loop until either 1 is unconscious or timeout
	while( m1.getHealth() > 0 and m2.getHealth() > 0):
		#Determine what move the monster makes
		#Probabilities:
		#	60% chance of standard attack
		#	20% chance of defense move
		#	20% chance of special attack move

		#Pick a number between 1 and 100
		move = random.randint(1,100)
		#It will be nice for output to record the damage done
		before_health=defender.getHealth()
		
		#for each of these options, apply the appropriate attack and 
		#print out who did what attack on whom
		if( move >=1 and move <= 60):
			#Attacker uses basic attack on defender
			######TODO######
		elif move>=61 and move <= 80:
			#Defend!
			######TODO######
		else:
			#Special Attack!
			######TODO######
		
		#Swap attacker and defender
		######TODO######
		
		#Print the names and healths after this round
		######TODO######
		
	#Return who won
	######TODO######

#----------------------------------------------------
if __name__=="__main__":
	#Every battle should be different, so we need to
	#start the random number generator somewhere "random".
	#With no input Python will set the seed
	
	random.seed(0)
	first = hamster("Periwinkle")
	second = hamster("Cilantro")
	
	winner = monster_battle(first,second)
	
	#Print out who won
	####TODO####
	