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
    n=IN()
    a=LI()
    sm=sum(a)
    if sm==n:
        print(0)
    elif sm<n:
        print(1)
    else:
        print(sm-n)
