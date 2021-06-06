#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n,k=LI()
    s=S()
    st=0
    en=-1
    t1=1
    t2=1
    for i in range(n):
        if s[i]=="*" and t1:
            st=i
            t1=0
        if s[n-1-i]=="*" and t2:
            en=n-1-i
            t2=0
        if (not t1 and not t2):
            break
    if st==en:
        print(1)
        continue
    ind=st
    ans=2
    while ind<en:
        ind+=k
        if ind>=en:
            break
        while s[ind]!="*":
            ind-=1
        ans+=1
    print(ans)



