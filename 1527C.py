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
    li=LI()
    dd=DefaultDict(int)
    ans=0
    for i in range(n):
        ans+=dd[li[i]]*(n-i)
        dd[li[i]]+=(i+1)

    print(ans)        

