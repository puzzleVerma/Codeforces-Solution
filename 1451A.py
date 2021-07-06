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
    if n==1:
        print(0)
    elif n==2:
        print(1)
    elif n==3:
        print(2)
    elif n%2:
        print(3)
    else:
        print(2)
