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
    vis=[s[0]]
    flag=True
    for i in range(1,n):
        if ((s[i]!=s[i-1]) and (s[i] in vis)):
            flag=False
            break
        else:
            vis+=[s[i]]
    if flag:
        print("YES")
    else:
        print("NO")