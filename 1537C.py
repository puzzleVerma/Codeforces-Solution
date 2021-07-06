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
    h=LI()
    h.sort()
    mn=10**10
    mnind=10**10
    for i in range(1,n):
        if (h[i]-h[i-1])<mn:
            mnind=i
            mn=(h[i]-h[i-1])
    ans=[]
    ans+=[h[mnind-1]]
    ans+=h[mnind+1:n]
    ans+=h[:mnind-1]
    ans+=[h[mnind]]
    # # ans[0]=h[mnind-1]
    # # ans[-1]=h[mnind]
    # # print(*ans)
    # # h.remove(h[mnind])
    # # h.remove(h[mnind-1])
    # # ans[1:n-1]=h
    # fin=ans2+ans
    print(*ans)
