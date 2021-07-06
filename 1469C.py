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
    k-=1
    h=LI()
    mx=h[0]
    mn=h[0]
    for i in range(1,n-1):
        mn-=k
        mx+=k
        if ((h[i]>=mn and h[i]<=mx) or ((h[i]+k)>=mn and (h[i]+k)<=mx)):
            mx=min(mx,h[i]+k)
            mn=max(mn,h[i])
        else:
            print("NO")
            break
    else:
        mn-=k
        mx+=k
        if (h[-1]>=mn and h[-1]<=mx):
            print("YES")
        else:
            print("NO")

