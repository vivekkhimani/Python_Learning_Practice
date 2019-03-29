import sys
ori_story = open ("file1.txt", "r")
output_story = open("file2.txt","w")
print ("Welcome to MidLab. Let's create a nonsensical story.")

missing_word = ""
newstory = ""
missing_word_list = []
for lines in ori_story:
    word_list = lines.split()
    for words in word_list:
        if words[0] == "[":
            missing_word_list.append(words)
            newstory = newstory + " " + words
        else:
            newstory = newstory + " " + words


replacement =[]
replacementcounter = 0
x = 0
while x < len(missing_word_list):
    missing_input = "Please enter a missing "+ str(missing_word_list[x])
    user_inp = input(missing_input)
    replacement.append(user_inp)
    missing_input = ""
    x += 1
newstory1 = ""  

for lines in ori_story:
    word_list = lines.split()
    for words in word_list:
        if words[0] == "[":
            words = str(replacement[replacementcounter])
            newstory1 = newstory1 + " " + words1
            replacementcounter += 1
        else:
            newstory1 = newstory1 + " " + words
output_story.write(newstory1)
output_story.close()
            
            
    
