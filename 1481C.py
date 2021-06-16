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
    n,m=LI()
    a=LI()
    b=LI()
    c=LI()
    q=0
    pnt=DefaultDict(list)
    for i in r(n):
        if a[i]!=b[i]:
            pnt[b[i]]+=[i+1]
            q+=1

    if c[-1] not in b:
        print("NO")
        continue
    ans=[0]*m
    for i in range(m-1,-1,-1):
        if pnt[c[i]]!=[]:
            ans[i]=pnt[c[i]].pop()
            q-=1
            if i==m-1:
                cmn=ans[i]
        elif i==m-1:
            for j in r(n):
                if b[j]==c[i]:
                    ans[i]=j+1
                    cmn=j+1
        else:
            ans[i]=cmn
    if q==0:
        print("YES")
        print(*ans)
    else:
        print("NO")

