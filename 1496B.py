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
    n,k=LI()
    li=LI()
    li=set(li)
    i=0
    mx=max(li)
    while 1:
        if i not in li:
            mex=i
            break
        i+=1
    if mex>mx:
        print(n+k)
    else:
        if (((mex+mx+1)//2) in li):
            print(n)
        else:
            print(n+min(k,1))