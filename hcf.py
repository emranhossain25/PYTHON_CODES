def HCF_NUM(x,y):

    if x>y:
        smaler=y
    else:
        smaler=x
    for i in range(1,smaler+1):
        if (x%i==0) and (y%i==0):
            hcf=i
        
    return hcf

num1=int(input("Enter first number..."))
num2=int(input("Enter second number..."))

hcf=HCF_NUM(num1,num2)

print("HCF of ",num1,"and",num2,"is",hcf)
