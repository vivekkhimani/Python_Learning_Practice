import math
print("Welcome to Predator-Prey Model.")

def bunnies (rabbits,foxes,years):
    
    if years == 0:
        return rabbits,foxes
    
    else:
        rabbits_finale = rabbits + math.floor(rabbits * (0.04-0.0005 * foxes))
        foxes_finale = foxes - math.floor(foxes * (0.2-0.00005 * rabbits))
        return bunnies(rabbits_finale,foxes_finale,years-1)
        
    
    
    
    
        
if __name__ == "__main__":
    rabbit_input = int(input("Enter Initial Rabbit Population:\n"))
    foxes_input = int(input("Enter Initial Fox Population:\n"))
    years_input = int(input("Enter Number of Years to Simulate:\n"))
    x,y = bunnies(rabbit_input,foxes_input,years_input)
    
    print("After",years_input,"years there will be",x,"rabbits.")
    print("After",years_input,"years there will be",y,"foxes.")