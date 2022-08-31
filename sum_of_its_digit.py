def sum_of_its_digit(n):
    sum=0

    while n!=0:
        d = n%10
        sum+=d
        n/=10
    return sum

num=123
print(sum_of_its_digit(num))