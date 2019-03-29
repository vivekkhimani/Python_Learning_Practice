import math
class Fraction:
    #Puts Fraction in simplest form.
    def __init__(self,a,b):
        self.num = a
        self.den = b
        self.simplify()
        
    #Print Fraction as a String.
    def __str__(self):
            return str(self.num) + "/" + str(self.den)
        
    #Get the numerator
    def GetNum (self):
        return self.num
    #Get the denominator
    def GetDen (self):
        return self.den
    
    #Numerical Approximation
    
    def Approx (self):
        return self.num / self.den
    
    def simplify (self):
        x = self.gcd(self.num,self.den)
        self.num = self.num//x
        self.den = self.den//x
        
    def gcd (self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd (b,a%b)
        
        
    def __add__ (self,other):      #add Fractions.
        return Fraction ((self.num * other.den) + (other.num * self.den) , self.den * other.den)
    
    def __sub__(self,other):      #subtract Fractions.
        return Fraction ((self.num * other.den) - (other.num * self.den) , self.den * other.den)
    
    def __mul__(self,other):      #multiply Fractions.
        return Fraction ((self.num * other.num) , (self.den * other.den))
    
    def __truediv__(self,other):  #divide Fractions.
        return Fraction ((self.num * other.den) , (self.den * other.num))
    
    def __pow__(self,exp):     #Powers of Fractions.
        if exp < 0:
            return Fraction (self.den ** exp , self.num ** exp)
        elif exp == 0:
            return Fraction (1,1)
        else:
            return Fraction (self.num ** exp , self.den ** exp)
        
        
print ("Welcome to the Fractions Calculator")
valid = False
while valid == False:
    try:
        x = int(input("Please enter your n as an input."))
        print ("Thank you for a valid input")
        valid = True
        
        #Harmonic Series Calculation
        nh = 1
        harmonic_answer = Fraction (0,1)
        while nh <= x:
            harmonic_object = Fraction(1,nh)
            harmonic_answer = harmonic_answer + harmonic_object
            nh +=1
        print ("H("+str(x)+"):",harmonic_answer)
        
        
        #Two Series Calculation
        th = 0
        two_answer = Fraction (0,1)
        while th <= x:
            two_object = Fraction(1,2) ** th
            two_answer = two_answer + two_object
            th += 1
        print ("T("+str(x)+"):",two_answer)
            
            
        #Zero Series Calculation
        zero_answer = Fraction (4,2) - two_answer
        print ("Z("+str(x)+"):",zero_answer)
            
        #Partial Riemann Zeta
        reimann_answer = Fraction (0,1)
        b = 2
        rh = 1
        while rh<= x:
            while b<=8:
                reimann_object = Fraction (1,rh) ** b
                reimann_answer = reimann_answer + reimann_object
                print("R("+str(x)+","+str(b)+"):",reimann_answer)
                b+=1
            rh+=1
                
            
            
            
                
    except ValueError as e:
        print ("Please enter an integer")
        
        
        
        