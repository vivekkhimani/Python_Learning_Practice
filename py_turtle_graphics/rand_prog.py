import secrets

secrets.SystemRandom().seed(28)
myFile = open("random_numbers.txt","w")

for i in range(0,1000):
    myFile.write(str(secrets.SystemRandom().randint(1,25)))
    myFile.write("\n")
myFile.close()
