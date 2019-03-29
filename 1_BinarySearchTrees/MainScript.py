import random

def populate(n):
    L = []
    
    
    for i in range(0,n):
        rand_num = random.randint(0,n)
        L.append(rand_num)
        
    return L

def another_fun(L1,n1):
    ret_value = False
    for x in range(0,len(L1)):
        if n1 == L1[x]:
            ret_value = True
            break
    
    return ret_value

my_list = populate(55)

counter = 0
for i in range(0,len(my_list)):
    counter+=1
    
print(counter)
    
    
        