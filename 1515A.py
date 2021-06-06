#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n,x=LI()
    w=LI()
    if x>sum(w):
        print("YES")
        print(*w)
    elif x==sum(w):
        print("NO")
    else:
        print("YES")
        for i in range(n):
            if x-w[i]!=0:
                x-=w[i]
                print(w[i],end=" ")
            else:
                x-=w[i+1]
                print(w[i+1],end=" ")
                w[i+1]=w[i]
        print()

