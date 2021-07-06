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
    n,q=LI()
    s=S()
    for qq in range(q):
        l,r=LI()
        ll=s[l-1]
        rr=s[r-1]
        for i in range(l-1):
            if s[i]==ll:
                print("YES")
                break
        else:
            for i in range(r,n):
                if s[i]==rr:
                    print("YES")
                    break
            else:
                print("NO")
