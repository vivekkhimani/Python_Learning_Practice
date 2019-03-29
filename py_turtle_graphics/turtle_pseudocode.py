import turtle
def A(lineLen):
    if lineLen > 0:
        turtle.forward(lineLen)
        turtle.right(90)
        A(lineLen - 5)
    
        return
    
A (50)
        