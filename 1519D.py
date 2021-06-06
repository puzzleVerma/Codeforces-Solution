#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


if 1:
    n=IN()
    a,b=LI(),LI()
    sm=0
    for i in r(n):
        sm+=a[i]*b[i]
    ans=sm
    for i in r(n):
        for j in r(i-1,i+1):
            temp=sm
            k=i+1
            while((j>=0) and (k<n)):
                temp-=((a[j]-a[k])*(b[j]-b[k]))
                ans=max(ans,temp)
                j-=1
                k+=1
    print(ans)