#######puzzleVerma#######


import sys
import math
mod = 10**9+7
from bisect import bisect


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range



for t in range(IN()):
    n=IN()
    li=LI()
    k=2
    m=3
    m-=1
    ans=0
    li.sort()
    for i in range(n):
        ind=bisect(li,li[i]+k)
        ind-=(i+1)
        if ind>=m:
            ans+=((ind*(ind-1))//2)
    print(int(ans))
