arr=[1,8,9,7,20,6]
n=len(arr)
k=20
low=0
high=n-1
ans=-1

while low<=high:
    mid=(low+high)/2
    if (arr[mid]>k):
        high=mid-1
    elif (arr[mid] <k):
        low=mid+1
    else:
        ans=mid
        break

print("The Element Presnt In Index No =",ans)
