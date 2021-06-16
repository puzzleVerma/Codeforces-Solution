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
    all=[]
    flag=0
    d=dict()
    lim=(m+1)//2
    for i in range(1,n+1):
        d[i]=lim
    for j in range(m):
        li=LI()
        all+=[li]
        if li[0]==1:
            d[li[1]]-=1
            if d[li[1]]<0:
                flag=1
    # print(d)
    if flag==1:
        print("NO")
        continue
    ans=[]
    for ele in all:
        if ele[0]==1:
            ans+=[ele[1]]
            continue
        for itm in ele[1:]:
            if d[itm]>0:
                d[itm]-=1
                ans+=[itm]
                break
    # print(all)
    # print(ans)
    # print(d)
    print("YES")
    print(*ans)