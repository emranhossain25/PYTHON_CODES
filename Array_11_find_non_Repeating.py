from numpy import who


def Find_Non_Repeating(arr,n):
    for i in range(n):
        j=0
        while (j<n):
            if i!=j and arr[i]==arr[j]:
                break
            j +=1
            if (j==n):
                return arr[i]
    return -1

arr=[2,1,2,4,5,6,4,5]
n=len(arr)
print(Find_Non_Repeating(arr,n))