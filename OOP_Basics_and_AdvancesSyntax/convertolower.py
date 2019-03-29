def conversion (string1):
    counter = 0
    var_convert = 0
    newstring = ""
    while counter<len(string1):
        if 65<=ord(string1[counter])<=90:
            var_convert = ord(string1[counter]) + 32
            newstring = newstring + chr(var_convert)
        else:
            newstring = newstring + string1[counter]
            
        counter = counter + 1
    return newstring

x = input("Please enter something.")
print (conversion(x))