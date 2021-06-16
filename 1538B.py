#######puzzleVerma#######


import sys
import math
mod = 10**9+75




LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


for t in r(IN()):
    n=IN()
    li=LI()
    sm=sum(li)
    ans=0
    if sm%n==0:
        avg=sm//n
        for ele in li:
            if ele>avg:
                ans+=1
        print(ans)
    else:
        print(-1)