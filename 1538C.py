#######puzzleVerma#######


import sys
import math
from bisect import *
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


for t in r(IN()):
    n,l,r=LI()
    li=LI()
    li.sort()
    ans=0
    for i in range(n-1):
        rr=bisect_right(li,r-li[i],i+1,n)
        ll=bisect_left(li,l-li[i],i+1,n)
        ans+=(rr-ll)
    print(ans)