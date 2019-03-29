import sys
print("Fractal Generator")

valid = False
while valid == False:
    try:
        user_input = int(input("Enter an integer > 0:\n"))
        if user_input > 0:
            valid = True
    except:
        pass
    
def fractal(length, spaces):
    if length == 1:
        print(" " * spaces + "*")
    
        
    elif length>1:
        fractal(length/2,spaces)
        print(str(" " * int(spaces)) + str("*" * int(length)))
        print(str(" " * int(length//2)),end = "")  
        fractal(length/2,spaces)       
        
fractal (user_input,0)
sys.exit(0)