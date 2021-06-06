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
    l=LI()
    li=sorted(l)
    curr=0
    ans=0
    for i in r(n-1):
        curr+=li[i]
        if curr<li[i+1]:
            ans=li[i]
    fin=[]

    for i in r(n):
        if l[i]>ans:
            fin+=[i+1]
    print(len(fin))
    print(*fin)
