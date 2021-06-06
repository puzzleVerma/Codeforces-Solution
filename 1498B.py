#######puzzleVerma#######


from collections import defaultdict
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
        n,w=LI()
        wli=LI()
        tot=sum(wli)
        dd=defaultdict(int)
        for i in wli:
            dd[i]+=1
        ke=list(set(wli))
        ke.sort(reverse=True)
        blank=w
        height=0
        while tot>0:
            for i in ke:
                while (blank>=i and dd[i]):
                    dd[i]-=1
                    blank-=i
                    tot-=i
            height+=1
            blank=w
        print(height)