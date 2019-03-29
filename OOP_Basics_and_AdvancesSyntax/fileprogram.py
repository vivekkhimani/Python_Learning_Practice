import sys
mybook = open("file1.txt")
dictionary = {}
for lines in mybook:
    word_list = lines.split()
    for word in word_list:
        letter = word[0]
        letter = letter.upper()
        if letter in dictionary.keys():
            dictionary[letter]+=1
        else:
            dictionary[letter]=1
mybook.close()

outfile = open("file2.txt","r+")
key_list = list(dictionary.keys())
key_list.sort()
newprint = ""
finalprint = ""
for key in key_list:
    newprint = "The number of words starting with " + str(key) + " is "
    if newprint in outfile:
        newprint += str(dictionary[key]) + ".\n"
        outfile.write(newprint)
        newprint = ""
    else:
        finalprint = "The number of words starting with " + str(key)+ " is "
        finalprint += str(dictionary[key]) + ".\n"
        outfile.write(finalprint)
        finalprint = ""
        
outfile.close()
    
