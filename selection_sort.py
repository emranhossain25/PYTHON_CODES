from operator import le


def SELECTION_SORT(arr):
    n=len(arr)
    for i in range(n):
        indexOFmin=i
        for j in range(i+1,n):
            if arr[indexOFmin]>arr[j]:
                indexOFmin=j
            #swap arr[i],arr[indexOfmin]
        arr[i],arr[indexOFmin]=arr[indexOFmin],arr[i]

arr=[10,2,3,60,40,50,90,62,31]
SELECTION_SORT(arr)
print("SORTING ARRAY..")
for i in range(len(arr)):
    print(" %d " %arr[i],end=" ")