#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


n=IN()
a=LI()
s=sum(a)
if s%2==1:
    print(0)
    sys.exit()
s//=2
dp=[[False for i in range((s)+1)] for j in range(n+1)]

for i in range(n+1):
    dp[i][0]=True
for i in range(s+1):
    dp[0][i]=False
for i in range(1,n+1):
    for j in range(1,s+1):
        if a[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j] or dp[i-1][j-a[i-1]]
if dp[n][s]:
    flag=1
    while flag:
        for i in range(n):
            if a[i]%2==1:
                print(1)
                print(i+1)
                flag=0
                break
            else:
                a[i]/=2
else:
    print(0)

