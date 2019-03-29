import turtle,math
def DrawTriangle(x1,y1,s1):
    turtle.penup()
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.forward(s1)
    turtle.left(120)
    turtle.forward(s1)
    turtle.left(120)
    turtle.forward(s1)
    turtle.left(120)
    
def SEIRPINSKI(x,y,s):
    if s>10:
        DrawTriangle(x,y,s)
        
        SEIRPINSKI(x,y,s/2)
        SEIRPINSKI(x+0.5*s,y,s/2)
        SEIRPINSKI(x+0.25*s,y + (math.sqrt(3)*s)/4,s/2)
        
        
SEIRPINSKI(20,20,100)

        