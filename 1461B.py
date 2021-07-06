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
    n,m=LI()
    mat=[[0]*m for i in range(n)]
    for i in range(n):
        cnt=0
        row=S()
        for j in range(m):
            if row[j]=="*":
                cnt+=1
                mat[i][j]=cnt
            else:
                cnt=0
    ans=0
    for i in range(n):
        for j in range(m):
            ind=0
            while (i+ind<n and j+ind<m and mat[i+ind][j+ind]>2*ind):
                ans+=1
                ind+=1
    print(ans)
            