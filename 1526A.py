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
    n*=2
    li=LI()
    li.sort()
    ans=[0]*n
    ind=0
    for i in r(0,n,2):
        ans[i]=li[ind]
        ind+=1
    for i in range(1,n,2):
        ans[i]=li[ind]
        ind+=1
    print(*ans)