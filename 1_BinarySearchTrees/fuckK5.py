def SelectionSort(numbers):
    for i in range(len(numbers)-1):
        index_small = i
        
        for j in range(i+1,len(numbers)):
            if numbers[j] < numbers[index_small]:
                index_small = j
                
        
        temp = numbers[i]
        numbers[i] = numbers[index_small]
        numbers[index_small] = temp
        
    print(numbers)
        
SelectionSort([2,4,15,1])