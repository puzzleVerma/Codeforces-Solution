#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n,k1,k2=LI()
    w,b=LI()
    tot=2*n
    bl=b*2
    wt=w*2
    flag=0
    if (abs(k1-k2)%2):
        if wt<=(k1+k2-1):
            if bl<=(tot-k1-k2-1):
                print("YES")
                flag=1
    else:
        if wt<=(k1+k2):
            if bl<=(tot-k1-k2):
                print("YES")
                flag=1        
    if flag==0:
        print("NO")