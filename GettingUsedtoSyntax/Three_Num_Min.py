import sys
print("Welcome. This program will calculate the minimum of three numbers you enter.")
try:
    num1=int(input("First number please:"))
    num2=int(input("Second number please:"))
    num3=int(input("Third number please:"))
    L=[]
    L.append(num1)
    L.append(num2)
    L.append(num3)
    print("The minimum number is",min(L))
except Exception as e:
    print("Error",e)
    print("Sorry we failed to compare the numbers")
    sys.exit()