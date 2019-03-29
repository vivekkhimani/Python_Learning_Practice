def user_inp(question):
    while True:
        try:
            question=int(input("Enter a number"))
            question=int(question)
            print("It's a number")
            return question
        except:
            print("Not a number")
            
            
x=user_inp("Enter your score for quiz 1:")
y=user_inp("Enter your score for quiz 2:")
average=(x+y)/2
print(average)