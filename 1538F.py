#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

def change(num):
    ans=0
    while num:
        ans+=num
        num//=10
    return ans


for t in r(IN()):
    l,r=LI()
    print(change(r)-change(l))
