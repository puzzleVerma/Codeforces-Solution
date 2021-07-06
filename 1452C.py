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
    ans=0
    s=S()
    b1=0
    b2=0
    for ele in s:
        if ele=="(":
            b1+=1
        elif ele=="[":
            b2+=1
        elif ele==")":
            if b1>0:
                b1-=1
                ans+=1
        else:
            if b2>0:
                b2-=1
                ans+=1
    print(ans)