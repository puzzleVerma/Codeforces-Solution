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
    li=LI()
    ans=n-1
    mx=0
    for i in range(n-1):
        mx+=li[i]
        same=1
        sm=0
        for j in range(i+1,n):
            sm+=li[j]
            if sm==mx:
                same+=1
                sm=0
            elif sm>mx:
                break
        else:
            if sm==0:
                ans=min(ans,n-same)
    print(ans)


