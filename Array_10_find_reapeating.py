#Find The Reapting Element In A array

from numpy import size


def Repeating_Element(arr,n):
    print("Repeating Element Are...")

    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                print(arr[i],end= ' ')

arr=[1,1,2,23,4,4,5,6,7]
size=len(arr)
Repeating_Element(arr,size)