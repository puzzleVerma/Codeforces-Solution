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
    n,a,b=LI()
    if a==1:
        n-=1
        if n%b==0:
            print("YES")
        else:
            print("NO")
        continue
    x=1
    while x<=n:
        if (n-x)%b==0:
            print("YES")
            break
        x*=a
    else:
        print("NO")