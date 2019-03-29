def readinput(question):
    valid = False
    while valid == False:
        try:
            x = input (question)
            x = int(x)
            valid = True
            return x
        except ValueError as e:
            print ("Please enter a valid number.")
            
            
readinput("Hi enter")