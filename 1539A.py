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
    n,x,t=LI()
    f=t//x
    ans=f*(max(0,n-f))
    f-=1
    f=min(n-1,f)
    ans+=((f*(f+1))//2)
    print(ans)
