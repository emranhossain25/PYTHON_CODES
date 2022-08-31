
def is_Automorphic(n):
    sq = n*n

    while n>0:
        if (n%10 != sq%10):
            return False
            n/=10
            sq/=10
        
    return True

number = int(input("Enter any number......"))

if(is_Automorphic(number)==True):
    print("In the given number is Automorphic")
else:
    print("In the given number is not Automorphic")
    