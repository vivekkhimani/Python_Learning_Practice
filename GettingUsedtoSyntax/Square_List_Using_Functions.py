def square_list(start,end):
    L=[]
    while start**2<=end**2:
        L.append(start**2)
        start+=1
    return L

x=int(input("Please enter a number you want to begin with:"))
y=int(input("Please enter an ending number:"))
print(square_list(x,y))
print(square_list(1,100))

            
        