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
    n=IN()
    li=LI()
    b=[0]*n
    for i in range(1,n):
        if li[i]>li[i-1]:
            if li[i]%li[i-1]==0:
                pass
            else:
                rem=li[i]%li[i-1]
                if rem>(li[i-1]-rem):
                    li[i]+=(li[i-1]-rem)
                    if li[i]>10**9:
                        li[i]-=(li[i-1])
                else:
                    li[i]-=rem
        else:
            li[i]=1
        b[i-1]=li[i-1]
    b[n-1]=li[n-1]
    print(*b)