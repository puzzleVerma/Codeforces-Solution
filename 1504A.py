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
    s=S()
    ind=-1
    for i in r(len(s)):
        if s[len(s)-1-i]!="a":
            ind=i
            break
    if ind==-1:
        print("NO")
    else:
        print("YES")
        for i in r(len(s)):
            if i==ind:
                print("a",end="")
            print(s[i],end="")
        print()