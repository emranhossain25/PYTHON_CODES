
def is_Harshad(n):
    sum=0
    temp=n
    while temp>0:
        sum= sum +temp%10
        temp = temp//10
    return n%sum==0

num=int(input("Enteer any number..."))
if(is_Harshad(num)):
    print("its  harshad number...")
else:
    print("its not harshad number...")