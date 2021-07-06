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
    xx=[]
    yy=[]
    for i in range(n):
        x,y=LI()
        xx+=[x]
        yy+=[y]
    for i in range(n):
        for j in range(n):
            if ((abs(xx[i]-xx[j])+abs(yy[i]-yy[j]))>(k)):
                break
        else:
            print(1)
            break
    else:
        print(-1)