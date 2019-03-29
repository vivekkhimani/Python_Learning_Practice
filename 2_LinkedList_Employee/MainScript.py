from MyList import LinkedList
from employee import Employee

def initial_display():
    print ("***CS172 PAYROLL PROGRAM***")
    print ("a. Add New Employee")
    print ("b. Calculate Weekly Wages")
    print ("c. Display Payroll")
    print ("d. Update Employee Hourly Rate")
    print ("e. Remove Employee from Payroll")
    print ("f. Exit the Program")
    

initial_display()
user_input = input("Enter your choice\n")

main_object = LinkedList()
while user_input.lower() in ["a","b","c","d","e","f"]:
    if user_input.lower() == "a":
        id_input = input("Enter the New Employee ID:\n")
        hour_input = int(input("Enter the Hourly Rate:\n"))
        main_object.AddNewMethod(Employee(id_input,hour_input))
        initial_display()
        user_input = input("Enter your choice\n")
        
    elif user_input.lower() == "b":
        main_object.WeeklyWages()
        initial_display()
        user_input = input("Enter your choice\n")
        
    elif user_input.lower() == "c":
        main_object.DisplayPayroll()
        initial_display()
        user_input = input("Enter your choice\n")
        
    elif user_input.lower() == "d":
        id_input1 = input("Enter the Employee ID:\n")
        hour_input1 = int(input("Enter the new hourly rate:\n"))
        main_object.HourlyRate(id_input1,hour_input1)
        initial_display()
        user_input = input("Enter your choice\n")
        
    elif user_input.lower() == "e":
        id_remove = input("Enter the Employee ID to remove:\n")
        main_object.EmpRemove(id_remove)
        initial_display()
        user_input = input("Enter your choice\n")
        
    else:
        break
        
    
        
        
        
        
        
            
        
        
        