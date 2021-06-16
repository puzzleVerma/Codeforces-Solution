#######puzzleVerma#######


import sys
import math
from typing import DefaultDict
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res



for t in r(IN()):
    n=IN()
    r1=LI()
    r2=LI()
    di=dict()
    sm=0
    nsm=0
    df=[]
    for i in range(n):
        di[r1[i]]=r2[i]
    for i in range(1,n+1):
        if (di[di[i]]==i):
            sm+=1
        else:
            df+=[i]
    lp=DefaultDict(int)
    for ele in df:
        if lp[ele]==0:
            fn=ele
            st=ele
            lp[st]=1
            while di[st]!=fn:
                st=di[st]
                lp[st]=1
            nsm+=1
    print(lp)
    sm//=2
    ex=sm+nsm
    ans=power(2,ex,mod)
    ans=ans%mod
    print(ans)
    

