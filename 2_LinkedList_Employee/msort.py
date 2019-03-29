def merge(A,B):
    C = []
    while len(A)>0 and len(B)>0:
        if A[0] < B[0]:
            C.append(A[0])
            A.pop(0)
            
        else:
            C.append(B[0])
            B.pop(0)
            
    
    while len(A)>0:
        C.append(A[0])
        A.pop(0)
        
    while len(B)>0:
        C.append(B[0])
        B.pop(0)
    return C


def msort(X):
    if len(X) > 1:
        middle = len(X)//2
        A = msort(X[:middle])
        B = msort(X[middle:])
        C = merge(A,B)
        
        return C

    else:
        return X
        
        
if __name__ == "__main__":
    import random
    for x in range(0, 10):
        L = [random.randint(0,100) for k in range(0,10)]
        print ("Merge Input:",L)
        L = msort(L)
        print ("Results after Merge Sort:",L)