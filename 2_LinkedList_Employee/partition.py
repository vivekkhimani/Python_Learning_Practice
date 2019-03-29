def partition(A,start,stop):
    pivot = A[stop]
    i = start
    
    for j in range(start,stop):
        if A[j] <= pivot:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i+=1
            
    temp = A[stop]
    A[stop] = A[i]
    A[i] = temp
    
    return i


def qsort(A,start,stop):
    if start<stop:
        p = partition(A,start,stop)
        qsort(A,start,p-1)
        qsort(A,p+1,stop)
        

if __name__ == "__main__":
    import random
    for x in range(0,10):
        L = [random.randint(0,100) for k in range(0,10)]
        print("Quick Sort Input:",L)
        qsort(L,0,len(L)-1)
        print("Results after Sort:",L)