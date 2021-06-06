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
    dd={}
    for i in li:
        if i in dd.keys():
            dd[i]+=1
        else:
            dd[i]=1
    arr=list(dd.values())
    arr.sort()
    sm=sum(arr)
    l=len(arr)
    ans=sm
    comp=0
    for i in arr:
        ans=min(ans,sm-(i*l)+comp)
        sm-=i
        l-=1
        comp+=i
    print(ans)


