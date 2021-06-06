#######puzzleVerma#######


import sys
import math
mod = 10**9+7
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n,k=LI()
    ans=1
    for i in range(k):
        ans*=n
        ans%=mod
    print(ans)