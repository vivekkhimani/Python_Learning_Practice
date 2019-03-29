def removevow(string1):
    newstring = ""
    vow_list = ['a','e','i','o','u']
    
    for letters in string1:
        if letters.lower() not in vow_list:
            newstring = newstring + letters
    return newstring

print (removevow("Vivek"))
            
        