#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for i in range(IN()):
    n,k=LI()
    a=LI()
    ind=0
    sk=k
    while (k and (ind<n-1)):
        if a[ind]>0:
            a[ind]-=1
            k-=1
        else:
            ind+=1
    a[-1]+=sk-k
    print(*a)