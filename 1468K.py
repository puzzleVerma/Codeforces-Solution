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
    y=dict()
    x=dict()
    yy=0
    xx=0
    s=S()
    t=[[0,0] for i in range(len(s))]
    for i in range(len(s)):
        ele=s[i]
        if ele=="U":
            yy+=1
        elif ele=="D":
            yy-=1
        elif ele=="R":
            xx+=1
        else:
            xx-=1
        y[i]=yy
        x[i]=xx
        t[i][0]=xx
        t[i][1]=yy
    for i in t:
        tc=i
        xx=0
        yy=0
        for j in range(len(s)):
            ele=s[j]
            txx=xx
            tyy=yy
            if ele=="U":
                yy+=1
            elif ele=="D":
                yy-=1
            elif ele=="R":
                xx+=1
            else:
                xx-=1
            if [xx,yy]==tc:
                xx=txx
                yy=tyy
        if [xx,yy]==[0,0]:
            print(*tc)
            break
    else:
        print(0,0)