from cmath import pi


def average(arr,n):
    sum=0
    for i in range(n):
        sum +=arr[i]
    return sum/n;

arr=[1,5,56,40,20]
n=len(arr)

#for i in range(1,n+1):
#    arr=int(input("Enter array element ..."))
#    lst.append(arr)
print(average(arr,n))