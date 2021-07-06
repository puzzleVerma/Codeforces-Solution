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
    n,m=LI()
    k=LI()
    c=LI()
    k.sort(reverse=True)
    ind=0
    flag=True
    nn=n
    ans=0
    while nn:
        if (flag and (c[k[n-nn]-1]>c[ind])):
            ans+=c[ind]
        else:
            flag=False
            ans+=c[k[n-nn]-1]
        nn-=1
        ind+=1
    print(ans)