#Find permutations in which n people can occupy r seats in a classroom.

def fact(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans


n=int(input("Enter n"))
r=int(input("enter r"))

res=fact(n)
num=fact(n-r)

print(res/num)