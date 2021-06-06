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
    li=LI()
    print(n*3)
    for i in r(0,n,2):
        for j in r(3):
            print(2,i+1,i+2)
            print(1,i+1,i+2)
    