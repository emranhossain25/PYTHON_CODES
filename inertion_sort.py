
def INSERTION_SORT(arr):
    n=len(arr)
    
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j >=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=key

arr=[10,9,8,40,30,50,20]
INSERTION_SORT(arr)
print('SORTING ARARY......')
for i in range(0,len(arr)):
    print(" %d " %arr[i],end=" ")