x=input("Please keep on entering the number. We'll stop when you'll enter stop")
L=[]
while x.lower()!="stop":
    try:
        x=int(x)
        L.append(x)
        x=input("Enter the next number")
    except ValueError as e:
        print ("Error:",e)
        print("Please enter a valid number or stop")
        x=input()
print("Your List:",L)
print("Minimum Number:",min(L))
print("Maximum Number:",max(L))
print("Average:",sum(L)/len(L))
        