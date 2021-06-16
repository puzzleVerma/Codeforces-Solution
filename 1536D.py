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
    n=IN()
    arr=LI()
    flag=0
    curr=arr[0]
    pr=dict()
    nx=dict()
    pr[curr]=None
    nx[curr]=None
    for ele in arr[1:]:
        if ele>curr:
            if (nx[curr]==None):
                nx[curr]=ele
                pr[ele]=curr
                nx[ele]=None
            elif (ele<nx[curr]):
                nx[ele]=nx[curr]
                pr[ele]=curr
                pr[nx[curr]]=ele
                nx[curr]=ele
                
            elif (ele==nx[curr]):
                pass
            else:
                flag=1
                break
        elif ele<curr:
            if (pr[curr]==None):
                nx[ele]=curr
                pr[curr]=ele
                pr[ele]=None
            elif (ele>pr[curr]):
                pr[ele]=pr[curr]
                nx[ele]=curr
                # print(ele,nx[ele])
                nx[pr[curr]]=ele
                pr[curr]=ele
                # print(ele,nx[ele])
                # print(ele,curr,pr,nx)
            elif (ele==pr[curr]):
                pass
            else:
                flag=1
                break
        curr=ele
    if flag==1:
        print("NO")
    else:
        print("YES")

