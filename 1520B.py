#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=S()
    num=int(n)
    l=len(n)
    ans=9*(l-1)
    fd=int(n[0])
    ans+=fd-1
    if num>=int(n[0]*l):
        ans+=1
    print(ans)
