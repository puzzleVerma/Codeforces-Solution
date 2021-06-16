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
    ans=[0]*n
    for i in r(n-1):
        ans[i]=i+2
    ans[n-1]=1
    print(*ans)
