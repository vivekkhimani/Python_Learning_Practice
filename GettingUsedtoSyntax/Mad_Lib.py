import sys
user_inp=input("Please enter the file you want to open")
try:
    file=open(user_inp,"r")
except FileNotFoundError:
    print("Bad File Name Sorry.")
    sys.exit()
story=""
for line in file:
    word_list=word.split()
    for word in word_list:
        if word[0]=="[":
            last=word.find("]")
            q=word[1:last]
            q=q.replace("-"," ")
            after=word[(last+1):]
            if q[0] in "aeiou":
                article="an"
            else:
                article="a"
            print("Please give",article,q)
            blank=input()
            story+=blank+after+" "
        else:
            story+=word+" "
file.close()
print("Here's your story:\n")
print("------------------\n")
print(story)