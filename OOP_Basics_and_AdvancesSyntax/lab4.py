cost1 = int(input("Enter the cost of first item:\n"))
cost2 = int(input("Enter the cost of second item:\n"))
payment1 = int(input("Enter the payment amount:\n"))
if payment1 < (cost1+cost2):
    print("Insufficient amount. You still owe:$ ",int((cost1+cost2)-payment1))

else:
    print("Thank you. Your change: $",int(payment1-(cost1+cost2)))
    


