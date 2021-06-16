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
    li=[0]+li+[0]
    ans=0
    for i in range(1,n+1):
        if ((li[i]>li[i-1]) and (li[i]>li[i+1])):
            st=li[i]
            li[i]=max(li[i-1],li[i+1])
            ans+=st-li[i]
    for i in range(1,n+2):
        ans+=abs(li[i]-li[i-1])
    print(ans)




        