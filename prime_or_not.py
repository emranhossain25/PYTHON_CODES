#def isPRIME(int n):
 #   for i in range(2,n):
  #      if (n%i==0):
   #         return False
    #return True

lower = 0
upper = 300

for num in range(lower , upper+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)

    
                