def PARTITION(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[j+1],arr[high]=arr[high],arr[j+1]
    return i+1    

def QUICK_SORT(arr,low,high):
    if low<high:
        partion=PARTITION(arr,low,high)
        QUICK_SORT(arr,low,partion-1)
        QUICK_SORT(arr,partion+1,high)


arr=[4,10,5,80,20,30,47,21]
QUICK_SORT(arr,0,len(arr)-1)
print("SORTING ARRAY...")
for i in range(len(arr)):
    print(" %d " %arr[i],end=" ")