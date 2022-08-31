arr=[4,6,9,8,9,8]
n=len(arr)
k=9
answer=-1
for i in range(0,n):
    if (arr[i]==k):
        ans=i
        break
print("The Element Presen In Index NO=",ans)