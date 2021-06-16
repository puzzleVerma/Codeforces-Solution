#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


n=IN()
li=LI()
di={}
flag=0
for i in r(n):
    for j in r(i):
        sm=li[i]+li[j]
        if sm not in di:
            di[sm]=[i,j]
        else:
            if i not in di[sm]:
                if j not in di[sm]:
                    print("YES")
                    print(di[sm][0]+1,di[sm][1]+1,i+1,j+1)
                    flag=1
                    break
    if flag==1:
        break
if flag==0:
    print("NO")

