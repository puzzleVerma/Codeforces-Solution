#######puzzleVerma#######


import sys
import math
mod = 998244353


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


if 1:
    n=IN()
    pas=0
    ans=0
    dp=[0]*(n+1)
    for i in r(1,n+1):
        for j in range(i,n+1,i):
            dp[j]+=1
    for i in r(1,n+1):
        ans=pas+dp[i]
        pas+=ans
        pas%=mod
    print(ans)

