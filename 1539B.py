#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

al="abcdefghijklmnopqrstuvwxyz"
al=list(al)
d=dict()
for i in range(26):
    d[al[i]]=i+1

n,q=LI()
s=S()
ansd=dict()
for i in range(n):
    ansd[i+1]=d[s[i]]
smd=dict()
smd[0]=0
sm=0
for i in range(n):
    sm+=ansd[i+1]
    smd[i+1]=sm

for i in range(q):
    l,r=LI()
    ans=smd[r]
    ans-=smd[l-1]
    print(ans)

