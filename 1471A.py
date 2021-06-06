#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input=lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for i in range(IN()):
    n,x=LI()
    a=LI()
    mx=0;mn=0;sm=0
    for ele in a:
        if ele%x==0:
            mx+=math.ceil(ele/x);mn+=math.ceil(ele/x)
        else:
            mx+=math.ceil(ele/x)
            sm+=ele
    mn+=math.ceil(sm/x)
    print(mn,mx)