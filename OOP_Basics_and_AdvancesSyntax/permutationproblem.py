import factorialmodule

if __name__ == "__main__":
    valid = False
    while valid == False:
        try:
            n = input("Please enter size of the set: ")
            n = int(n)
            k = input("Please enter the number of elements: ")
            k = int(k)
            perm = (factorialmodule.factorialfun(n))/(factorialmodule.factorialfun(n-k))
            print ("No of permutation is:",perm)
            valid = True
        except ValueError as e:
            print ("Please enter a number.")
            
else:
    print("File is not a script.")