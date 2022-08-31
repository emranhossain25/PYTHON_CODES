#Find The Smallest in A array

lst=[]

n=int(input("Enter the array length..."))

for i in range(1,n+1):
    arr=int(input("Enter The array element...."))
    lst.append(arr)

print("MINIMUM ELEMENT IS...",min(lst))