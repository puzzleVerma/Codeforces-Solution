#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n,m,x=LI()
    h=LI()
    hh=[]
    for i in range(n):
        hh.append([h[i],i])
    hh.sort()
    ans=[0]*n
    for i in range(n):
        ans[hh[i][1]]=i%m+1
    print("YES")
    print(*ans)

