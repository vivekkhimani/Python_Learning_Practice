x=input("Enter any number")
while True:
    try:
        x=int(x)
        print("Thank you for entering the number")
        break
    except ValueError as e:
        print("Error:",e)
        print("The entered input wasn't number. Try again.")
        x=input()
        