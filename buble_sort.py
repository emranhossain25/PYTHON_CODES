def BUBBLE_SORT(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[1,5,2,3,78,54,30,10]
BUBBLE_SORT(arr)
print("SORTED  ARRAY...")

for i in range(len(arr)):
    print(" %d " %arr[i],end=" ")