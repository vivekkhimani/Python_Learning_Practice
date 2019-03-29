def mystery(num_list):
    num_list.sort()
    if len(num_list) == 1:
        return num_list[0]
    
    else:
        return mystery(num_list[1:])
    
print(mystery([5,4,9,15,2]))
        