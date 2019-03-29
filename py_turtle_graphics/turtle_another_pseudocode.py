import turtle

def B(line):
    if line>5:
        turtle.forward(line)
        turtle.right(20)
        B(line-15)
        turtle.left(40)
        B(line-15)
        turtle.right(20)
        turtle.backward(line)
        
    
        
turtle.left(90)
B(50)