def _sum(arr,n):
    return sum(arr)

lst=[]
n=len(lst)

n=int(input("Enter The length of the array..."))

for i in range(1,n+1):
    arr=int(input("Enter The Array Element..."))
    lst.append(arr)
print(_sum(lst,n))