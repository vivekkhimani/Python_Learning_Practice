try:
    x=int(input("Enter a number: "))
    y=int(input("Another number for division: "))
    z=x/y
    print(z)
except Exception as e:
    print("Error:",e)
    