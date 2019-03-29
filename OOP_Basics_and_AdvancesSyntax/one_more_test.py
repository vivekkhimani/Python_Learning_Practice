import sys
print ("Welcome to Binary Printer")
print ("Enter exit to quit at any time.")

def getInt(question):
    user_input = input(question)
    while user_input.lower() != "exit":
        try:
            user_input = int(user_input)
            return user_input
        except:
            print("Not a Number.")
            user_input = input(question)
    sys.exit()
    
       

def binaryStr(num,bits):
    rev_binary_str = ""
    remainder = 0
    quotient = num
    while quotient!=0:
        remainder = quotient%2
        rev_binary_str += str(remainder)
        quotient = quotient//2
        
    required_binary = rev_binary_str [::-1]
    
    if len(required_binary)>=bits:
        return required_binary[len(required_binary)-bits:]
    
    elif len(required_binary)<bits:
        required_zero = bits - len(required_binary)
        required_binary = ("0"*required_zero)+required_binary
        return required_binary
        
while True:
    user_input1 = getInt("Enter a Positive Int:\n")
    user_input2 = getInt("Number of Bits:\n")
    print("As Binary:",binaryStr(user_input1,user_input2))
   

                
            


                
            
