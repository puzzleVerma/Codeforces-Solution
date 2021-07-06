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
    ans=[]
    i=0
    ind=0
    while i<n:
        ans+=[li[ind]]
        i+=1
        if i>=n:
            break
        ans+=[li[n-1-ind]]
        ind+=1
        i+=1
    print(*ans)