def Factorial(n):
    if ( n==0 or n==1):
        return 1
    else:
        return n * Factorial(n-1)
    
num=int(input("Enter any number...."))
Fact=Factorial(num)
print(Fact)