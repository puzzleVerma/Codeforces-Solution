#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    a,b,c=LI()
    if c==min(a,b):
        print(10**(a-1),10**(b-1))
    elif a==b:
        print(10**(a-1),10**(a-1)+10**(c-1))
    else:
        print(10**(a-1),10**(b-1)+10**(c-1))