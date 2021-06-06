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
    s=S()
    plm=0
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            plm+=1

    z=0
    for i in s:
        if i=="0":
            z+=1

    if plm>0:
        if z==0:
            print("DRAW")
        elif z==1:
            print("ALICE")
        elif z==2:
            if ((n%2) and s[n//2]=="0"):
                print("DRAW")
            else:
                print("ALICE")
        elif z>2:
            print("ALICE")
        continue
    if z==1:
        print("BOB")
    elif z==0:
        print("DRAW")
    elif z%2:
        print("ALICE")
    else:
        print("BOB")