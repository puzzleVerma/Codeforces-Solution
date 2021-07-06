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
    a,b,c=LI()
    sm=a+b+c
    if sm%9==0:
        mn=sm//9
        if min(a,b,c)>=mn:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")