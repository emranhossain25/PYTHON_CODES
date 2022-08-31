
def reverse_Digit(n):
    
    reverse=0
    while n>0:
        remender=n%10
        reverse = (reverse * 10) + remender
        n = n//10
    return reverse

num=int(input("Enter Any Digits...."))

rev=reverse_Digit(num)
print(rev)