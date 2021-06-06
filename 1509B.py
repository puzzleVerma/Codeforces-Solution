#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=IN()
    s=S()
    c=0
    t=0
    m=0
    flag=0
    for i in s:
        if i=="T":
            c+=1
            t+=1
        else:
            c-=2
            m+=1
        if (m>t or ((t-m)>(n//3))):
            flag=1
            break
    if ((flag==0) and (c==0)):
        print("YES")
    else:
        print("NO")