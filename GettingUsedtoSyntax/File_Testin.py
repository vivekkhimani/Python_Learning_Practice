import sys
try:
    va=open("File_Testing.txt")
except FileNotFoundError as e:
    print("File Not Found")
    sys.exit()
dic={}
for line in va:
    word_list=line.split()
    for words in word_list:
        letter=words[0]
        letter=letter.upper()
        if letter in dic.keys():
            dic[letter]+=1
        else:
            dic[letter]=1
va.close()

out_file=open("Output_Test.txt","w")
key_list=list(dic.keys())
key_list.sort()
for keys in key_list:
    result="Number of words starting with:"
    result+=str(keys)+" is "
    result+=str(dic[keys])+"\n"
    out_file.write(result)
out_file.close()