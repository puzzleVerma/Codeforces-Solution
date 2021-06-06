#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


for t in r(IN()):
    n=IN()
    a=LI()
    ans=[0 for i in r(n)]
    l=0
    for i in r(n):
        l=max(l,a[n-1-i])
        if l:
            ans[n-i-1]=1
        l-=1
    print(*ans)

