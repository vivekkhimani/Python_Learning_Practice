def custom_split(user_string,target_char):
    counter=0
    newword=""
    L=[]
    while counter<len(user_string):
        if user_string[counter]==target_char:
            L.append(newword)
            newword=""
        else:
            newword=newword+user_string[counter]
        counter=counter+1
    L.append(newword)
    return L

x=input("Please enter any string:")
y=input("Please enter any one target character:")
print(custom_split(x,y))