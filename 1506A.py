#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n,m,x=LI()
    ans=0
    ans+=((x-1)%n)*m
    ans+=((x-1)//n)+1
    print(ans)