#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


if 1:
    n,k=LI()
    alp="abcdefghijklmnopqrstuvwxyz"
    init=0
    while n:
        print(alp[init],end="")
        n-=1
        it=init+1
        if it==k:
            init=0
            continue
        while n:
            print(alp[init],end="")
            n-=1
            if n:
                print(alp[it],end="")
                n-=1
            it+=1
            if it==k:
                break
        init+=1
        if init==k:
            init=0
    print()