#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    k=int(input())
    if (math.gcd(k,100-k)!=1):
        print(int(100/math.gcd(k,100-k)))
    else:
        print(100)