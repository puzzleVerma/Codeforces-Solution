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
    s=S()
    l=len(s)
    s=list(s)
    if l==1:
        print(0)
        continue
    ans=0
    for i in range(l):
        if (i<l-1 and s[i]==s[i+1] and s[i]!="-"):
            s[i+1]="-"
            ans+=1
        if (i<l-2 and s[i]==s[i+2]):
            s[i+2]="-"
            ans+=1
    print(ans)