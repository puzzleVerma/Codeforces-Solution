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
    li=LI()
    o=[]
    e=[]
    for ele in li:
        if ele%2==0:
            e+=[ele]
        else:
            o+=[ele]
    o+=e
    print(*o)