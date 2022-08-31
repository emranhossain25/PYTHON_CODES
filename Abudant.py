num=int(input("Enter any number...."))

sum=0
for i in range(2,num):
    if (num%i==0):
        sum = sum+i
#1+2+3+4+6=16<12
if (sum>num):
    print(num,"Number is abudent....")
else:
    print("Number is not abudent....")