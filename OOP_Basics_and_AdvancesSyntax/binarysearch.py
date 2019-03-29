def binarysearch(list1,x):
    lower = 0
    upper = len(list1)-1
    while lower <= upper:
        mid = (lower + upper) // 2
        if list1[mid] == x:
            return "Found at "+str(mid)+" position."
            break
        
        elif x > list1[mid]:
            lower = mid+1
            
        elif x < list1[mid]:
            upper = mid-1
            
        
 
myL = [1,5,9,15,25,27,39,69,85,94,95,97,98,99]
y = int(input("Enter the element you want to search for."))

if binarysearch(myL,y) == None:
    print ("Not Found")
    
       
print(binarysearch(myL,y))