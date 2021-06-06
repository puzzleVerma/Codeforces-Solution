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
    if n%11==0:
        print("YES")
    elif n%111==0:
        print("YES")
    else:
        time=12
        while (time>0 and n>=111):
            n-=111
            if n%11==0:
                print("YES")
                break
            time-=1
        else:
            print("NO")