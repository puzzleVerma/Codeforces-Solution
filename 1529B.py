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
    m=0
    diff=2*mod
    li.sort()
    if n==1:
        print(1)
        continue
    if li[0]>0:
        print(1)
        continue
    for i in r(n):
        if i>=1:
            diff=min(diff,li[i]-li[i-1])
        if li[i]<=0:
            m+=1
        else:
            if li[i]<=diff:
                m+=1
            else:
                break
    print(m)
        