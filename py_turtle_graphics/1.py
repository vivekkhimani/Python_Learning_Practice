sportsList = open('sports.txt')
for index in range(1,11):
    sp = sportsList.readline(5_000_000)
    if len(sp) >= 8 :
        print (sp .rstrip())    
