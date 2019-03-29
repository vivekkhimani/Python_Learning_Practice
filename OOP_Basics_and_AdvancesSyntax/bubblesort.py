def bubblesort (list1):
    temp = 0
    #this code is implemented for ascending sort
    
    for i in range(len(list1)-1,0,-1):
        for j in range (i):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
                
                
        
    return list1


myL = [2,4,10,64,52,14,18,25]
print (bubblesort(myL))
            
            
        
        