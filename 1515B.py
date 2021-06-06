#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=IN()
    if (math.sqrt(n/2)%1==0) or (math.sqrt(n/4)%1==0):
        print("YES")
    else:
        print("NO")