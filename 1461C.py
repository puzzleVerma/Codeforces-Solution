#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
LIF=lambda:[float(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
F=lambda:float(input())
S=lambda:input()
r=range


for t in r(IN()):
    n,m=LI()
    a=LI()
    ind=-1
    for i in reversed(range(n)):
        if a[i]!=i+1:
            ind=i
            break
    pro=[]
    ans=1
    for i in r(m):
        l,p=LIF()
        if l>ind:
            ans*=(1-p)
    if ind==-1:
        print(1.000000)
        continue
    ans=1-ans
    print("%.6f" %ans)
