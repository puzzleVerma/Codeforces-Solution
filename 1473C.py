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
    n,k=LI()
    diff=n-k
    diff+=1
    kk=k
    kk-=diff
    ans=[int(i+1) for i in range(kk)]
    while diff:
        ans+=[k]
        k-=1
        diff-=1
    print(*ans)
