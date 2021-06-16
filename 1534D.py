#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

n=IN()
print("?",1,flush=True)
li=LI()
t=n-1
o=0
ans=dict()
for i in range(n):
    if li[i]==1:
        t-=1
        ans[1]=i+1
        o+=1
        oo=i+1
if o==1:
    for i in range(n):
        if li[i]==1:
            t-=1
            ans[oo]=i+1


