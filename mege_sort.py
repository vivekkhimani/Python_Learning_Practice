#Merge_sort_module

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
        C.apppend(A[0])
        A.pop(0)
        
    while len(B)>0:
        C.append(B[0])
        B.pop(0)
    return C


