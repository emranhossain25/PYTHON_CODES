def product_of_sum(n):
    product=1
    sum=0
    while n!=0:
        product = product * (n%10)
        sum +=product
        n =n//10
        return product
    return sum

n=4356
print(product_of_sum(n))