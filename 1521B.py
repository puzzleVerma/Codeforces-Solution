#######puzzleVerma#######


import sys
import math
mod = 10**9+7


# Function for checking prime
def isPrime(n):
    #for less than  4
    if(n <= 1):
        return False
    if(n <= 3):
        return True
     
    # This is checked so that we can skip
    # middle five numbers in below loop
    if(n % 2 == 0 or n % 3 == 0):
        return False
     
    for i in range(5,int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
     
    return True
 
# Function to return the smallest
# prime number greater than N
def nextPrime(N):
 
    # Base case
    if (N <= 1):
        return 2
 
    prime = N
    found = False

    while(not found):
        prime = prime + 1
 
        if(isPrime(prime) == True):
            found = True
 
    return prime


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=IN()
    li=LI()
    if n==1:
        print(0)
        continue
    time=(n-1)//2
    time+=1
    print(time)
    mxp=1999999973
    print(1,2,mxp,min(li[0],li[1]))
    li[1]=min(li[0],li[1])
    i=1
    while (time-1):
        ele=min(li[i],li[i+1])
        print(i+1,i+2,ele,mxp)
        i+=2
        time-=1
