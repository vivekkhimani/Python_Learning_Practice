print("Welcome to Digit Flipper")
def rev(text):
    return text[::-1]
    
if __name__ == "__main__":
    user_input = input("Enter Some Text:\n")
    
    alpha_string = ""  
    string_for_reverse = ""
    new_string = ""
    
    word_list = user_input.split()
    
    for words in word_list:
        
        if words.isnumeric() == True:
            new_string += rev(words) + " "
        
        elif words.isalpha() == True:
            new_string += words + " "
            
        
        else:
            for chars in words:
                if chars.isalpha() == True:
                    new_string += rev(string_for_reverse)
                    string_for_reverse = ""
                    new_string += chars 
                    
                
                elif chars.isnumeric() == True:
                    string_for_reverse += chars
                    
                elif chars in [","," ","!","."]:
                    if words == word_list[-1]:
                        new_string += rev(string_for_reverse)
                        string_for_reverse = ""
                        new_string += chars
                        
                    else:
                        new_string += rev(string_for_reverse)
                        string_for_reverse = ""
                        new_string += chars + " "
                  
            new_string += rev(string_for_reverse) 
                
                
                
    print("Revised String:")
    print(new_string)
                    
        
    