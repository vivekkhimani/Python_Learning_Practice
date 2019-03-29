#Vivek Khimani
#Drexel University 2018
#BMI Calculator (Lecture 3 Project)
import sys
try:
    wip=float(input("Please enter your weight in pounds:"))
    if wip<0:
        print("Weight cannot be negative. Please run the program again to try again.")
        sys.exit()
    else:
        wip=wip*0.453592
        print("Thank you. Your weight in kg is",wip)
            
    height=float(input("Please enter your height in feet:"))
    if height<0:
        print("Height cannot be negative. Please run the program again to try again.")
        sys.exit()
    else:
        height=height*0.3048
        print("Thank you. Your height in meters is",height)
        
    BMI=((wip)/(height*height))
    rBMI=round(BMI,1)
    if BMI<=18.5:
        print("Your BMI is:",rBMI,"You are UNDER WEIGHT.")
    elif BMI>18.5 and BMI<=24.9:
        print("Your BMI is:",rBMI,"You are NORMAL WEIGHT.")
    elif BMI>=25.0 and BMI<=29.9:
        print("Your BMI is:",rBMI,"You are OVER WEIGHT.")
    elif BMI>=30:
        print ("Your BMI is:",rBMI,"You are suffering from OBESITY.")
    

except ValueError as e:
    print("This is the error:",e)
    print("Sorry. You've been exited the program. Please run it again to try again.")
    sys.exit()
    
            
            
