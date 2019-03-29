def bubblesort(list1):
    #this is for the descending sorting
    temp = 0
    for i in range (0,len(list1)-1,1):
        for j in range (len(list1)-1):
            if list1[j] < list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
                
    return list1

myL = [12,1,5,3,2,11,8,15]
print (bubblesort(myL))