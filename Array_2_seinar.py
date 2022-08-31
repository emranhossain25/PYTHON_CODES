#Find The Maximum Eleement...
lst=[]
n=int(input("Enter The Length Of The Array...."))

for i in range(1,n+1):
    arr=int(input("Enter The Array Element One By One.... "))
    lst.append(arr)
print("MAXIMUM ELEMENT IS..",max(lst))