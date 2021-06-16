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
    num=DefaultDict(int)
    d=dict()
    for i in range(n):
        if li[i] not in d:
            d[li[i]]=i+1
        else:
            num[li[i]]=1
    li=set(li)
    li=sorted(li)
    for i in set(li):
        if num[i]==0:
            print(d[i])
            break
    else:
        print(-1)

