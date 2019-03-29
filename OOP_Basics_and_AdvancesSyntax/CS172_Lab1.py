import sys
import spellchecker from spellchecker.py as SP1

print("Welcome to the Spellchecker Online.")
file_name = input("Enter to open a file.\n")

def get_file(file_open):
    valid = False
    while valid == False:
        try:
            file_input = open(file_open,"r")
            valid = True
        
        except FileNotFoundError as e:
            print("File Not Found. Try again.")
            
check_file = get_file(file_name)

SP = SP1("dictionary.txt")

word_count = 0
true_word_count = 0
for lines in check_file:
    word_list = lines.split()
    for words in word_list:
        if SP.check(words) == False:
            print("Possible Spelling Error on line",lines,":",words)
            false_word_count += 1
            
            
        else:
            true_word_count += 1
            
print (true_word_count,"words passed the spell checker")
print (false_word_count,"words failed the spell checker")
percent = (true_word_count/(true_word_count + false_word_count))
print(percent,"% words passed.")
            

            
    
            
        