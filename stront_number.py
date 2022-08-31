def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

def is_strong(num):
    sum=0
    while num>0:
        digit = num%10
        sum = sum + factorial(digit)
        num = num//10
    return sum

number = int(input("Enter a number......"))

if is_strong(number):
    print("Yes This is a strong number...")
else:
    print("This is not a strong number....")