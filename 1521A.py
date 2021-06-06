#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    a,b=LI()
    if b==1:
        print("NO")
    else:
        print("YES")
        if b==2:
            print(a*2,a*3,a*5)
        else:
            print(a,a*(b-1),a*b)