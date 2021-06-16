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
    n=IN()
    li=LI()
    mx=-1
    mn=101
    for i in r(n):
        if li[i]>mx:
            mx=li[i]
            xx=i+1
        if li[i]<mn:
            mn=li[i]
            nn=i+1
    ans1=max(xx,nn)
    ans2=n+1-min(xx,nn)
    ans3=min(xx,nn)+n+1-max(xx,nn)
    # if (nn<=n//2 and xx<=n//2) or (nn>n//2 and xx>=n//2):
    #     ans1=min(xx,n-xx+1)
    #     ans1=max(ans1,min(nn,n-nn+1))
    # else:
    #     ans1=min(xx,n-xx+1)
    #     ans1+=min(nn,n-nn+1)
    print(min(ans1,ans2,ans3))
