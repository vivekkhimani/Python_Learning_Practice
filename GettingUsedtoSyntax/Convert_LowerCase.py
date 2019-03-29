word="My Name is Vivek"
lowerword=""
i=0
while i<len(word):
    letter=ord(word[i])
    if letter>=65 and letter<=90:
        letter+=32
    lowerword+=chr(letter)
    i+=1
print("Before:",word)
print("After:",lowerword)