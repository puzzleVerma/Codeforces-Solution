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
    if n%3==0:
        print(n//3,n//3,n//3)
    else:
        if (n%2):
            print(1,n//2,n//2)
        else:
            if (n%4):
                print(2,(n-2)//2,(n-2)//2)
            else:
                print(n//2,n//4,n//4)