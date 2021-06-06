#######puzzleVerma#######


import sys
import math
from collections import defaultdict as dd
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=LI()
    li=LI()
    d=dd(int)
    for i,ele in enumerate(li,0):
        ele-=i
        d[ele]+=1
    ans=0
    for ele in d:
        if d[ele]>1:
            ans+=int(d[ele]*(d[ele]-1)/2)
    print(ans)