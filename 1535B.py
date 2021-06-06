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
    o=[]
    e=0
    for i in range(n):
        if (li[i]%2):
            o+=[li[i]]
        else:
            e+=1
    l=len(o)
    ans=0
    n-=1
    while e:
        ans+=n
        n-=1
        e-=1
    for i in range(l):
        for j in range(i+1,l):
            if ((math.gcd(o[i],2*o[j]))>1):
                ans+=1

    print(ans)

