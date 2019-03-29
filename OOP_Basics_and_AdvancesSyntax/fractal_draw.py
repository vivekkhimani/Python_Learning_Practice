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
        print((" " * int(spaces)) + "*")
    
        
    elif length>1:
        fractal(length/2,spaces)
        print(str(" " * int(spaces)) + str("*" * int(length)))
        fractal(length/2,spaces + length//2)       
        
fractal (user_input,0)
sys.exit(0)