import sys
print ("Welcome to a fun word replacement game.")

try:
    file_name = input("Enter the name of the file to use:\n")
    open_file = open(file_name,'r')

except:
    print ("Error Bad File Name")
    sys.exit(0)
    
new_string = ""
input_list = []    
for lines in open_file:
    word_list = lines.split()
    for words in word_list:
        if words[0] == "[":
            words = words.replace ("-"," ")
            words = words.replace (","," ")
            words = words.replace ("."," ")
            words = words.replace ("!"," ")
            
            if words[1] in ['a','e','i','o','u']:
                resultant_question = "Please give an " + words[1:len(words)-1] + "\n"
                user_input = input(resultant_question)
                words = str(user_input)
                new_string = new_string + words + " "
            
            else:
                resultant_question = "Please give a " + words[1:len(words)-1] + "\n"
                user_input = input(resultant_question)
                words = str(user_input)
                new_string = new_string + words + " "
        else:
            new_string = new_string + words + " "
print("Here is your story:")
print("--------------------")
print(new_string)
open_file.close()
                