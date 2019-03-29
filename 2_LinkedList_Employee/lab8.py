from birthday_prog import Birthday
hashtable = []

for i in range(12):
    hashtable.append([])
    
file_var = open("bdaylist.txt","r")

line_var = file_var.readlines()
tot_counter = 0
for lines in line_var:
    word_list = lines.split("/")
    
    
    day = int(word_list[0])
    month = int(word_list[1])
    year = int(word_list[2])
    my_object = Birthday(day,month,year)
    hash_value = hash(my_object)
    b_tuple = (my_object,lines)
        
        
        
    for lists in range(len(hashtable)):
        if lists == hash_value:
            hashtable[lists].append(b_tuple)
    tot_counter += 1
                
                
counter = 0                
for new_lists in hashtable:
    print("Hash location",counter,"has",len(new_lists),"elements.")
    counter+=1
    
    
print("Total Lines:",tot_counter)
            
    