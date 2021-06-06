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
    li=LI()
    a=li[:2]
    b=li[2:]
    li.sort()
    if ((li[0] in a) and (li[1] in b)):
        print("YES")
    elif ((li[0] in b) and (li[1] in a)):
        print("YES")
    else:
        print("NO")