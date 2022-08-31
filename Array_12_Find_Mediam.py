
def Find_mean(arr,n):
    sum=0
    for i in range(0,n):
        sum +=arr[i]
    return float(sum/2)

def Find_Median(arr,n):
    sorted(arr)
    if n%2!=0:
        return float(arr[int(n/2)])
    return float(arr[int(n-1)/2] - arr[int(n/2)/2.0])

arr=[2,4,5,6,7,8,9]
n=len(arr)
print('Mean=',Find_mean(arr,n))
print('Median=',Find_Median(arr,n))