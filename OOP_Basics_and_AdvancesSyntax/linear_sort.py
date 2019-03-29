myL = [2,4,6,9,10]
x = 0
y = int(input("Enter the element you want to search for: "))
while x<len(myL):
    if y == myL[x]:
        print (y,"is",x+1,"th element in the list.")
        break
    
    elif x == (len(myL)-1):
        print ("Not Found")
        break
    
    else:
        x = x+1
    
    