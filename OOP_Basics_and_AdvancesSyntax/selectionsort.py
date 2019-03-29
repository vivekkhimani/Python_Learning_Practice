def selectionsort (list1):
    temp = 0
    for i in range (0,len(list1)-1):
        max_possible = i
        for j in range (i,len(list1)):
            if list1[j] > list1[max_possible]:
                temp = list1[max_possible]
                list1[max_possible] = list1[j]
                list1[j] = temp
                
    return list1

myL = [1,5,36,25,14,9,52,41]
print (selectionsort(myL))
                