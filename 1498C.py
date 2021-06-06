#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


for t in r(IN()):
    n,k=LI()
    k-=1
    ans=1
    if k==0:
        print(ans)
        continue
    k-=1
    ans+=n
    if k==0:
        print(ans)
        continue
    if n==1:
        print(2)
        continue

    rf=n-1
    rfl=[1]*rf
    rfl2=[1]*rf
    
    for i in r(k):
        sm=sum(rfl2)
        sm%=mod
        rfl=rfl2.copy()
        rfl[-1]=0
        # print(rfl,rfl2)
        for j in r(rf):
            sm-=rfl[j-1]
            sm%=mod
            rfl2[n-2-j]=sm
            ans+=sm
            ans%=mod
            # print(ans,sm)


    print(ans)
