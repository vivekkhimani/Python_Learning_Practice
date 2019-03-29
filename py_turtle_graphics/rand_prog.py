import random
random.seed(28)
myFile = open("random_numbers.txt","w")

for i in range(0,1000):
    myFile.write(str(random.randint(1,25)))
    myFile.write("\n")
myFile.close()