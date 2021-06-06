#######puzzleVerma#######


import sys
import math
from typing import DefaultDict
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


for t in r(IN()):
    n,m=LI()
    a=LI()
    dd=DefaultDict(int)
    ans=0
    for ele in a:
            dd[ele%m]+=1
    if dd[0]:
        ans+=1
    for i in range(1,m//2+1):
        if (dd[i] and dd[m-i]):
            ans+=max(1,abs(dd[i]-dd[m-i]))
        else:
            ans+=dd[i]
            ans+=dd[m-i]
    print(ans)




