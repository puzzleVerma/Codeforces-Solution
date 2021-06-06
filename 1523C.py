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
    l=IN()
    li=[1]
    curr=0
    print(1)
    if n==1:
        continue
    for i in r(1,n):
        l=IN()
        if l==1:
            curr+=1
            li+=[l]
        else:
            for i in reversed(r(curr+1)):
                if ((li[i]+1)==l):
                    li[i]+=1
                    li=li[:i+1]
                    curr=i
                    break
        print('.'.join([str(ele) for ele in li]))

