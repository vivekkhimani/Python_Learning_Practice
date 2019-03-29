class MyStack:
    def __init__(self):
        self.__S = []
        
    def __str__(self):
        return str(self.__S)
    
    def push(self,element):
        self.__S.append(element)
        
    def pop(self):
        return self.__S.pop()
    
    def top(self):
        return self.__S[-1]
    

def postflix(exp):
    my_list = exp.split()
    stack_object = MyStack()
    
    for ele in my_list:
        if ele.isnumeric() == True:
            stack_object.push(ele)
        
        else:
            if ele == "+":
                stack_object.push(float(stack_object.pop()) + float(stack_object.pop()))
                
            elif ele == "-":
                stack_object.push(float(stack_object.pop()) - float(stack_object.pop()))
            
            elif ele == "*":
                stack_object.push(float(stack_object.pop()) * float(stack_object.pop()))
                
            elif ele == "/":
                stack_object.push(float(stack_object.pop()) / float(stack_object.pop()))
                
    return float(stack_object.top())

print("Welcome to the Postfix Calculator")
print("Enter exit to quit")

my_input = input("Enter your expression:\n")
while my_input.lower() != "exit":
    print("Result:\n"+str(postflix(my_input)))
    my_input = input("Enter your expression:\n")


            
    