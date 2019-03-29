def listofsquares():
    L = []
    valid = False
    while valid == False:
        try:
            x = input("Please enter the first number.")
            x = int(x)
            y = input("Please enter the last number.")
            y = int(y)
            for a in range (x,y+1):
                L.append(a*a)
            valid = True
            return L
        except ValueError as e:
            print("Please enter a number and try again.")
            
print1 = listofsquares()
print (print1)
                
         
            