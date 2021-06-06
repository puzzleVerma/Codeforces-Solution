#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()

def dist(x,y):
    return float((x**2+y**2)**(0.5))
for t in range(IN()):
    n=IN()
    mr=[]
    ms=[]
    for i in range(2*n):
        x,y=LI()
        if x==0:
            mr+=[abs(y)]
        else:
            ms+=[abs(x)]
    ms.sort()
    mr.sort()
    ans=0
    for i in range(n):
        ans+=dist(ms[i],mr[i])
    print(ans)