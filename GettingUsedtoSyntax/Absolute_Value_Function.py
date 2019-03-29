x=int(input("Please enter any number"))
def abs_value(inp):
    if inp<=0:
        inp=(-1)*inp
        return inp
    else:
        return inp
    
print(abs_value(x))
    