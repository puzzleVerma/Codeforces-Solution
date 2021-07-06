#######puzzleVerma#######


import sys
import math
mod = 10**9+7
from bisect import bisect


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

dp=[[0]*101 for i in range(200005)]
dp[0][0]=1
for i in range(1,200005):
    for j in range(101):
        if (i>j and j!=0):
            dp[i][j]=((dp[i-1][j]%mod)+(dp[i-1][j-1]%mod))%mod
        elif (i==j or j==0):
            dp[i][j]=1

for t in range(IN()):
    n,m,k=LI()
    li=LI()
    m-=1
    ans=0
    li.sort()
    for i in range(n):
        ind=bisect(li,li[i]+k)
        ind-=(i+1)
        ans+=(dp[ind][m])
    print(int(ans%mod))
