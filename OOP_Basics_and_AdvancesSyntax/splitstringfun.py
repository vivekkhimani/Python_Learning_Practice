def stringsplit (mystring, target = " "):
    pos = 0
    word = ""
    L=[]
    while pos < len(mystring):
        if mystring[pos] == target:
            L.append(word)
            word = ""
        else:
            word = word + mystring[pos]
        pos = pos + 1
    L.append(word)        
    return L

example = "I am Vivek"
print (stringsplit(example))