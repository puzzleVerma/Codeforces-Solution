#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

dp=[1]*(2*10**5 + 11)
for i in range(10,(2*10**5 + 11)):
    dp[i]=(dp[i-10]+dp[i-9])%mod

for t in r(IN()):
    n,k=LI()
    ans=0
    while n:
        x=n%10
        ans+=dp[x+k]
        ans%=mod
        n//=10
    print(ans)