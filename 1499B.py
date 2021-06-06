#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    s=S()
    st=-1
    lens=len(s)
    for i in range(1,lens):
        if s[i]=="1":
            if s[i-1]=="1":
                st=i-1
                break
    en=-1
    for i in range(1,lens):
        if s[lens-1-i]=="0":
            if s[lens-i]=="0":
                en=i-1
                break
    if (en==-1 or st==-1):
        print("YES")
    elif en+st>=lens:
        print("YES")
    else:
        print("NO")