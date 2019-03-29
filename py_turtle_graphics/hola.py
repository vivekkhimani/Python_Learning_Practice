print("Welcome to Two's Complement Creator")
binary_input = input("Enter a Binary Value:\n")

two_compl = ""
for bits in binary_input:
    if str(bits) == "0":
        two_compl = two_compl + "1"
        
    elif str(bits) == "1":
        two_compl = two_compl + "0"

final_two = ""  
final_two_reverse = ""
    

for chars in two_compl[::-1]:
    if chars == "1":
        final_two_reverse += "0"
            
    elif chars == "0":
        final_two_reverse += "1"
        break

display_range = len(two_compl) - len(final_two_reverse)
final_two = two_compl[:display_range] + final_two_reverse[::-1]
print("In Two\'s Complement:\n"+str(final_two))
            
            
        
    
                
                
 
            
            
        
    
                
                