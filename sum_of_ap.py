from ast import Num


def sumofap(a,n,d):
    sum = (n * (2*a + (n-1)*d))/2
    return sum

a=int(input("Enter first number..."))
d=int(input("Enter comon difference number...."))
n=int(input("Enter total number..."))

sum=sumofap(a,n,d)
print(sum)