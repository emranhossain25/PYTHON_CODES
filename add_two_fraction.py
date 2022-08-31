def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def simple(num3,den3):
    gcd_of=gcd(num3,den3)

    num3 /=gcd_of
    den3 /= gcd_of

num1=3
den1=7
num2=1
den2=7,num3,den3
lcm=(den1 * den2) / gcd(den1,den2)
den3=lcm
num3=num1 * (den3/den1) + num2 * (den3/den3)
simple(num3,den3)

print(num1 + "/" + den1 + " + " + num2 + "/" + den2 + " = " + num3 + "/" + 
    den3);