
#arr=[2,2,2,3,4,5,5,6,6,20]
#n=len(arr)
#for i in range(n):
#    if i is not n:
#        arr.append(i)

def RemoveDuolicate(arr,n):
    mp={ i: 0 for i in arr}

    for i in range(n):
        if mp[arr[i]]==0:
            print(arr[i],end=" ")
            mp[arr[i]]=1
arr=[2,1,2,4,5,5]
n=len(arr)
RemoveDuolicate(arr,n)