import random #Fillin1

def PrintRocket():
    for x in range (10, -1, -1):    #Fillin2
        print(x)        #Fillin 3
        
    
    print ( "Blast -off !!" )
    print ( "  *  " )
    print ( " ***" )
    print ( "*****" )
    print ( "*****" )
    print ( "*****" )
    print ( "*****" )
    
def main():
    numCorrect = 0
    for x in range(5):
        num1 = random.randint (1,10)  #Fillin4
        num2 = random.randint (1,10)  #Fillin5
        
        answer = int(input(str(num1) + " + " + str(num2) + " = "))
        
        if answer == (num1 + num2):      #Fillin6
            print ("Congratulations! Your answer is correct!\n")
            numCorrect += 1         #Fillin7
            
        else:
            print ("Sorry, your answer is incorrect.",end = " ")
            print ("Correct answer: ",num1+num2)    #Fillin8
            
            
    if numCorrect == 5:       #Fillin9
        print ( "\nGreat Job! You answered the problems correctly !" )
        PrintRocket()       #Fillin10
    else:
        print ( "You answered:" , numCorrect , " questions correctly ." )
        print ( "Type again for a perfect score!" )
        
main()
    
    