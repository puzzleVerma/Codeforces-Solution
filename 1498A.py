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
    while 1:
        sn=str(n)
        num=0
        for i in sn:
            num+=int(i)
        if math.gcd(n,num)>1:
            print(n)
            break
        n+=1