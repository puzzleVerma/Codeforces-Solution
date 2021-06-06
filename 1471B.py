#######puzzleVerma#######
 
 
import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
 
 
for i in range(IN()):
    n,x=LI()
    a=LI()
    sm=sum(a)
    ans=0
    ndi=0
    co=10**9
    for i in range(n):
        ele=a[i]
        tco=1
        while ele%x==0:
            tco+=1
            ele/=x
        if tco<co:
            co=tco
            ndi=i
    ans+=sum(a[:ndi])
    ans+=(sm*co)
    print(ans)