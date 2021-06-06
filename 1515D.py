#######puzzleVerma#######


import sys
import math
from collections import defaultdict
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n,l,r=LI()
    c=LI()
    ldd=defaultdict(int)
    rdd=defaultdict(int)
    ll=0
    rr=0
    for i in range(n):
        if i<l:
            ldd[c[i]]+=1
        else:
            rdd[c[i]]+=1
    sc=set(c)
    for ele in sc:
        it=min(ldd[ele],rdd[ele])
        ldd[ele]-=it
        rdd[ele]-=it
        l-=it
        r-=it
    ans=0
    if l>r:
        for ele in sc:
            it=ldd[ele]//2
            ans+=min(it,(l-r)//2)
            l-=it*2
            if l<=r:
                break
    elif r>l:
        for ele in sc:
            it=rdd[ele]//2
            ans+=min(it,(r-l)//2)
            r-=it*2
            if r<=l:
                break
    ans+=max(l,r)
    print(ans)
    