#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range
from bisect import *

def split(l,r,a,sl):
    mid=(a[l]+a[r])//2
    mid=bisect(a,mid)
    sl+=[d[mid-1]-d[l-1]]
    if (mid-1)!=r:
        split(l,mid-1,a,sl)
    sl+=[d[r]-d[mid-1]]
    if mid!=l and mid<=r:
        split(mid,r,a,sl)

    

    


for t in r(IN()):
    n,q=LI()
    a=LI()
    a.sort()
    sm=0
    d=dict()
    d[-1]=0
    for i in range(n):
        sm+=a[i]
        d[i]=sm
    sl=[sm]
    split(0,n-1,a,sl)
    sl.sort()
    for i in r(q):
        s=IN()
        ans=bisect(sl,s)
        if ans==0:
            print("NO")
        elif s==sl[ans-1]:
            print('YES')
        else:
            print('NO')
