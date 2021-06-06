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
    n,k=LI()
    ans=n-k
    ans+=k//2
    print(ans)
    li=[0]*ans
    ind=0
    for i in r(((k+1)//2),n+1):
        if i!=k:
            li[ind]=i
            ind+=1
    print(*li)