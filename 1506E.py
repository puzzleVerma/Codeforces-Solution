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
    ddx=DefaultDict(int)
    ddn=DefaultDict(int)
    mn={li[0]}
    mx={li[0]}
    ddx[li[0]]=1
    ddn[li[0]]=1
    st=1
    en=li[0]
    for i in range(1,n):
        ele=li[i]
        if ele>li[i-1]:
            mx.add(ele)
            mn.add(ele)
            ddx[ele]=1
            ddn[ele]=1
            if ele>(li[i-1]+1):
                en=ele
        else:
            while (ddx[en]):
                en-=1
            ddx[en]=1
            mx.add(en)
            while (ddn[st]):
                st+=1
            ddn[st]=1
            mn.add(st)
            st+=1
    print(*mn)
    print(*mx)
