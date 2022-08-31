lower=int(input("Enter the range of the lower  range"))
upper=int(input("Enter the range of the upper range"))

order=int(input("Enter the order..."))

for num in range(lower,upper+1):
    sum=0
    temp=num

    while temp>0:
        remerder=num%10
        sum += remerder ** order
        temp = num//10

        if(num==sum):
            print(num)
        