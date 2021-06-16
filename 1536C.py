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


for t in r(IN()):
    n=IN()
    s=S()
    d=0
    k=0
    rat=DefaultDict(int)
    ans=[0]*n
    ind=0
    for ele in s:
        if ele=="D":
            d+=1
        else:
            k+=1
        if min(d,k)==0:
            ans[ind]=max(d,k)
        else:
            rat[d/k]+=1
            ans[ind]=rat[d/k]
        ind+=1
    print(*ans)

