#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


n=IN()
li=LI()
li.sort()
dp=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n-2,-1,-1):
    for j in range(i,n):
        dp[i][j]=li[j]-li[i]+min(dp[i+1][j],dp[i][j-1])
print(dp[0][n-1])
