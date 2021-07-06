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

from heapq import heappop, heappush, heapify
heap = []
heapify(heap)
done=DefaultDict(int)
ind=1
ans=[]
amt=DefaultDict(list)
amtind=DefaultDict(int)
ser=1

q=IN()
for i in range(q):
    itm=LI()
    if itm[0]==1:
        heappush(heap,(-1)*itm[1])
        amt[itm[1]]+=[ser]
        ser+=1

    elif itm[0]==2:
        while done[ind]!=0:
            ind+=1
        ans+=[ind]
        done[ind]=1
    else:
        ele=heappop(heap)
        ele*=(-1)
        tans=amt[ele][amtind[ele]]
        amtind[ele]+=1
        while done[tans]!=0:
            ele=heappop(heap)
            ele*=(-1)
            tans=amt[ele][amtind[ele]]
            amtind[ele]+=1
        ans+=[tans]
        done[ans[-1]]=1
print(*ans)


        

