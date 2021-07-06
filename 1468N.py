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
    c=LI()
    a=LI()
    for i in range(3):
        c[i]-=a[i]
        if c[i]<0:
            print("NO")
            break
    else:
        a[3]=max(0,a[3]-c[0])
        a[4]=max(0,a[4]-c[1])
        if c[2]>=(a[3]+a[4]):
            print("YES")
        else:
            print("NO")