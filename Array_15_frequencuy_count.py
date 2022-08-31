from itertools import count


def CoubntFrequency(arr,n):
    visit=[False for i in range(n)]

    for i in range(n):
        if(visit[i]==True):
            continue
        count =1
        for j in range(i+1,n,1):
            if (arr[i]==arr[j]):
                visit[j]=True
                count+=1
        print(arr[i],count)


arr=[1,1,1,5,5,5,7,75,8,9,101]
n=len(arr)
CoubntFrequency(arr,n)