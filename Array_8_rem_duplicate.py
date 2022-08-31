#Remove Duplicate In sorted Array

from subprocess import list2cmdline


def RemoveDuplicate(arr,n):
    if n==0 and n==1:
        return n
    
    temp=list(range(n))
    j=0
    for i in range(0,n-1):
        if arr[i]!=arr[i+1]:
            temp[j]=arr[i]
            j +=1
    temp[j]=arr[n-1]
    j+=1

    for i in range(0,j):
        arr[i]=temp[i]
    return j

arr=[2,22,2,3,3,4,5,6,6]
n=len(arr)
n=RemoveDuplicate(arr,n)
for i in range(n):
    print("%d" %arr[i] ,end=" ")