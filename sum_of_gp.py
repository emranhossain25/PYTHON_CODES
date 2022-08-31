
def sum_of_GP(a,r,n):
    sum=0
    for i in range(0,n):
        sum=sum+a
        a=a*r
    #sum= a * (pow(r,n)-1)/(r-1)
    return sum

a=float(input("Enter First term of GP"))
r=float(input("Common Rotation Of GP"))
n=int(input("Number Of Terms Of GP"))

sum=sum_of_GP(a,r,n)
print(sum)