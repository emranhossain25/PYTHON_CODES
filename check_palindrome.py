#num=int(input("enter any number"))
#copy=num

#reverse=0

#while num!=0:
 #   r=num % 10;
  #  reverse=reverse*10+r
   # num=int(num/10)

    #if copy==reverse:
     #   print("num is pa;indrome")
    #else:
     #   print("not a palindrome")#

def reverse(no):
    rev=0

    while no>0:
        rev = rev*10 + (no % 10)
        no=no//10
    return rev

def palimdrome(no):
    if no==reverse(no):
        return True
    else:
        return False

num = int(input("Enter any number..."))

palimdrome(num)