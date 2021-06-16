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
    li=LI()
    if n==1:
        print(0)
        continue
    if n==2:
        if li[0]==li[1]:
            print(0)
        else:
            print(1)
        continue
    if (min(li)==max(li)):
        print(0)
        continue


    d=dict()
    for i in reversed(range(n)):
        if li[i]!=li[i-1]:
            ind=i
            break

    n=ind+1

    if n==1:
        print(0)
        continue

    flag=0
    for i in range(1,n-1):
        if li[i]!=li[i-1]:
            if flag==0:
                ii=i
                flag=1
            if li[i] not in d:
                d[li[i]]=1
            else:
                d[li[i]]+=1
    f=li[0]
    l=li[-1]
    # if l==f:
    #     if (li.count(f)==2):
    #         print(1)
    #         continue
    # if li.count(f)==1:
    #     print(1)
    #     continue
    # if li.count(l)==1:
    #     print(1)
    #     continue
    if f not in d:
        print(1)
        continue
    if l not in d:
        print(1)
        continue
    mn=10**8

    for ele in d.values():
        if ele<mn:
            mn=ele
    print(mn+1)
