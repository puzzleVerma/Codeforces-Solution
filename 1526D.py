#######puzzleVerma#######


import sys
import math
mod = 10**9+7
import heapq

LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

n=int(input())
arr=LI()
li=[]
heapq.heapify(li)
sm=0
ans=0
for i in arr:
    sm+=i
    heapq.heappush(li,i)
    if sm>=0:
        ans+=1
    else:
        sm-=heapq.heappop(li)

print(ans)
