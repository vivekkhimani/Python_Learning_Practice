import sys
try:
    story = open ("file1.txt")
    dictionary = {}
    for lines in story:
        word_list = lines.split()
        for words in word_list:
            letter = words [0]
            letter = letter.upper()
            if letter in dictionary.keys():
                dictionary[letter]+=1
            else:
                dictionary[letter]=1
except FileNotFoundError as e:
    print("File not found")
    
story.close()
print(dictionary)
    