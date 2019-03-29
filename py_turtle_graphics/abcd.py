myFile = open("studentInfo.txt","a")

for i in range(1,4):
    myFile.write("Student Information " + str(i) + "\n")
    student_last = input("Enter Last Name:\n")
    student_first = input("Enter First Name:\n")
    myFile.write("Full Student Name: " + student_first + " " + student_last)
    
    studentID = input("Enter ID:\n")
    myFile.write("\nStudent ID: " + studentID)
    
    creditHours = input("Enter the number of credits earned:\n")
    myFile.write("\nCredits Earned: " + creditHours)
    myFile.write("\n")

myFile.close()
    

