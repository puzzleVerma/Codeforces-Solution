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
    sli=sorted(li)
    if li==sli:
        print(0)
    elif ((li[0]==sli[0]) or (li[-1]==sli[-1])):
        print(1)
    elif ((li[0]==sli[-1]) and (li[-1]==sli[0])):
        print(3)
    else:
        print(2)