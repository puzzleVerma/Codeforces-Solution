#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=IN()
    a=LI()
    pre=0
    for i in range(n):
        pre^=a[i]
        prea=0
        flag=0
        for j in range(i+1,n):
            prea^=a[j]
            if prea==pre:
                prea=0
                flag=1
        if (flag and (not prea)):
            print("YES")
            break
    if (not flag):
        print("NO")
    