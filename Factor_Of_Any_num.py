def factor_of_any(n):
    print("Factor are",n,"are")
    for i in range(1,n+1):
        if n%i==0:
            print(i)

num=320
print(factor_of_any(num))