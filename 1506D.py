#######puzzleVerma#######


import sys
import math
from typing import DefaultDict
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=IN()
    li=LI()
    dd=DefaultDict(int)
    for ele in li:
        dd[ele]+=1
    ms=0
    for ele in dd:
        ms=max(ms,dd[ele])
    if n%2:
        print(max(1,ms-(n-ms)))
    else:
        print(max(0,ms-(n-ms)))