import math


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
a=60
b=48

print(gcd(60,48))

print(math.gcd(60,48))